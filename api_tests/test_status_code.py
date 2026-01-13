import requests


def test_status_code(url="https://ya.ru", status_code=200):
    r = requests.get(url)
    assert r.status_code == int(status_code)
