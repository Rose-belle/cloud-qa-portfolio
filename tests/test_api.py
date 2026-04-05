import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# --- FIXTURES ---

@pytest.fixture
def posts_response():
    """Fetch all posts once, reuse across tests."""
    return requests.get(f"{BASE_URL}/posts")

@pytest.fixture
def single_post_response():
    """Fetch a single post once, reuse across tests."""
    return requests.get(f"{BASE_URL}/posts/1")

@pytest.fixture
def created_post():
    """Simulate creating a new post via POST request."""
    payload = {
        "title": "Cloud QA Test Post",
        "body": "This post was created by an automated test.",
        "userId": 1
    }
    return requests.post(f"{BASE_URL}/posts", json=payload)

@pytest.fixture
def not_found_response():
    """Request a post that doesn't exist."""
    return requests.get(f"{BASE_URL}/posts/99999")


# --- GET TESTS ---

def test_get_posts_returns_200(posts_response):
    assert posts_response.status_code == 200

def test_get_posts_returns_list(posts_response):
    assert isinstance(posts_response.json(), list)

def test_get_posts_returns_100_items(posts_response):
    assert len(posts_response.json()) == 100

def test_get_posts_response_time(posts_response):
    """Response should come back in under 3 seconds."""
    assert posts_response.elapsed.total_seconds() < 3

def test_single_post_has_required_fields(single_post_response):
    data = single_post_response.json()
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data

def test_single_post_correct_id(single_post_response):
    assert single_post_response.json()["id"] == 1

def test_single_post_correct_content_type(single_post_response):
    assert "application/json" in single_post_response.headers["Content-Type"]


# --- POST TESTS ---

def test_create_post_returns_201(created_post):
    assert created_post.status_code == 201

def test_create_post_returns_correct_title(created_post):
    assert created_post.json()["title"] == "Cloud QA Test Post"

def test_create_post_returns_id(created_post):
    """A newly created post should have an id assigned."""
    assert "id" in created_post.json()


# --- ERROR HANDLING TESTS ---

def test_not_found_returns_404(not_found_response):
    assert not_found_response.status_code == 404

def test_invalid_endpoint_returns_404():
    response = requests.get(f"{BASE_URL}/nonexistent")
    assert response.status_code == 404