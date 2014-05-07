# !/usr/bin/env python

def gather_basic_info(victim):
    cont = net.basic.http("http://graph.facebook.com/" + victim.personalInfo["username"] + "/")
    data = parse.json.parse_json(cont)
    if data["code"] == 803:
        print("[*] ERROR: ", data["message"])
    else:
        victim.personalInfo["id"] = data["id"]
        victim.personalInfo["first_name"] = data["first_name"]
        victim.personalInfo["last_name"] = data["last_name"]
        victim.personalInfo["gender"] = data["gender"]
        victim.personalInfo["link"] = data["link"]
