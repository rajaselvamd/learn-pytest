import requests
import uuid

ENDPOINT = 'https://todo.pixegami.io'

#response = requests.get(ENDPOINT)
#print(response)

#data = response.json()
#print(data)

#status_code = response.status_code
#print(status_code)

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def get_task_list(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def new_task_payload():
    ''' task_id - auto generated, no need to pass
    payload = {
        "content": "sample content",
        "user_id": "test_user",
        "task_id": "sample test task",
        "is_done": False
        }
    '''
    # create task
    user_id = f"test_user_{uuid.uuid4().hex}"
    content = f"test_content_{uuid.uuid4().hex}"
    payload = {
        "content": content,
        "user_id": user_id,
        "is_done": False,
        }    
    return payload

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    print( "response code is ", response.status_code)
    assert response.status_code == 200

def test_can_create_task():
    new_payload = new_task_payload()
    create_task_response = create_task(new_payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    print(data)
    ''' sample output:
    {'task': {'user_id': 'test_user', 'content': 'sample content', 'is_done': False, 'created_time': 1688975954, 'task_id': 'task_e4140ded93ac427788679c940c85fb83', 'ttl': 1689062354}}
    '''
    # verify task id - to ensure created is same
    task_id = data['task']['task_id']
    print(task_id)
    get_task_response = get_task(task_id)
    print( "response code is ", get_task_response.status_code)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['user_id'] == new_payload['user_id']

def test_can_update_task():
    '''
    create a task
    update the task
    get and validate the changes
    '''
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()['task']['task_id']
    new_payload = {
        'user_id': payload['user_id'],
        'task_id': task_id,
        'content': 'sample updated content',
        'is_done': True,
    }
    # update teh task
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    # get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['is_done'] == new_payload['is_done']

def test_can_list_tasks():
    '''
    create 3 task
    list the tasks
    '''
    # create a task
    N = 3
    payload = new_task_payload()
    for _ in range(N):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200
    # get list
    user_id = payload['user_id']
    list_task_response = get_task_list(user_id)
    assert list_task_response.status_code == 200
    get_task_data = list_task_response.json()
    print(get_task_data)
    # verify count
    assert len(get_task_data['tasks']) == N

def test_can_delete_task():
    '''
    create a task
    delete the task
    validate the task, supposed to get error
    '''
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()['task']['task_id']
    print(payload)
    # delete task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200

    # get and validate 
    get_task_response = get_task(task_id)
    print(get_task_response)
    assert get_task_response.status_code == 404
    
