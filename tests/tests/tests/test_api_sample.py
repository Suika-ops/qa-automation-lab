import requests

def test_status_code():
    r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    assert r.status_code == 200
