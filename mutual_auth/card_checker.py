import datetime
import json
import logging

import requests

url='https://sandbox.api.visa.com/cofds-web/v1/datainfo'

user_id = 'KHU6RG1BB38YZC3R5CU021O_kkSj792KyteXoFDnIgYkF7f0Y'
password = 'A9c96L0Y'

cert = './cert.pem'
key = './key_14a8353c-41c9-4434-a6ec-6eeded1b6293.pem'

payload= {
   "requestHeader":{
      "requestMessageId":"6da6b8b024532a2e0eacb1af58581",
      "messageDateTime":"2019-02-35 05:25:12.327"
   },
   "requestData":{
      "pANs":[
         4072208010000000
      ],
      "group":"STANDARD"
   }
}

# payload ={
#    "requestHeader":{
#       "requestMessageId":"6da6b8b024532a2e0eacb1af58581",
#       "messageDateTime":"2019-02-35 05:25:12.327"
#    },
#    "requestData":{
#       "pANs":[
#          4072208010000000
#       ],
#       "group":"STANDARD"
#    }
# }


try:
   response = requests.post(url, 
   cert=(cert, key),
   auth=(user_id, password),
   data=payload
)
except Exception as e:
    print("error" , e)

print(response.json())



# #!/usr/bin/env python
# import requests
# import json

# # Sandbox Server address
# url = 'https://sandbox.api.visa.com/cofds-web/v1/datainfo'

# # Sample data request: This is the payload that we will send to the Sandbox Server
# payload = {
#   "requestHeader": {
#     "requestMessageId": "6da6b8b024532a2e0eacb1af58581",
#     "messageDateTime": "2019-02-35 05:25:12.327"
#   },
#   "requestData": {
#     "pANs": [
#       4072208010000000
#     ],
#     "group": "STANDARD"
#   }
# }

# # Load configuration data
# config_path = 'config.json'
# with open(config_path) as config_file:
#     config = json.load(config_file)
# user_id = config["user_id"]
# password = config["password"]
# cert_path = config["cert_path"]
# key_path = config["key_path"]

# timeout = 10

# # Send request to server
# try:
#     response = requests.post(url,
#                             cert=(cert_path, key_path),
#                             auth=(user_id, password),
#                             json = payload,
#                             timeout=timeout)

#     # Print response data
#     print(response.headers)
#     print(response.content)
# except Exception as e:
#     print(e)