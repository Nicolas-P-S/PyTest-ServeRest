import requests

ENDPOINT = "https://compassuol.serverest.dev/"

def test_call_endpoint():
    r = requests.get(ENDPOINT)
    print(r.text)
    assert r.status_code == 200