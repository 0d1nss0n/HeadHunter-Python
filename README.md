# HeadHunter

![HeadHunter Logo](https://raw.githubusercontent.com/0d1nss0n/HeadHunter-Python/main/bin/headhunter.png)

## Showcase

![ezgif-2-764ac63be5](https://user-images.githubusercontent.com/55106700/230660106-0db0e26c-1fe1-4390-9fab-1cc12083beea.gif)

## About
HeadHunter is a cross platform, session based command and control (C2) server to handle reverse shell connections from infected zombie devices. The operator of HeadHunter has the ability to switch between multiple infected devices through the interactive shell interface. All communications between HeadHunter and the custom payload are encrypted in NIST recommended RSA 2048 bit asymmetric encryption. 

I am not liable for any damage caused by this software. This software is for educational purposes only. This software is under the discretion of the end user.

## Platforms
HeadHunter has been tested on the following platforms

- GNU/Linux

- OpenBSD

- Microsoft Windows

## Dependencies
Install the dependencies with

```pip3 install -r requirements.txt```


If you're running headhunter on a Debian based GNU/Linux distribution, then install the HeadHunter python library files by using apt.

```sudo apt install python3-rsa python3-netifaces```

## Use Guide (With GNU/Linux)

1. Clone the HeadHunter source
```
git clone https://github.com/Lionskey/HeadHunter
```

2. Change into source directory
```
cd HeadHunter
```

3. Execute install script
```
sudo ./install.sh
```

4. Run HeadHunter interactive shell
```
headhunter
```

Alternatively you can just run the headhunter python file if you would like your file system unchanged.
```
python3 headhunter.py
```


