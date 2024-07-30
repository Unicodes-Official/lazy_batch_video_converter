import os
import customtkinter as ctk
from tkinter import filedialog, messagebox, ttk
import threading
from .conversion import convert_to_mp3, terminate_all_processes, terminate_program

def start_gui():
    def select_folder():
        folder_path = filedialog.askdirectory()
        entry_folder.delete(0, ctk.END)
        entry_folder.insert(0, folder_path)

    def convert_all_videos():
        input_folder = entry_folder.get()
        if not input_folder:
            messagebox.showwarning("Warning", "Please select a folder containing video files.")
            return

        output_folder = os.path.join(input_folder, "audio_extractions")
        os.makedirs(output_folder, exist_ok=True)

        video_files = [f for f in os.listdir(input_folder) if f.endswith((".mp4", ".avi", ".mov", ".mkv"))]

        if not video_files:
            messagebox.showinfo("Information", "No video files found in the selected folder.")
            return

        total_files = len(video_files)

        def run_conversion():
            global terminate_program
            all_converted = True
            button_browse_folder.configure(state="disabled")  # Disabilita il pulsante "Choose Folder"
            button_convert_all.configure(state="disabled")  # Disabilita il pulsante "Extract Audio"
            for index, filename in enumerate(video_files, start=1):
                if terminate_program:
                    break
                input_file = os.path.join(input_folder, filename)
                name, ext = os.path.splitext(filename)
                output_file = os.path.join(output_folder, f"{name}.mp3")
                success = convert_to_mp3(input_file, output_file, label_status, label_progress, label_file_progress, index, total_files, spinner)
                if not success:
                    all_converted = False
                    break
            if all_converted and not terminate_program:
                messagebox.showinfo("Conversion Completed", "All video files have been successfully converted!")
            elif terminate_program:
                messagebox.showinfo("Process Terminated", "The conversion process was terminated.")
            else:
                messagebox.showerror("Error", "An error occurred while converting a file.")
            button_browse_folder.configure(state="normal")  # Riabilita il pulsante "Choose Folder"
            button_convert_all.configure(state="normal")  # Riabilita il pulsante "Extract Audio"

        threading.Thread(target=run_conversion).start()

    def on_closing():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            terminate_all_processes()

    # Configurazione dell'interfaccia grafica
    ctk.set_appearance_mode("dark")  # Modalità scura
    ctk.set_default_color_theme("blue")  # Tema blu

    root = ctk.CTk()
    root.title("Video to MP3 Converter")
    root.geometry("600x550")
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Stile premium
    frame = ctk.CTkFrame(root, corner_radius=15, fg_color=("gray20", "gray20"))
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    label_title = ctk.CTkLabel(frame, text="Extract Audio from Videos", font=("Helvetica", 24, "bold"))
    label_title.pack(pady=10)

    label_folder = ctk.CTkLabel(frame, text="Select folder containing video files:", font=("Helvetica", 16))
    label_folder.pack(pady=10)

    entry_folder = ctk.CTkEntry(frame, width=400, font=("Helvetica", 14))
    entry_folder.pack(pady=10)

    button_browse_folder = ctk.CTkButton(frame, text="Choose Folder", command=select_folder, width=200, font=("Helvetica", 14))
    button_browse_folder.pack(pady=10)

    button_convert_all = ctk.CTkButton(frame, text="Extract Audio", command=convert_all_videos, width=200, font=("Helvetica", 14))
    button_convert_all.pack(pady=20)

    label_status = ctk.CTkLabel(frame, text="Status: Waiting to start...", font=("Helvetica", 14))
    label_status.pack(pady=10)

    spinner = ttk.Progressbar(frame, mode='indeterminate', length=250)
    spinner.pack(pady=10)

    label_progress = ctk.CTkLabel(frame, text="Progress: 0%", font=("Helvetica", 14))
    label_progress.pack(pady=10)

    label_file_progress = ctk.CTkLabel(frame, text="File 0 of 0", font=("Helvetica", 14))
    label_file_progress.pack(pady=10)

    root.mainloop()
