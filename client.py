from urllib import response
import requests

# response = requests.get("http://127.0.0.1:5000/hello?name=Aditya")
# print(response.text)

# response = requests.post("http://127.0.0.1:5000/echo")
# print(response.text)

# headers = {'Content-Type': 'application/json'}
# response = requests.post("http://127.0.0.1:5000/messages", headers=headers, data='{"message":"Aditya"}')

# # send a binary with requests

# data = open('./data/moon_sky.jpg', 'rb').read()

# headers = {'Content-Type': 'application/octet-stream'}
# response = requests.post("http://127.0.0.1:5000/messages", headers=headers, data=data)
# print(response.text)

response = requests.get("http://127.0.0.1:5000/hello")
print(response.headers)