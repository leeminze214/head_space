import requests

r = requests.get("https://type.fit/api/quotes")
print(r)
a = r.json()
b = a[10]["text"]
print(b)
