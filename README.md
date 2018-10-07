# Python Keylogger
A stealth keylogger for Windows.

##### *DISCLAIMER: This tutorial has been made for educational purposes only. I do not promote malicious practices and will not be responsible for any illegal activities. Use at your own risk.*

To Do list
- [ ] Automate keylogging
- [ ] Add remote monitoring
- [ ] Injection techniques

**Table of Contents**
1. [Introduction](#introduction) 
2. [Before You Start](#before-you-start)
3. [Keylogging](#keylogging)  

## Introduction
Recording the keys struck on a keyboard, commonly referred to as keystroke logging or keyboard capturing, is typically a covert action that the person using they keyboard is unaware that their actions are being monitored. This type of surveillance has the capability to record every keystroke made on that system.

Keystroke logging can be acheived with the help of a keylogger, short for keystroke logger, that allows the person operating the program to capture every keystroke that the user makes and reteive that data.

## Before You Start
The keylogger uses Python 3.0 which means that the target machine must have Python installed in order to run the script.

### Check if Python is Installed
1. Click the Start button
2. Type `Command Prompt` or `cmd` for short. Click Command Prompt from the list of results.
3. Type `python` in the Command Prompt and hit Enter. The response you receive should indicate whether Python is recognized, and if so the current version of Python that is installed.

#### Install Python

1. Verify if Python is installed
2. [Download the latest version for Windows](https://www.python.org/downloads/windows/) from the official Python Software Foundation site.
3. Once the download has finished, run the executable to complete the install.

### Install pynput
This keylogging script uses the [pynput](https://pynput.readthedocs.io/en/latest/) library to monitor input devices.

1. [Download pynput from GitHub](https://github.com/moses-palmer/pynput).
2. Unzip the Navigate to the ```pynput-master``` directory in Windows Powershell or Command Prompt and run the following command to install the package.
```shell
python setup.py install
```

## Keylogging
This keylogger will store typed keys in a file in order of when they were typed.
- start the keylogger (.pyw file type)
- view logging in progress
- stop the keylogger
- how to automatically start the keylogger

---

**References**

- [YouTube: Python Keylogger](https://www.youtube.com/watch?v=x8GbWt56TlY)  