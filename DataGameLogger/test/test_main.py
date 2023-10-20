from .config import client



def test_read_main():
    response = client.get("/auth/register")
    assert response.status_code == 200