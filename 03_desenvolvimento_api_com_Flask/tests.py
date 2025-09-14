import pytest
import requests

# CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []


# response 200
def test_create_tasks():
    new_task_data = {"title": "Nova tarefa", "description": "Descrição da nova tarefa"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200  # status
    response_json = response.json()
    assert "message" in response_json  # message(se existe, não a msg em si)
    assert "id" in response_json  # se volta id, não o numero do id
    tasks.append(response_json["id"])
