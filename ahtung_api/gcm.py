# -*- encoding: utf-8 -*-

from urllib.request import urlopen, Request
import json

API_KEY = "key=AIzaSyD8mJ00OICojAGrJhshG1S84gw2Euq16BM"
SCM_SERVER = "https://android.googleapis.com"
SCM_URL = "/gcm/send"

test_json_data = """
{
  "registration_ids" : ["APA91bHun4MxP5egoKMwt2KZFBaFUH-1RYqx..."],
  "data" : {
    "action" : "send_signal"
  },
}
"""

def send_signal(reg_ids, signal):
    #    req = Request(SCM_SERVER + SCM_URL)
    #    req.add_header("Content-Type","application/json")
    #    req.add_header("Authorization", API_KEY)
    #    print(req.header_items())
    #    con = urlopen(req, data=test_json_data.encode("utf-8"))
    #    data = json.loads(con.read().decode("utf-8"))
    #    print("Senging signal %s to %s" % (signal, reg_ids))
    pass

if __name__ == "__main__":
    send_signal("234", "Warning")
