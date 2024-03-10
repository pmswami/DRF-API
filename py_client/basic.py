import requests

# endpoint = f"https://httpbin.org/"
endpoint = f"https://httpbin.org/anything"
# response = requests.get(endpoint, json={"msg":"Hello Wolrd"})
response = requests.get(endpoint, data={"msg":"Hello World"})
# print(response.text)

# JSON => JavaScript Object Notation
# Very much similar to Python Dict

print("json_response" ,response.json())
print("response status code" ,response.status_code)