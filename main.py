import customtkinter as ctk
from tkinter import messagebox
import lyricsgenius

# ===== Genius API Setup =====
genius = lyricsgenius.Genius("DFFIVt58UmD7tXMMAa3ZfbrgBBNRJqLsXNgSKyyfHe4LbMWGIaCOUKu_afXgnQhq")

# ===== App Setup =====
ctk.set_appearance_mode("dark")  # Options: "light", "dark", "system"
ctk.set_default_color_theme("green")  # Try "blue", "green", "dark-blue", "purple"

app = ctk.CTk()
app.title("🎵 Lyrics Extractor")
app.geometry("750x650")
app.configure(fg_color="#1e1e2f")  # Background color

# ===== Function to Get Lyrics =====
def get_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()
    try:
        result = genius.search_song(song, artist)
        if result:
            lyrics_box.delete("0.0", "end")
            lyrics_box.insert("0.0", result.lyrics)
        else:
            messagebox.showinfo("Not Found", "Lyrics not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ===== Stylish Title =====
title_label = ctk.CTkLabel(
    app,
    text="🎤 Lyrics Finder",
    font=("Segoe UI Black", 28),
    text_color="#FCA311"
)
title_label.pack(pady=25)

# ===== Inputs =====
artist_entry = ctk.CTkEntry(
    app,
    width=500,
    height=40,
    corner_radius=10,
    placeholder_text="🎶 Enter Artist Name",
    font=("Segoe UI", 14)
)
artist_entry.pack(pady=10)

song_entry = ctk.CTkEntry(
    app,
    width=500,
    height=40,
    corner_radius=10,
    placeholder_text="🎵 Enter Song Title",
    font=("Segoe UI", 14)
)
song_entry.pack(pady=10)

# ===== Get Lyrics Button =====
search_button = ctk.CTkButton(
    app,
    text="✨ Get Lyrics",
    command=get_lyrics,
    fg_color="#7F5AF0",
    hover_color="#6246EA",
    font=("Segoe UI Semibold", 16),
    width=200,
    height=40,
    corner_radius=8
)
search_button.pack(pady=20)

# ===== Lyrics Box =====
lyrics_box = ctk.CTkTextbox(
    app,
    width=700,
    height=350,
    wrap="word",
    font=("Consolas", 13),
    text_color="#EAEAEA",
    fg_color="#2c2c3c",
    corner_radius=10
)
lyrics_box.pack(pady=15)

# ===== Start App =====
app.mainloop()
