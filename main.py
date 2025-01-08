import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import os
import shutil


def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def sort_files():
    target_folder = folder_entry.get()

    if not os.path.isdir(target_folder):
        result_text.insert(tk.END, "Invalid folder path\n")
        return

    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        if os.path.isfile(file_path):
            mod_time = os.path.getmtime(file_path)
            timestamp = datetime.fromtimestamp(mod_time).strftime("%Y%m%d")

            new_file_name = f"{timestamp}_{filename}"
            file_ext = os.path.splitext(filename)[1][1:].lower()
            dest_folder = os.path.join(target_folder, file_ext)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            new_file_path = os.path.join(dest_folder, new_file_name)
            shutil.move(file_path, new_file_path)
            result_text.insert(tk.END, f"Moved and renamed {filename} to {new_file_name} in {file_ext} folder\n")

    result_text.insert(tk.END, "Sorting completed\n")



# Create the main window
root = tk.Tk()
root.title("File Sorter")

# Create a frame for the folder selection
folder_frame = tk.Frame(root)
folder_frame.pack(fill=tk.X, pady=10)

folder_label = tk.Label(folder_frame, text="Target Folder:")
folder_label.pack(side=tk.LEFT, padx=10)

folder_entry = tk.Entry(folder_frame)
folder_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)

# Create a frame for the Browse button
browse_frame = tk.Frame(root)
browse_frame.pack(fill=tk.X, pady=5)

browse_button = tk.Button(browse_frame, text="Browse", command=browse_folder)
browse_button.pack(expand=True, fill=tk.X, padx=150)  # Centered with padding

# Create a frame for the result text
result_frame = tk.Frame(root)
result_frame.pack(fill=tk.BOTH, expand=True, pady=10)

result_text = tk.Text(result_frame, height=10)
result_text.pack(fill=tk.BOTH, expand=True, padx=10)

# Create a frame for the Go button
go_frame = tk.Frame(root)
go_frame.pack(fill=tk.X, pady=10)

go_button = tk.Button(go_frame, text="Sort files", command=sort_files)
go_button.pack(expand=True, fill=tk.X, padx=150)  # Centered with padding
root.mainloop()
