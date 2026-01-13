import requests
import json
import pytest


def test_random_brewery():
    r = requests.get("https://api.openbrewerydb.org/v1/breweries/random")
    assert r.status_code == 200
    assert r.json()[0].get("name")


@pytest.mark.parametrize("count",
                         [9, 4])
def test_multiple_random(count):
    r = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=" + str(count))
    assert r.status_code == 200
    assert len(r.json()) == count


@pytest.mark.parametrize(("id", "name"),
                         [("981cd7dd-8130-4eda-899c-70f3a556e1bd", "Cobblehaus Brewing Company"),
                          ("262002b9-b5bd-4de4-92b2-266a1f21fbdf", "Reuben's Brews Taproom")])
def test_single(id, name):
    r = requests.get("https://api.openbrewerydb.org/v1/breweries/" + id)
    assert r.status_code == 200
    assert r.json().get("id") == id
    assert r.json().get("name") == name


@pytest.mark.parametrize("brewery_type",
                         ["nano", "proprietor"])
def test_by_type(brewery_type):
    r = requests.get("https://api.openbrewerydb.org/v1/breweries?by_type=" + brewery_type + "&per_page=3")
    assert r.status_code == 200
    for brewery in r.json():
        assert brewery["brewery_type"] == type


def test_metadata_brewery():
    r = requests.get("https://api.openbrewerydb.org/v1/breweries/meta?by_country=america")
    assert r.status_code == 200
    assert r.json().get("page") == 1
