import requests

url = 'http://127.0.0.1:5000/'
Text = input("Enter the text to analyse: ")
r = requests.post(url,json={'text':Text})
print(r.json())