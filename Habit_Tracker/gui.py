import tkinter
import requests


class UserInterface:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Main Panel.")
        self.window.config(padx=20, pady=20, bg="blue")

        self.username()
        self.token()
        self.graphid()
        self.quantity()
        self.date()

        self.register_button = tkinter.Button(
            text="Register",
            font=["Arial", 8, "bold"],
            bg="yellow",
            command=self.new_registration
        )
        self.register_button.grid(row=5, column=0, padx=8, pady=8)

        self.create_button = tkinter.Button(
            text="Create Graph",
            font=["Arial", 8, "bold"],
            bg="yellow",
            command=self.create_graph
        )
        self.create_button.grid(row=5, column=1, padx=8)

        self.enter_button = tkinter.Button(
            text="Enter Details",
            font=["Arial", 8, "bold"],
            bg="yellow",
            command=self.new_pixel
        )
        self.enter_button.grid(row=5, column=2, padx=8)

        self.update_button = tkinter.Button(
            text="Update Details",
            font=["Arial", 8, "bold"],
            bg="yellow",
            command=self.update_pixel
        )
        self.update_button.grid(row=5, column=3, padx=8)

        self.delete_button = tkinter.Button(
            text="Delete Entry",
            font=["Arial", 8, "bold"],
            bg="yellow",
            command=self.delete_pixel
        )
        self.delete_button.grid(row=5, column=4, padx=8)

        self.window.mainloop()

    def username(self):
        self.username_label = tkinter.Label(text="Username : ", bg="blue")
        self.username_label.grid(row=0, column=0)
        self.enter_username = tkinter.Entry(width=40)
        self.enter_username.grid(row=0, column=1, columnspan=4)

    def token(self):
        self.token_label = tkinter.Label(text="Token : ", bg="blue")
        self.token_label.grid(row=1, column=0, pady=8)
        self.enter_token = tkinter.Entry(width=40, show="*")
        self.enter_token.grid(row=1, column=1, columnspan=4)

    def graphid(self):
        self.graphid_label = tkinter.Label(text="Graph_ID : ", bg="blue")
        self.graphid_label.grid(row=2, column=0, pady=8)
        self.enter_graphid = tkinter.Entry(width=40)
        self.enter_graphid.grid(row=2, column=1, columnspan=4)

    def quantity(self):
        self.quantity_label = tkinter.Label(text="Enter hours : ", bg="blue")
        self.quantity_label.grid(row=3, column=0, pady=8)
        self.enter_quantity = tkinter.Entry(width=40)
        self.enter_quantity.grid(row=3, column=1, columnspan=4)

    def date(self):
        self.date_label = tkinter.Label(text="Date (yyyymmdd) : ", bg="blue")
        self.date_label.grid(row=4, column=0, pady=8)
        self.enter_date = tkinter.Entry(width=40)
        self.enter_date.grid(row=4, column=1, columnspan=4)

    def new_registration(self):
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.pixela_params = {
            "token": self.enter_token.get(),
            "username": self.enter_username.get(),
            "agreeTermsOfService": "yes",
            "notMinor": "yes",
        }
        self.response = requests.post(url=self.pixela_endpoint, json=self.pixela_params)
        self.response_check()

    def create_graph(self):
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_endpoint = f"{self.pixela_endpoint}/{self.enter_username.get()}/graphs"
        self.graph_config = {
            "id": self.enter_graphid.get(),
            "name": "coding",
            "unit": "hour",
            "type": "float",
            "color": "shibafu",
        }
        self.header = {
            "X-USER-TOKEN": self.enter_token.get(),
        }
        self.response = requests.post(url=self.graph_endpoint, json=self.graph_config, headers=self.header)
        self.response_check()

    def new_pixel(self):
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.header = {
            "X-USER-TOKEN": self.enter_token.get(),
        }
        self.post_pixel_endpoint = f"{self.pixela_endpoint}/{self.enter_username.get()}/graphs/{self.enter_graphid.get()}"
        self.post_pixel_config = {
            "date": self.enter_date.get(),
            "quantity": self.enter_quantity.get(),
        }
        self.response = requests.post(
            url=self.post_pixel_endpoint,
            json=self.post_pixel_config,
            headers=self.header
        )
        self.response_check()

    def update_pixel(self):
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.header = {
            "X-USER-TOKEN": self.enter_token.get(),
        }
        self.update_pixel_endpoint = f"{self.pixela_endpoint}/{self.enter_username.get()}/graphs/{self.enter_graphid.get()}/{self.enter_date.get()} "
        self.update_config = {
            "quantity": self.enter_quantity.get(),
        }
        self.response = requests.put(
            url=self.update_pixel_endpoint,
            json=self.update_config,
            headers=self.header
        )
        self.response_check()

    def delete_pixel(self):
        self.header = {
            "X-USER-TOKEN": self.enter_token.get(),
        }
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.delete_pixel_endpoint = f"{self.pixela_endpoint}/{self.enter_username.get()}/graphs/{self.enter_graphid.get()}/{self.enter_date.get()}"
        self.response = requests.delete(url=self.delete_pixel_endpoint, headers=self.header)
        self.response_check()

    def response_check(self):
        return print(self.response.text)
