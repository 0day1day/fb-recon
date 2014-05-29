# !/usr/bin/env python

import os

def html_write(filename, html, description, fileExistsCalls=0 ):
    if not filename.endswith() ".html" and not filename.endswith() ".htm":
        filename = filename + ".html"
    if not os.path.lexists(filename):
        fd = open(filename, "w")
        fd.write(html.encode("utf8"))
        fd.close()
    else:
        filename = filename.split('.')[0] + str(fileExistsCalls) + ".html"
        html_write(filename, html, description, fileExistsCalls += 1)

    
        

