import requests
from datetime import datetime
import gui

USER = "moazzam"
TOKEN = "abcxyz123789"
GRAPH_ID = "graph1"

gui.UserInterface()


# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)
#
# graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "coding",
#     "unit": "hour",
#     "type": "float",
#     "color": "shibafu",
# }
#
# header = {
#     "X-USER-TOKEN": TOKEN,
# }
#
# # response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# # print(response.text)
#
# post_pixel_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"
#
# date = datetime.now()
#
# post_pixel_config = {
#     "date": date.strftime("%Y%m%d"),
#     "quantity": "3.0",
# }
#
# # post.Post(post_pixel_endpoint, post_pixel_config, header)
#
# # date = datetime(year=2021, month=8, day=12)
# date_format = date.strftime("%Y%m%d")
#
# update_delete_pixel_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{date_format}"
#
# update_config = {
#     "quantity": "21.0",
# }
#
# # put.Put(url=update_delete_pixel_endpoint, json=update_config, header=header)
#
# # delete.Delete(url=update_delete_pixel_endpoint, header=header)
#
# # response = requests.delete(url=update_pixel, headers=header)
# # print(response.text)

