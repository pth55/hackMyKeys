# hackMyKeys

## Introduction
Welcome to hackMyKeys! This repository contains a simple Python script that logs victim keystrokes along with system information and sends that data remotely to Dropbox using the Dropbox API.

The primary functionality of the script revolves around logging keyboard inputs, including keystrokes, key combinations, and system events such as key presses, releases, and system state changes. Additionally, it captures crucial system information such as processor details, operating system version, machine type, hostname, and private IP address.

To facilitate remote monitoring and data collection, the script leverages the Dropbox API for seamless integration with Dropbox cloud storage. By utilizing this API, the collected keyboard and system data are securely transmitted and stored in a designated Dropbox folder.

hackMyKeys serves as an educational resource for cybersecurity enthusiasts, students, and professionals interested in exploring keylogging techniques, understanding system vulnerabilities, and implementing robust security measures. It underscores the significance of proactive cybersecurity practices and the importance of safeguarding sensitive information against unauthorized access and data breaches.



## Features
- Logs keystrokes from the victim's keyboard.
- Collects system information such as processor, system version, machine type, hostname, and IP address.
- Uploads the collected information securely to Dropbox.

## Requirements
- Python 3.x
- `pynput` - Used to monitor keyboard events.
- `platform` - Used to gather system information.
- `socket` - Used to obtain hostname and IP address.
- `getpass` - Used to retrieve the username of the current user.
- `dropbox` - Used to interact with Dropbox's API.

## Installation
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/pth55/hackMyKeys.git
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Obtain a Dropbox access token and replace `TOC` value with your token in the script and make sure to encode api key to base64 before placing it in `TOC` Variable.

## Usage
1. Run the script `main.py`: goto src folder and run the script with `py` or `python` command 
    ```bash
    python main.py
    ```

2. The script will start logging keystrokes and system information.

3. The collected data will be uploaded to your Dropbox folder linked with API.

## Note
- Use this script responsibly and only for educational or authorized testing purposes.
- Respect privacy and legal boundaries when using this script.
