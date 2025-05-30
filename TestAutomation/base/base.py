from config.constants import *
import requests
import json
from dotenv import load_dotenv
import os

class BasePage:
    def __init__(self, page):
        self.page = page

    def scroll_into_view(self,locator):
        reference_list = locator
        locator.nth(reference_list.count()-1).scroll_into_view_if_needed()

    def is_visible(self,locator):
        locator.is_visible()

    def validate_response_status(self, question_api):
        load_dotenv()
        # The URL of the API endpoint you want to access
        url = f"{URL}/backend/chat"

        headers = {
            "Content-Type": "application/json",
            "Accept": "*/*",
        }
        payload = {
            "Question": question_api,  # This is your example question, you can modify it as needed
        }
        # Make the POST request
        response = self.page.request.post(url, headers=headers, data=json.dumps(payload), timeout=200000)

        # Check the response status code
        assert response.status == 200, "Response code is " + str(response.status) + " " + str(response.json())

    