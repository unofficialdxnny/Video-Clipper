import tkinter as tk
from moviepy.editor import VideoFileClip
import os
import subprocess

def chop_video():
    video_path = input_video_path.get()
    part_duration = int(input_part_duration.get())
    output_folder = input_output_folder.get()

    # Clear console
    console_text.delete('1.0', tk.END)

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the video
    try:
        clip = VideoFileClip(video_path)
    except Exception as e:
        console_text.insert(tk.END, f"Error loading video: {e}\n")
        return

    # Calculate total parts
    total_parts = int(clip.duration / part_duration)

    # Split and save each part
    for i in range(1, total_parts + 1):
        start_time = (i - 1) * part_duration
        end_time = i * part_duration
        output_clip = clip.subclip(start_time, end_time)
        try:
            output_clip.write_videofile(f"{output_folder}/part_{i}.mp4")
            console_text.insert(tk.END, f"Part {i} saved successfully.\n")
        except Exception as e:
            console_text.insert(tk.END, f"Error saving part {i}: {e}\n")

    # Clean up
    clip.close()

# Create the main window
window = tk.Tk()
window.title("Video Chopper")

# Input fields
label_video_path = tk.Label(window, text="Video Path:")
label_video_path.grid(row=0, column=0)
input_video_path = tk.Entry(window)
input_video_path.grid(row=0, column=1)

label_part_duration = tk.Label(window, text="Part Duration (seconds):")
label_part_duration.grid(row=1, column=0)
input_part_duration = tk.Entry(window)
input_part_duration.grid(row=1, column=1)

label_output_folder = tk.Label(window, text="Output Folder:")
label_output_folder.grid(row=2, column=0)
input_output_folder = tk.Entry(window)
input_output_folder.grid(row=2, column=1)

# Chop button
chop_button = tk.Button(window, text="Chop Video", command=chop_video)
chop_button.grid(row=3, columnspan=2)

# Console section
console_text = tk.Text(window, width=50, height=10)
console_text.grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()
