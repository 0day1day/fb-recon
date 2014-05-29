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

def gather_friends(victim, driver):
    uname = victim.personalInfo["username"]
    driver.get("http://facebook.com/" + uname + "friends/")
# check if friends are found or not
# render entire friendslist by scrolling to bottom
# parse friend name by name, then get username
# parse by div class "fsl fwb fcb"?

