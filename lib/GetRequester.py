import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        json_list = []
        json_response = json.loads(self.get_response_body())
        for response in json_response:
            json_list.append(response)
        
        return json_list