API_KEY = "key=AIzaSyD8mJ00OICojAGrJhshG1S84gw2Euq16BM"
SCM_SERVER = "android.googleapis.com"
SCM_URL = "/gcm/send"

from http.client import HTTPSConnection

test_json_data = """
{
  "registration_ids" : ["APA91bHun4MxP5egoKMwt2KZFBaFUH-1RYqx..."],
  "data" : {
    "action" : "send_signal"
  },
}
"""

headers={"Content-Type":"application/json", "Authorization" : API_KEY}

conn = HTTPSConnection(SCM_SERVER)
conn.request("POST", SCM_URL, body=test_json_data, headers=headers)
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print (data1)
conn.close()



