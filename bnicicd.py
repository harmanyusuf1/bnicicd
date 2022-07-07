import requests
from datetime import datetime


print("hello world")'
print ("testing CICD BNI")

response = requests.get("https://www.google.com")

# print(response.text)
waktu = datetime.now()

with open("tempResponse/"+str(waktu)+".txt","w") as f:
    f.write(response.text)