import requests

BASE_URL = "http://localhost:8000"
HEADERS = {}

# --- read endpoints ---
def get_studenten():
    r = requests.get(f"{BASE_URL}/studenten", timeout=5)
    r.raise_for_status()
    return r.json()

# --- write mock endpoints to match requested structure ---
def post_student(matrikel: str, nachname: str, vorname: str):
    payload = {"matrikel": matrikel, "nachname": nachname, "vorname": vorname}
    r = requests.post(f"{BASE_URL}/studenten", json=payload, headers=HEADERS, timeout=5)
    r.raise_for_status()
    return r.json()
