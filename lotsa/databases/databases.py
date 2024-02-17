import requests, os

# Authentication

host = os.environ.get('host') if os.environ.get('host') else 'http://localhost:8080'

login_url = f"{host}/api/session"

USER = os.environ.get('user') if os.environ.get('user') else 'a@b.com'
PASSWORD = os.environ.get('password') if os.environ.get('password') else 'metabot1'

login_payload = {"username": f"{USER}", "password": f"{PASSWORD}"}
session = requests.Session()
response = session.post(login_url, json=login_payload, verify=False)

times = os.environ.get('times') if os.environ.get('times') else 10000

for i in range(int(times)):
    # Create database
    create_db_url = f"{host}/api/database"
    create_db_payload = {
        "is_on_demand": False,
        "is_full_sync": False,
        "is_sample": False,
        "cache_ttl": None,
        "refingerprint": False,
        "auto_run_queries": True,
        "schedules": {},
        "details": {
            "host": "postgres-data1",
            "port": 5432,
            "dbname": "sample",
            "user": "metabase",
            "password": "metasample123",
            "schema-filters-type": "all",
            "ssl": False,
            "tunnel-enabled": False,
            "advanced-options": False,
        },
        "name": f"postgres-data-{i}",
        "engine": "postgres"
    }
    response = session.post(create_db_url, json=create_db_payload, verify=False)

    print(f"Created database, group and user {i}, last permission call took {response.elapsed}")