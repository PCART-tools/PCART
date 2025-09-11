from app import create_app

def run_test(test_name, func):
    try:
        func()
        print(f"[✓] Test Pass: {test_name}")
        return True
    except AssertionError as e:
        print(f"[×] Test Failed: {test_name} - Assertion Error: {str(e)}")
    except Exception as e:
        print(f"[×] Test Exception: {test_name} - Unexpected Error: {str(e)}")
    return False

# --------------------------
# Test Cases Design
# --------------------------

def test_unauthorized_access():
    """ Unauthorized Access Test """
    app = create_app()
    client = app.test_client()
    
    response = client.get("/api/tasks")
    assert response.status_code == 401
    assert response.json["error"] == "invalid authorization token"

def test_get_tasks():
    """ Get Tasks Test """
    app = create_app()
    client = app.test_client()
    headers = {"Authorization": "Bearer my-secret-token"}
    
    response = client.get("/api/tasks", headers=headers)
    assert response.status_code == 200
    data = response.json
    assert len(data["tasks"]) == 2
    assert data["tasks"][0]["title"] == "学习Flask"

def test_get_single_task():
    """ Get Single Task Test """
    app = create_app()
    client = app.test_client()
    headers = {"Authorization": "Bearer my-secret-token"}
    
    # Valid Task ID
    response = client.get("/api/tasks/1", headers=headers)
    assert response.status_code == 200
    assert response.json["task"]["id"] == 1
    
    # Invalid Task ID
    response = client.get("/api/tasks/999", headers=headers)
    assert response.status_code == 404
    assert response.json["error"] == "Task Not Found"

def test_create_task():
    """ Create Task Test """
    app = create_app()
    client = app.test_client()
    headers = {"Authorization": "Bearer my-secret-token"}
    
    # Get Initial Task Number 
    initial_response = client.get("/api/tasks", headers=headers)
    initial_count = len(initial_response.json["tasks"])
    
    # Normal Creation
    response = client.post(
        "/api/tasks",
        headers=headers,
        json={"title": "新任务", "description": "测试描述"}
    )
    assert response.status_code == 201
    assert response.json["task"]["id"] == 3
    
    # Verify Task Number Increment
    updated_response = client.get("/api/tasks", headers=headers)
    assert len(updated_response.json["tasks"]) == initial_count + 1
    
    # Missing Required Parameters
    response = client.post("/api/tasks", headers=headers, json={})
    assert response.status_code == 400
    assert response.json["error"] == "Missing Required Parameters"

def test_update_task():
    """ Update Task Test """
    app = create_app()
    client = app.test_client()
    headers = {"Authorization": "Bearer my-secret-token"}
    
    # Normal Update
    response = client.put(
        "/api/tasks/1",
        headers=headers,
        json={"title": "更新标题", "done": True}
    )
    assert response.status_code == 200
    assert response.json["task"]["title"] == "更新标题"
    assert response.json["task"]["done"] is True
    
    # Verify Updates are Persistent 
    verify_response = client.get("/api/tasks/1", headers=headers)
    assert verify_response.json["task"]["title"] == "更新标题"
    
    # Update Non-existent Tasks
    response = client.put("/api/tasks/999", headers=headers, json={"title": "无效"})
    assert response.status_code == 404

# --------------------------
# Main Test Logic
# --------------------------

if __name__ == "__main__":
    tests = [
        ("Unauthorized Access", test_unauthorized_access),
        ("Get Task Lists", test_get_tasks),
        ("Get Single Task", test_get_single_task),
        ("Create Task", test_create_task),
        ("Update Task", test_update_task)
    ]
    
    passed = 0
    total = len(tests)
    
    print("="*50)
    print("Test Suite Running")
    print("="*50 + "\n")
    
    for name, test_func in tests:
        if run_test(name, test_func):
            passed += 1
    
    print("\n" + "="*50)
    print(f"Test Result: Pass {passed} Cases; Failed {total-passed} Cases; Total: {total} Cases")
    print("="*50)
