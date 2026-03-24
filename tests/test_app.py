import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
from src.app import app

@pytest.mark.asyncio
async def test_get_activities():
    # Arrange
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Act
        response = await ac.get("/activities")
    # Assert
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), dict)

@pytest.mark.asyncio
async def test_signup_activity():
    # Arrange
    activity = "Chess Club"
    email = "testuser@mergington.edu"
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Act
        response = await ac.post(f"/activities/{activity}/signup", params={"email": email})
    # Assert
    assert response.status_code in (status.HTTP_200_OK, status.HTTP_400_BAD_REQUEST)
    # Accept 400 if user already signed up, 200 if new
