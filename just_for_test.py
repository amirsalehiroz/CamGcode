import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen


def download_file():
    info_label["text"] = "Downloading file..."
    # Disable the button while downloading the file.
    download_button["state"] = "disabled"
    url = "https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe"
    filename = "python-3.7.2.exe"
    # Open the URL address.
    with urlopen(url) as r:
        with open(filename, "wb") as f:
            # Read the remote file and write the local file.
            f.write(r.read())
    info_label["text"] = "File successfully downloaded!"
    # Re-enable the button.
    download_button["state"] = "normal"


root = tk.Tk()
root.title("Download file with Tcl/Tk")
info_label = ttk.Label(text="Click the button to download the file.")
info_label.pack()
download_button = ttk.Button(text="Download file", command=download_file)
download_button.pack()
root.mainloop()