import pytest
import responses

from repositories.app import APP


@pytest.fixture
def client():
    with APP.test_client() as client:
        APP.extensions["cache"].clear()
        yield client


@responses.activate
def test_get_repo(client):
    url = f"https://api.github.com/repos/owner/repo"
    response = {
        "full_name": "test/name",
        "description": "description",
        "clone_url": "clone url",
        "stargazers_count": 500,
        "created_at": "2020-01-17T22:24:45Z",
    }
    responses.add(responses.GET, url, json=response)

    r = client.get("/repositories/owner/repo")

    assert r.get_json() == {
        "fullName": "test/name",
        "description": "description",
        "cloneUrl": "clone url",
        "stars": 500,
        "createdAt": "2020-01-17T22:24:45+00:00",
    }
    assert r.status_code == 200
    assert r.is_json


@responses.activate
def test_404_error(client):
    url = f"https://api.github.com/repos/owner/repo"
    responses.add(responses.GET, url, status=404)

    r = client.get("/repositories/owner/repo")

    assert r.get_json() == {
        "status": 404,
        "error": "Not Found",
        "message": "requested repository does not exist",
    }
    assert r.status_code == 404


@responses.activate
def test_500_error(client):
    url = f"https://api.github.com/repos/owner/repo"
    responses.add(responses.GET, url, status=500)

    r = client.get("/repositories/owner/repo")

    assert r.get_json() == {
        "status": 500,
        "error": "Internal Server Error",
        "message": "the server encountered an unexpected internal server error",
    }
    assert r.status_code == 500
