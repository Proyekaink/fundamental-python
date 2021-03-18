import requests

print("Hello World")
r = requests.get ('https://google.com')
print(r.status_code)
if r.status == 200:
    print(r.text)