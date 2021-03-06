import requests
from datetime import datetime

USERNAME = "popdog"
TOKEN = "*******"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create Pixela account
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Exercise Graph",
    "unit": "Min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create habit graph
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "80",
}

# Adding a pixel to the graph
#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)

## ------  Amending a pixel---------##
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_data = {
    "quantity": "120"
}

response = requests.put(url=update_endpoint, json=new_data, headers=headers)
print(response.text)






