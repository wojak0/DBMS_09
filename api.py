import requests

BASE_URL = "http://localhost:8000"

def get_studenten():
    r = requests.get(f"{BASE_URL}/studenten", timeout=5)
    r.raise_for_status()
    return r.json()
