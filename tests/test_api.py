from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_town():
    response = client.post(
        "/api/town/",
        json={"name": "Sochi", "latitude": 43.3507, "longitude": 39.4313},
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["name"] == "Sochi"
    town_id = data["id"]

    response = client.get(f"/api/town/{town_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Sochi"
    assert data["id"] == town_id


def test_create_town_bad():
    response = client.post(
        "/api/town/",
        json={"name": "Sochi", "latitude": 43.3507, "lon": "39.4313"},
    )
    assert response.status_code == 422, response.text
    assert response.json() == {
        "detail": [{"loc": ["body", "longitude"], "msg": "field required", "type": "value_error.missing"}]
    }


def test_read_town():
    town_id = 1
    response = client.get(f"/api/town/{town_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Sochi"


def test_read_inexistent_town():
    town_id = 10
    response = client.get(f"/api/town/{town_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Town not found"}


def test_read_towns_list():
    response = client.get("/api/town/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_town():
    town_id = 1
    response = client.put(
        f"/api/town/{town_id}",
        json={"name": "Ivanovo", "latitude": 56.5942, "longitude": 40.5849},
    )
    assert response.status_code == 202, response.text
    data = response.json()
    assert data["name"] == "Ivanovo"
    town_id = data["id"]

    response = client.get(f"/api/town/{town_id}")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Ivanovo"
    assert data["id"] == town_id


def test_update_inexistent_town():
    town_id = 10
    response = client.put(
        f"/api/town/{town_id}",
        json={"name": "Ivanovo", "latitude": 56.5942, "longitude": 40.5849},
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Town not found!"}


def test_delete_town():
    town_id = 1
    response = client.delete(f"/api/town/{town_id}")
    assert response.status_code == 202, response.text

    response = client.get(f"/api/town/{town_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Town not found"}


def test_delete_inexistent_town():
    town_id = 10
    response = client.delete(f"/api/town/{town_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Town not found!"}
