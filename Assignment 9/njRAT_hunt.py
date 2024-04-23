import os
import psutil
import tkinter as tk
from tkinter import messagebox, PhotoImage

def scan_for_malware():
    # List of files to scan for
    files_to_scan = [
        "C:\\njq8.exe",
        "C:\\njRAT.exe",
        "C:\\Users\\User\\AppData\\Local\\Temp\\windows.exe",
        "C:\\Users\\User\\AppData\\Local\\Temp\\windows.exe.tmp",
        "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ecc7c8c51c0850c1ec247c7fd3602f20.exe"
    ]

    # Check if files exist
    found_files = [file for file in files_to_scan if os.path.exists(file)]

    # Check if windows.exe process is running
    windows_exe_running = False
    for proc in psutil.process_iter():
        try:
            if proc.name() == "windows.exe":
                windows_exe_running = True
                break
        except psutil.NoSuchProcess:
            pass

    # Show scan result
    if found_files or windows_exe_running:
        messagebox.showinfo("Scan Result", "System is infected.")
    else:
        messagebox.showinfo("Scan Result", "System is clean.")

def remove_njrat():
    # Check if windows.exe process is running and terminate it
    for proc in psutil.process_iter():
        try:
            if proc.name() == "windows.exe":
                proc.terminate()
        except psutil.NoSuchProcess:
            pass

    # List of files to delete
    files_to_delete = [
        "C:\\njq8.exe",
        "C:\\njRAT.exe",
        "C:\\Users\\User\\AppData\\Local\\Temp\\windows.exe",
        "C:\\Users\\User\\AppData\\Local\\Temp\\windows.exe.tmp",
        "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ecc7c8c51c0850c1ec247c7fd3602f20.exe"
    ]

    # Delete files
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")

    messagebox.showinfo("Removal Result", "njRAT removed, windows.exe terminated, and associated files deleted.")

def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Malware Scanner and Remover")

    # Load the background image
    bg_image = PhotoImage(file="mouse.png")  # Update path to your image file

    # Get the dimensions of the image
    img_width = bg_image.width()
    img_height = bg_image.height()

    # Set the size of the GUI window based on the image dimensions
    window.geometry(f"{img_width}x{img_height}")

    # Create a label to hold the background image
    bg_label = tk.Label(window, image=bg_image)
    bg_label.place(relwidth=1, relheight=1)  # Expand the label to cover the whole window

    # Create buttons
    scan_button = tk.Button(window, text="Scan System", command=scan_for_malware)
    scan_button.pack(padx=20, pady=10)

    remove_button = tk.Button(window, text="Remove njRAT", command=remove_njrat)
    remove_button.pack(padx=20, pady=10)

    # Run the GUI
    window.mainloop()

# Create the GUI when the script is run
if __name__ == "__main__":
    create_gui()
