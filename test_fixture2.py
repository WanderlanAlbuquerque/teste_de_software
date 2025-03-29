import pytest
import requests
from unittest.mock import MagicMock
#para testar simulações requisição via api Mock
@pytest.fixture
def mock_response():
    mock=MagicMock(spec=requests.Response)
    mock.status_code=200
    mock.json.return_value={"Message":"Sucess"}
    return mock
def test_call_mock1(mock_response):
    response=mock_response
    assert response.status_code == 200
    assert response.json()=={"Message":"Sucess"}
def test_call_mock2(mock_response):
    response=mock_response
    assert response.status_code == 200
    assert response.json()=={"Message":"Sucess"}
    