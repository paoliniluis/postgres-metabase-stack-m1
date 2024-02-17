import requests, os

# Authentication
login_url = f"{os.environ['host']}/api/session"
login_payload = {"username": f"{os.environ['user']}", "password": f"{os.environ['password']}"}
session = requests.Session()
response = session.post(login_url, json=login_payload)

for i in range(int(os.environ['lower']), int(os.environ['upper'])):
    # Create database
    create_db_url = f"{os.environ['host']}/api/database/{i}"
    
    response = session.delete(create_db_url)

    # Create group
    create_group_url = f"{os.environ['host']}/api/permissions/group/{i}"
    response = session.delete(create_group_url)

    print(f"deleted db and group {i}, call took {response.elapsed}")