from datetime import datetime
import requests

USERNAME = "camille2021"
TOKEN = "kakelkrlLKSDJVKJB<WXCJKNBVJKXHKUDGFHU"
GRAPH = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH,
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "ichou",
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
today = datetime.now()
post_value = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",
}
response = requests.post(url=post_endpoint, json=post_value, headers=headers)
print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": ""
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
