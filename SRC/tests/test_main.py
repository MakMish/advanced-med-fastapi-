import main
from unittest import mock
from fastapi.testclient import TestClient
from utils.dbconnection import get_db
from fastapi import status,Depends
from users.table import user_table
from sqlalchemy.orm import Session
client=TestClient(main.app)

# def test_check1():
#     resp=client.get("/admin/all")
#     assert resp.status_code==200
#     assert resp.json()!=None
from main import casr

# @mock.patch("main.casr")
# def test_2(mock_res):

#     mock_res.return_value = {
#         "status":" kya haal hai"
#     }

#     result = main.gt()  # direct call

#     assert result == "ho gya"

@mock.patch("main.genai.Client")
def test_3(mock_v2):
    mock_instance=mock_v2.return_value
    mock_instance.models.generate_content.return_value.text="mocked Ai response"
    resp = client.post("/ai", json={"rext": "hello"})

    assert resp.status_code == 200
    assert resp.json()["status"] == "mocked Ai response"
   
   




 