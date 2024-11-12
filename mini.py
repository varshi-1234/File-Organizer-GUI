import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    # Get the base path from the file dialog
    base_path = Path(filedialog.askdirectory(title="Select Base Directory"))
    # Create a dictionary to store file extensions and their corresponding directories
    extension_dirs = {}

    # Iterate through the files in the base path
    for current_file in base_path.glob('*'):
        if current_file.is_file():
            # Get the file extension
            file_extension = current_file.suffix[1:].lower()

            # If the extension is not in the dictionary, add it with a new directory
            if file_extension not in extension_dirs:
                extension_dirs[file_extension] = base_path / file_extension
                os.makedirs(extension_dirs[file_extension], exist_ok=True)

            # Move the file to the corresponding directory
            shutil.move(current_file, extension_dirs[file_extension])

    # Display the directories and ask for deletion
    existing_dirs = [d for d in base_path.glob('*') if d.is_dir()]
    for dir_path in existing_dirs:
        if dir_path != base_path:  # Exclude the base path from deletion
            delete_dir = messagebox.askyesno("Delete Directory", f"Do you want to delete the directory '{dir_path}' and its contents?")
            if delete_dir:
                try:
                    shutil.rmtree(dir_path)
                    messagebox.showinfo("Success", f"Directory '{dir_path}' and its contents have been deleted.")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while deleting '{dir_path}': {e}")

# Create the main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("500x500")
root.configure(bg="light pink")

# Create a button to organize files
organize_button = tk.Button(root, text="Organize Files", command=organize_files, bg="blue", padx=100, pady=10, font=('Arial', 14, 'bold'))
organize_button.pack(pady=10)

# Run the main loop
root.mainloop()