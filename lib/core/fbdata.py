# !/usr/bin/env python

class Victim:

    count = 0

    def __init__(self, uname):
        Victim.count += 1

        self.personalInfo = {
            "username" : uname,
            "first_name" : "",
            "last_name" : "",
            "id" : "",
            "link" : "".
            "gender" : "",
            "birth_date" : "",
            "location" : "",
            "friend_count" : "",
        }

        self.friendList = []
        self.pictures = []
        self.likes = []
			
class Friend:
    
    count = 0

    def __init__(self, source_friend):
        Friend.count += 1
        self.source_friend = source_friend
    
