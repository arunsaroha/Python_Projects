import requests
from datetime import datetime

USERNAME = "arunsaroha"
TOKEN = f"@123{USERNAME}#123"
GRAPH_ID = "graph1"
TODAY = datetime.now().strftime("%Y%m%d")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
PIXEL_EDIT_ENDPOINT = f"{PIXEL_POST_ENDPOINT}/{TODAY}"

# USER CREATION
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
create_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

# GRAPH CREATION
header = {"X-USER-TOKEN": TOKEN,}
graph_params = {
    "id": GRAPH_ID,
    "name": "My Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "ichou",
}
graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=header)
# link_to_see_graph = "https://pixe.la/v1/users/arunsaroha/graphs/graph1"

# PIXEL ADDITION
pixel_data = {
    "date": TODAY,
    "quantity": "15",
}
# pixel_response = requests.post(url=PIXEL_POST_ENDPOINT,json=pixel_data, headers=header)
# print(pixel_response.text)

# PIXEL UPDATION AND DELETION USING PUT AND DELETE
pixel_update = requests.put(url=PIXEL_EDIT_ENDPOINT, headers=header, json=pixel_data)
pixel_delete = requests.delete(url=PIXEL_EDIT_ENDPOINT, headers=header)
