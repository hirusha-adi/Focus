# Focus

Focus while doing work or studies for a specified period of time

# How does this work?

This script will edit the hosts file of your computer blocking access from a list of websites.

The computer file hosts is an operating system file that maps hostnames to IP addresses. It is a plain text file.

[Click here](<https://en.wikipedia.org/wiki/Hosts_(file)>) to learn more about the hosts file of an operating system

# Usage

## Arch Linux

run the commands below, line by line

```bash
sudo pacman -Syyuu --noconfirm
sudo pacman -S git python python-pip --noconfirm
cd ~
git clone https://github.com/hirusha-adi/Focus.git
cd Focus
python3 maker.py # start the maker
pyhton3 focus.pyw # start the file generated from the maker.py
# CTRL + Z
# bg
# disown -h
```

## Ubuntu/Debian

run the commands below, line by line

```bash
sudo apt install && sudo apt upgrade -y
sudo apt install git python3 python3-pip -y
cd ~
git clone https://github.com/hirusha-adi/Focus.git
cd Focus
python3 maker.py # start the maker
pyhton3 focus.pyw # start the file generated from the maker.py
# CTRL + Z
# bg
# disown -h
```

## Windows

1. Download and install Python3. Make sure to 'Add to PATH' when install python3

![image1](https://www.tutorials24x7.com/uploads/2019-12-26/files/3-tutorials24x7-python-windows-install.png)

2. Download the code as a .zip file from this [Github Reposotory of Focus](https://github.com/hirusha-adi/Focus)

![image2](https://cdn.discordapp.com/attachments/935515175073763398/937186561299197952/unknown.png)

(this above image might not be the same)

3. Extract the downloaded `.zip` file
4. open `cmd` in that folder
5. run `python maker.py` to start the maker
6. Right click and click on run as administrator on the `focus.pyw` file to start the program

# Special Thanks to:

1. Oshada (`OkSheBroken#7960`) for compiling this script with `pyinstaller` for Windows10x64
