import os
import tkinter as tk
from tkinter import messagebox, PhotoImage
import subprocess

def disable_windows_exe_startup_msconfig():
    try:
        # Run msconfig command to modify startup entries
        subprocess.run(["msconfig", "/startup"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error opening System Configuration Utility (msconfig): {e}")
        return False

def reboot_system():
    # Display a message before rebooting
    messagebox.showinfo("Rebooting", "Make sure you disable 'windows.exe' manually using msconfig before reboot. After rebooting, come back here to remove malicious files by clicking on Remove Malicious files button .")
    # Trigger a system reboot
    subprocess.run(["shutdown", "/r", "/t", "0"], check=True)

def remove_specific_files():
    files_to_delete = [
        "C:\\njq8.exe",
        "C:\\njRAT.exe",
        "C:\\Users\\User\\AppData\\Local\\Temp\\windows.exe",
        "C:\\Users\\User\\AppData\\Local\\Temp\\windows.exe.tmp",
        "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\ecc7c8c51c0850c1ec247c7fd3602f20.exe"
    ]

    for file_path in files_to_delete:
        try:
            os.remove(file_path)
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")

    messagebox.showinfo("File Removal", "Specific files removed.")

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

    disable_njrat_button = tk.Button(window, text="Disable windows.exe (msconfig)", command=disable_windows_exe_startup_msconfig)
    disable_njrat_button.pack(padx=20, pady=10)

    reboot_button = tk.Button(window, text="Reboot", command=reboot_system)
    reboot_button.pack(padx=20, pady=10)

    remove_files_button = tk.Button(window, text="Remove Malicious Files", command=remove_specific_files)
    remove_files_button.pack(padx=20, pady=10)

    # Run the GUI
    window.mainloop()

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

    # Show scan result
    if found_files:
        messagebox.showinfo("Scan Result", "System is infected.\n\nPress 'Disable windows.exe (msconfig)' below and manually disable windows.exe and ecc7c8c51c0850c1ec247c7fd3602f20.exe by clicking start up -> right click on windows.exe and ecc7c8c51c0850c1ec247c7fd3602f20.exe -> disable -> OK.\n\nThen Press 'Reboot' button.")
    else:
        messagebox.showinfo("Scan Result", "System is clean.")

# Create the GUI when the script is run
if __name__ == "__main__":
    create_gui()