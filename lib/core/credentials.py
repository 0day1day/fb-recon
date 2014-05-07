from getpass import getpass

def fbCreds():
    creds = []
    creds.append(input("FB Username: "))
    creds.append(getpass())
    creds.append(input("Access Token: "))
    return creds
