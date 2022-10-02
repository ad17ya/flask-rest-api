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

# response = requests.get("http://127.0.0.1:5000/hello")
# print(response.headers)

# response = requests.get("http://127.0.0.1:5000/users/2")
# print(response.text)

# response = requests.get("http://127.0.0.1:5000/users/8")
# print(response.text)

# Make an unauthorized request
# response = requests.get("http://127.0.0.1:5000/secrets")
# print(response.text)
# print(response.headers)

# Make an authorized request
# response = requests.get("http://127.0.0.1:5000/secrets", auth=("admin", "secret"))
# print(response.text)
# print(response.headers)

response = requests.get("http://127.0.0.1:5000/log")
print(response.text)
