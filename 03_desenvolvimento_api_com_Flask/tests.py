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


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]
