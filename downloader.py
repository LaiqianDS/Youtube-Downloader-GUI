import tkinter as tk
import customtkinter as ctk
import yt_dlp as youtube_dl
from tkinter import messagebox

# Function to download video
def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube video URL")
        return
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': './%(title)s.%(ext)s',
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = ctk.CTk()
root.title("YouTube Video Downloader")

# URL label and entry
url_label = ctk.CTkLabel(root, text="Enter YouTube Video URL:")
url_label.pack(pady=10)

url_entry = ctk.CTkEntry(root, width=400)
url_entry.pack(pady=10)

# Download button
download_button = ctk.CTkButton(root, text="Download", command=download_video)
download_button.pack(pady=20)

# Run the application
root.mainloop()
