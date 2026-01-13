import requests
import random
import pytest


def test_list_all():
    r = requests.get("https://dog.ceo/api/breeds/list/all")
    assert r.status_code == 200
    assert r.json().get("status") == "success"


def test_random_breed():
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    assert r.status_code == 200
    assert r.json().get("status") == "success"


def test_multiple_random(count=random.randint(1, 50)):
    r = requests.get("https://dog.ceo/api/breeds/image/random/" + str(count))
    assert r.status_code == 200
    assert r.json().get("status") == "success"
    assert len(r.json().get("message")) == count, f"Wrong count of images"


@pytest.mark.parametrize("breed",
                         ["mountain", "hound"])
def test_random_image_from_breed(breed):
    r = requests.get("https://dog.ceo/api/breed/" + breed + "/images/random")
    assert r.status_code == 200
    assert r.json().get("status") == "success"
    assert requests.get(r.json()["message"]).status_code == 200, f"Wrong link in response"


@pytest.mark.parametrize("breed",
                         ["bullterrier", "schnauzer"])
def test_list_subbreed_images(breed):
    r = requests.get("https://dog.ceo/api/breed/" + breed + "/images")
    assert r.status_code == 200
    assert r.json().get("status") == "success"
