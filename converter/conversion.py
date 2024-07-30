import os
import threading
import time
from moviepy.editor import VideoFileClip
from tkinter import messagebox
import psutil
import sys

terminate_program = False

def convert_to_mp3(input_file, output_file, status_label, progress_label, file_progress_label, current_file_index, total_files, spinner):
    global terminate_program
    try:
        status_label.configure(text=f"Loading video file {os.path.basename(input_file)}...")
        video = VideoFileClip(input_file)
        status_label.configure(text="Extracting audio track...")
        audio = video.audio
        status_label.configure(text=f"Extracting audio from {os.path.basename(input_file)}...")

        total_duration = audio.duration
        progress_label.configure(text="Progress: 0%")

        def update_progress():
            while True:
                if terminate_program:
                    return
                current_time = audio.reader.pos / audio.reader.fps
                progress_percentage = (current_time / total_duration) * 100
                if progress_percentage >= 100:
                    progress_label.configure(text="Progress: 100%")
                    break
                progress_message = f"Progress: {progress_percentage:.2f}%"
                progress_label.configure(text=progress_message)
                time.sleep(1)

        file_progress_message = f"File {current_file_index} of {total_files}"
        file_progress_label.configure(text=file_progress_message)

        progress_thread = threading.Thread(target=update_progress)
        progress_thread.start()

        spinner.start()
        audio.write_audiofile(output_file, codec='mp3')
        progress_thread.join()
        spinner.stop()

        status_label.configure(text="Closing video and audio files...")
        video.close()
        audio.close()
        status_label.configure(text=f"Conversion completed for {os.path.basename(input_file)}.")
        return True
    except Exception as e:
        status_label.configure(text=f"An error occurred: {str(e)}")
        return False

def terminate_all_processes():
    global terminate_program
    terminate_program = True
    current_process = psutil.Process(os.getpid())
    for proc in current_process.children(recursive=True):
        proc.kill()
    current_process.kill()
    sys.exit()
