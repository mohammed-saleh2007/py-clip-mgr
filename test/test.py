from pyclipmgr import pyclipmgr

print("your clipboard have: ", pyclipmgr.paste())

text = input("copy?: ")

pyclipmgr.copy(text)

print("your clipboard have: ", pyclipmgr.paste())
