# Py ClipBoard Manager

## Features:
- this lib check for your machine's platform and use system commands to contact with clipboard (copy or paste) in python

- this script works with `linux` `(XORG or Wayland)`, `Windows` and `Macos`

-  I didn't test it on windows and macos

- ~~for linux users! you need to install `xclip` if you use xorg or `wl-clipboard` if you use wayland from your package manager~~ Now! you do not need to do that. I did it for you by providing the requierd binaries from this packages.

## How to install?

- you can clone the repo and import the script (pyclipmgr.py) to your script
```
git clone https://github.com/mohammed-saleh2007/py-clip-mgr
```
- you can also use pip [Project In PyPi here](https://pypi.org/project/pyclipmgr/) to install it (recommended)
```
pip install pyclipmgr
```

## How to use it?

- import the lib in your file 
```
import pyclipmgr
```

- to copy some text
```
pyclipmgr.copy("Some Text")
```

- to paste from clipboard, this will return the clipboard content
```
pyclipmgr.paste()
```

- to print them in terminal
```
print(pyclipmgr.paste())
```

~~- you can use it in your (console/terminal)~~

<!-- ```
~$ pyperclip-copy "Some Text"
~$ pyperclip-paste
Some Text
``` -->

### Hope this script get the work done as it did with me