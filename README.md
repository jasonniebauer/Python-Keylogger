# Python Keylogger
A stealth keylogger for Windows.

#### Disclaimer
This tutorial has been made for educational purposes only. I do not promote malicious practices and will not be responsible for any illegal activities. Use at your own risk.

**Table of Contents**
1. [Introduction](#introduction) 
2. [Get Started](#get-started)
3. [Keylogging](#keylogging)
4. [Roadmap](#roadmap)

## Introduction
Recording the keys struck on a keyboard, commonly referred to as keystroke logging or keyboard capturing, is typically a covert action that the person using the keyboard is unaware that their actions are being monitored. This type of surveillance has the capability to record every keystroke made on that system.

Keystroke logging can be acheived with the help of a keylogger, short for keystroke logger, that allows the person operating the program to capture every keystroke that the user makes and then retreive that data.

### Prerequisite
This project assumes you have Python 3 already installed on both your machine and the target's to run the keylogger. If not, go ahead and [download the latest version for Windows](https://www.python.org/downloads/windows/) from the official Python Software Foundation.

## Get Started

### Install pynput
Included in this keylogger is the [pynput](https://github.com/moses-palmer/pynput) library, which is used to monitor input devices. We need to install the package to make use of it within our script.

1. Navigate to the **python-keylogger** project folder.
2. Press <kbd>shift</kbd>+ right click the **pynput** folder and then select **Open PowerShell window here**.
3. With the PowerShell window open pointing to the pynput directory, type the following command and press <kbd>Enter</kbd>
    ```shell
    python setup.py install
    ```

## Keylogging
Navigate to the project folder and double click the file labeled **keylogger.pyw** to initiate the script. The `.pyw` file extension allows the script to run in the background to prevent detection.

This keylogger will store typed keys in a **key_log.txt** file in the order of when they were typed.

Stop the keylogger by opening the Task Manager and ending the running Python process.

Start keylogger on startup
1. Press <kbd>⊞ Win</kbd>+<kbd>R</kbd> to show the "RUN" box
2. Type `shell:startup` and press <kbd>Enter</kbd>
3. Copy the **keylogger.pyw** file into this folder
4. Change the path where the log will be stored
    ```python
    log_dir = "C:\Users\Owner\Desktop\logs"
    ```
    
## Roadmap
- [ ] Add remote monitoring
- [ ] Clear log file from target machine
- [ ] Automate injection (start keylogger on boot) [Reference](https://www.youtube.com/watch?v=x8GbWt56TlY)
