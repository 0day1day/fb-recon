from getpass import getpass

def fb_creds():
    creds = []
    creds.append(input("FB Username: "))
    creds.append(getpass())
    creds.append(input("Access Token: "))
    return creds
