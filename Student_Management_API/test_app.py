import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

@pytest.fixture
def student_data():
    return {
        "name": "Test",
        "age": 20,
        "course": "AI",
        "email": "test1@test.com"
    }

def test_create_student(student_data):

    response = client.post("/student", json=student_data)

    assert response.status_code == 200 or response.status_code == 201

    data = response.json()

    assert data["name"] == "Test"


def test_get_students():

    response = client.get("/student")

    assert response.status_code in [200,404]
    assert len(response.json()) > 0
    
    
    
def test_delete_students():

    response = client.delete("/student/1")

    assert response.status_code in [200,404]
    assert response.json()["name"] == "Test"
    assert response.json()["age"] == 20
    assert response.json()["email"] == "test1@test.com"
    
