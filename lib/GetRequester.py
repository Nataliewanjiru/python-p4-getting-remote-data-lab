import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  
            return response.text
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch data from {self.url}: {str(e)}")


    def load_json(self):
          response_body = self.get_response_body()
          try:
              data = json.loads(response_body)  
              return data
          except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse JSON data from {self.url}: {str(e)}")