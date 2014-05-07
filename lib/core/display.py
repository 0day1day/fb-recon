# !/usr/bin/env python

def vprint(output, verbose=False):
    if verbose:
        print("[-] " + output)

def eprint(output):
    print("[*] " + output)
