import requests

# endpoint = f"https://httpbin.org/"
# endpoint = f"https://httpbin.org/anything"
# endpoint = "http://127.0.0.1:8000/"
endpoint = "http://127.0.0.1:8000/api/"

# response = requests.get(endpoint, json={"msg":"Hello Wolrd"})
# response = requests.get(endpoint, data={"msg":"Hello World"})

# response = requests.get(endpoint, params={"abc":123},json={"query": "Hello world"}, data={"msg":"Hello World"})
response = requests.get(endpoint, params={"abc":123},json={"query ": "Hello world"})
# print(response.text)

# JSON => JavaScript Object Notation
# Very much similar to Python Dict

print("json_response - " ,response.json())
print("response status code - " ,response.status_code)