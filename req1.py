import requests
# знаменитая библиотека но сам лично не работал с ней
response = requests.get("https://google.com/")
print("Status Code:", response.status_code)
print("Content:", response.text)
