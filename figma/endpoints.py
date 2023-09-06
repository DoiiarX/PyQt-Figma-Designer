"""Utility classes and functions for Figma API endpoints.
"""
import requests


class Files:
    """https://www.figma.com/developers/api#files-endpoints
    """

    API_ENDPOINT_URL = "https://api.figma.com/v1"

    def __init__(self, token, file_key):
        self.token = token
        self.file_key = file_key

    def __str__(self):
        return f"Files {{ Token: {self.token}, File: {self.file_key} }}"

    def get_file(self) -> dict:
        try:
            response = requests.get(
                f"{self.API_ENDPOINT_URL}/files/{self.file_key}?geometry=paths",
                headers={"X-FIGMA-TOKEN": self.token}
            )
        except ValueError:
            raise RuntimeError(
                "Invalid Input. Please check your input and try again.")
        except requests.ConnectionError:
            raise RuntimeError(
                "Tkinter Designer requires internet access to work.")
        else:
            return response.json()

    def get_images(self) -> dict:
        response = requests.get(
            f"{self.API_ENDPOINT_URL}/files/{self.file_key}/images",
            headers={"X-FIGMA-TOKEN": self.token}
        )
        return response.json()['meta']["images"]
