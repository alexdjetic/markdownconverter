# markdownconverter

## install python

### ubuntu/derivate

```fish
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python-pip xterm
```
### fedora

```fish
sudo dnf update && sudo dnf install python3 python-pip xterm
```

### centOS/older fedora

```fish
sudo yum update && sudo yum install python3 python-pip xterm
```

### archlinux/manjaro

```fish
sudo pacman -Syu
sudo pacman -S python3 python-pip xterm
```

### alpine

```fish
apk update && apk upgrade
apk add python
```

### gentoo
- go to the official page: [python install for gentoo](https://wiki.gentoo.org/wiki/Python)

## config file
* an example of config file:
```json
{
  "file": "/home/oem/obsidian/main/NAT.md",
  "namefilehtml": "/home/oem/markdownConverter/nat.html", 
  "title": "NAT",
  "content_type": "text/html"
} 
```

*always use absolut path for now until i made a python script with a class to autoload the config then you can use it*

## run
```fish
python3 app.py -c /path/to/config/file.json #general runing command
python3 app.py -c /home/oem/markdownConverter/config.json #in my case
```
