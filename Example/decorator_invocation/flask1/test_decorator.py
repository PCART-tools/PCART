from app import app

client = app.test_client()
response = client.get("/")

try:
    assert response.status_code == 200
    assert response.data == b"Hello, World!"
    print("All tests pass!")
except AssertionError as e:
    print(f"Test failed: {e}")
