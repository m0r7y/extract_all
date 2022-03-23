#!/bin/python
import os
from unrar import rarfile

xfile = os.listdir(os.getcwd())
i = 0

for compressed in xfile:
    if not compressed.endswith('.rar'):
        continue
    rar = rarfile.RarFile(compressed)
    print("Extracting : %s" % compressed)
    rar.extractall()
    i += 1

print("%s extracted" % i)
