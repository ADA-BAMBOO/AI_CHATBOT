import requests
from django.test import TestCase, Client
from django.urls import reverse
import json
class test_post(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "https://c8ce-14-241-247-68.ngrok-free.app/"  # Lấy URL API

    def test_valid_json_request(self):
        data = {"message": "do you know ada"}
        response = self.client.post(self.url, data=json.dumps(data), content_type="application/json")
        print("-----------------------------------output---------------------------------------\n")
        print(response.json())
        print("\n-----------------------------------output---------------------------------------")
