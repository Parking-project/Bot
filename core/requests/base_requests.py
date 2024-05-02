import requests
from config import ApiConfig

def send_get_request(url, data, token = None):
    headers = {
        "Content-Type": "application/json",
    }
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.get(
        url=ApiConfig.API_URL+url,
        params=data,
        json={},
        headers=headers
    )
    print("\n\n\nGET = ", headers, "\n\n\n")
    if response.status_code == 500:
        raise Exception(f"Status code is too big: {url} : {response.status_code}\n\n{response.content}")
    return response

def send_post_request(url, json, token = None):
    headers = {
        "Content-Type": "application/json",
    }
    if token is not None:
        headers["Authorization"] = f"Bearer {token}"
    response = requests.post(
        url=ApiConfig.API_URL+url,
        json=json,
        headers=headers
    )
    print("\n\n\POST = ", headers, "\n\n\n")
    if response.status_code == 500:
        raise Exception(f"Status code is too big: {url} : {response.status_code}\n\n{response.content}")
    return response