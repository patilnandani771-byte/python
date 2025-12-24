import os
import tkinter as tk
from tkinter import messagebox

# ---------------- Playlist Class ----------------
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def save_to_file(self):
        folder = "playlists"
        if not os.path.exists(folder):
            os.makedirs(folder)

        filename = os.path.join(folder, f"playlist_{self.name}.txt")

        if os.path.exists(filename):
            raise FileExistsError("Playlist already exists!")

        with open(filename, "w") as file:
            for song in self.songs:
                file.write(song + "\n")

    @staticmethod
    def load_from_file(filepath):
        with open(filepath, "r") as file:
            return file.read()


# ---------------- GUI Application ----------------
class MusicBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MusicBox Playlist Manager")
        self.root.geometry("600x400")

        # Labels
        tk.Label(root, text="Playlist Name").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(root, text="Songs (one per line)").grid(row=1, column=0, padx=10)

        # Entry & Text
        self.playlist_entry = tk.Entry(root, width=30)
        self.playlist_entry.grid(row=0, column=1, padx=10)

        self.song_text = tk.Text(root, width=40, height=8)
        self.song_text.grid(row=1, column=1, padx=10)

        # Buttons
        tk.Button(root, text="Save Playlist", command=self.save_playlist).grid(row=2, column=1, pady=10)

        tk.Label(root, text="Saved Playlists").grid(row=0, column=2)
        self.playlist_listbox = tk.Listbox(root, width=25)
        self.playlist_listbox.grid(row=1, column=2, rowspan=4, padx=10)

        tk.Button(root, text="View Playlist", command=self.view_playlist).grid(row=5, column=2)

        self.load_playlists()

    # ---------------- Save Playlist ----------------
    def save_playlist(self):
        name = self.playlist_entry.get().strip()
        songs = self.song_text.get("1.0", tk.END).strip().split("\n")

        if not name or not songs or songs == [""]:
            messagebox.showerror("Error", "Playlist name or songs cannot be empty!")
            return

        try:
            playlist = Playlist(name, songs)
            playlist.save_to_file()
            messagebox.showinfo("Success", "Playlist saved successfully!")
            self.load_playlists()
            self.clear_fields()
        except FileExistsError:
            messagebox.showerror("Error", "Playlist name already exists!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- Load Playlists ----------------
    def load_playlists(self):
        self.playlist_listbox.delete(0, tk.END)
        if os.path.exists("playlists"):
            for file in os.listdir("playlists"):
                if file.endswith(".txt"):
                    self.playlist_listbox.insert(tk.END, file)

    # ---------------- View Playlist ----------------
    def view_playlist(self):
        try:
            selected = self.playlist_listbox.get(self.playlist_listbox.curselection())
            filepath = os.path.join("playlists", selected)
            content = Playlist.load_from_file(filepath)
            self.song_text.delete("1.0", tk.END)
            self.song_text.insert(tk.END, content)
        except:
            messagebox.showerror("Error", "Please select a playlist!")

    def clear_fields(self):
        self.playlist_entry.delete(0, tk.END)
        self.song_text.delete("1.0", tk.END)


# ---------------- Run Application ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicBoxApp(root)
    root.mainloop()
