import json
import requests

def create_postman_request(url):
    return {
        "name": url,
        "request": {
            "method": "GET",
            "header": [],
            "body": {},
            "url": {
                "raw": url,
                "protocol": "http",
                "host": [url],
            },
        },
        "response": [],
    }

file_path = "input.txt"

try:
    with open(file_path, "r") as file:
        urls = file.read().splitlines()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    exit(1)

postman_collection = {
    "info": {
        "name": "URLs Collection",
        "_postman_id": "unique-id-here",
        "description": "A collection of URLs from a text file.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    },
    "item": [create_postman_request(url) for url in urls],
}

postman_json_path = "postman_collection.json"
with open(postman_json_path, "w") as json_file:
    json.dump(postman_collection, json_file, indent=2)

print(f"Postman collection saved to '{postman_json_path}'")
