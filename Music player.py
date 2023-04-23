import tkinter as tk
from tkinter import filedialog
import pygame
import pytube

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")

        # Create a button for choosing a file
        self.file_button = tk.Button(master, text="Open File", command=self.open_file)
        self.file_button.pack()

        # Create a button for playing the file
        self.play_button = tk.Button(master, text="Play", command=self.play_music)
        self.play_button.pack()

        # Create a button for pausing the file
        self.pause_button = tk.Button(master, text="Pause", command=self.pause_music, state=tk.DISABLED)
        self.pause_button.pack()

        # Create a button for stopping the file
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.pack()

        # Create an input box for entering YouTube video link
        self.link_entry = tk.Entry(master, width=40)
        self.link_entry.pack()

        # Create a button for downloading the YouTube video
        self.download_button = tk.Button(master, text="Download", command=self.download_music)
        self.download_button.pack()

        # Set initial state of pause button and stop button to disabled
        self.paused = False
        self.playing = False

    def open_file(self):
        # Open a file dialog to choose a file
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("Audio Files", "*.mp3;*.wav"), ("all files", "*.*")))
        print("File selected:", self.filename)

    def play_music(self):
        # Initialize pygame mixer
        pygame.mixer.init()

        if not self.playing:
            pygame.mixer.music.load(self.filename)
            pygame.mixer.music.play()
            self.playing = True
            self.pause_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
        else:
            pygame.mixer.music.unpause()
            self.paused = False

    def pause_music(self):
        if not self.paused:
            pygame.mixer.music.pause()
            self.paused = True
        else:
            pygame.mixer.music.unpause()
            self.paused = False

    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

    def download_music(self):
        # Get the YouTube video link from the input box
        link = self.link_entry.get()

        # Create a YouTube object and get the highest quality audio stream
        youtube = pytube.YouTube(link)
        audio_stream = youtube.streams.get_audio_only()

        # Ask the user to choose a file name and location to save the audio file
        save_path = filedialog.asksaveasfilename(initialdir="/", title="Save File", defaultextension=".mp3", filetypes=(("Audio Files", "*.mp3"), ("all files", "*.*")))

        # Download the audio file
        audio_stream.download(output_path=".", filename="temp")
        temp_file_path = "temp." + audio_stream.mime_type.split("/")[-1]
        os.rename(temp_file_path, save_path)

        print("Downloaded:", save_path)

root = tk.Tk()
root.geometry("400x250")
root.title("Music Player")
my_player = MusicPlayer(root)
root.mainloop()
git 