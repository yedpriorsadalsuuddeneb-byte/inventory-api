import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_list_items(client):
    res = client.get("/items")
    assert res.status_code == 200
    assert len(res.get_json()) == 3


def test_get_item(client):
    res = client.get("/items/2")
    assert res.get_json()["name"] == "Gadget"


def test_get_missing_item_returns_404(client):
    assert client.get("/items/999").status_code == 404


def test_total_endpoint(client):
    res = client.get("/items/2/total?quantity=10")
    assert res.get_json()["total"] == 108.0

