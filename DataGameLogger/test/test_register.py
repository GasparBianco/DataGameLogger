from .test_config import client

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
    assert 'password' not in data
    
def test_register_already_existent_username():
    response = client.post(
        "/auth/register",
        json={  "email": "test2@test.com", 
                "password": "Test.1234",
                'username': 'Tester'},
    )
    assert response.status_code == 400, response.text

def test_register_already_existent_email():
    response = client.post(
        "/auth/register",
        json={  "email": "test@test.com", 
                "password": "Test.1234",
                'username': 'Tester2'},
    )
    assert response.status_code == 400, response.text

def test_register_invalid_email():
    response = client.post(
        "/auth/register",
        json={  "email": "test2testcom", 
                "password": "Test.1234",
                'username': 'Tester'},
    )
    assert response.status_code == 422, response.text

def test_register_invalid_username():
    response = client.post(
        "/auth/register",
        json={  "email": "test3@test.com", 
                "password": "Test.1234",
                'username': 'Te'},
    )
    assert response.status_code == 422, response.text

def test_register_invalid_password():
    response = client.post(
        "/auth/register",
        json={  "email": "test3@test.com", 
                "password": "Te",
                'username': 'Tester3'},
    )
    assert response.status_code == 422, response.text