import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_returns_200():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

def test_get_posts_returns_list():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert isinstance(data, list)

def test_get_posts_returns_100_items():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert len(data) == 100

def test_single_post_has_required_fields():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data