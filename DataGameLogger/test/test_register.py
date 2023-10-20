from .config import client

def test_register_new_user_succed():
    response = client.post(
        "/auth/register",
        json={  "email": "test@test.com", 
                "password": "Test.1234",
                'username': 'Tester'},
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["email"] == "test@test.com"
    assert data["username"] == "Tester"
    assert "id" in data
    