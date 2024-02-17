import requests, os

# Authentication
login_url = f"{os.environ['host']}/api/session"
login_payload = {"username": f"{os.environ['user']}", "password": f"{os.environ['password']}"}
session = requests.Session()
response = session.post(login_url, json=login_payload)

for i in range(int(os.environ['lower']), int(os.environ['upper'])):
    elapsed = 0
    # Create database
    create_db_url = f"{os.environ['host']}/api/database"
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
    response = session.post(create_db_url, json=create_db_payload)
    db_time = response.elapsed
    db_id = response.json()["id"]

    # Create group
    create_group_url = f"{os.environ['host']}/api/permissions/group"
    create_group_payload = {"name": f"data{i}"}
    response = session.post(create_group_url, json=create_group_payload)
    group_time = response.elapsed

    group_id = response.json()["id"]

    # Create user
    create_user_url = f"{os.environ['host']}/api/user"
    create_user_payload = {
        "first_name": f"data{i}",
        "last_name": f"data{i}",
        "email": f"data{i}@a.com",
        "user_group_memberships": [
            {"id": 1, "is_group_manager": False},
            {"id": group_id, "is_group_manager": False},
        ],
    }
    response = session.post(create_user_url, json=create_user_payload)
    user_time = response.elapsed

    # Update permissions
    get_permissions_url = f"{os.environ['host']}/api/permissions/graph"
    response = session.get(get_permissions_url)
    graph_time = response.elapsed

    # Get the graph revision
    revision_id = response.json()["revision"]

    update_permissions_url = f"{os.environ['host']}/api/permissions/graph"
    update_permissions_payload = {
        "groups": {
            group_id: {
                db_id: {
                    "data": {
                        "native": "write",
                        "schemas": "all"
                    }
                }
            }
        },
        "revision": revision_id
    }
    response = session.put(update_permissions_url, json=update_permissions_payload)
    permission_time = response.elapsed

    # Now change permissions 5 more times
    response = session.get(get_permissions_url)
    revision_id = response.json()["revision"]
    update_permissions_payload = {
        "groups": {
            group_id: {
                db_id: {
                    "data": {
                        "native": "none",
                        "schemas": "all"
                    },
                    "data_model": {
                        "schemas": "all"
                    },
                    "download": {
                        "schemas": "full"
                    },
                    "details": "yes"
                }
            }
        },
        "revision": revision_id
    }
    response = session.put(update_permissions_url, json=update_permissions_payload)
    elapsed += response.elapsed
    # One
    response = session.get(get_permissions_url)
    elapsed += response.elapsed
    revision_id = response.json()["revision"]
    update_permissions_payload = {
        "groups": {
            group_id: {
                db_id: {
                    "data": {
                        "native": "write",
                        "schemas": "all"
                    }
                }
            }
        },
        "revision": revision_id
    }
    response = session.put(update_permissions_url, json=update_permissions_payload)
    elapsed += response.elapsed

    # Two
    response = session.get(get_permissions_url)
    elapsed += response.elapsed
    revision_id = response.json()["revision"]
    update_permissions_payload = {
        "groups": {
            group_id: {
                db_id: {
                    "data": {
                        "native": "none",
                        "schemas": "all"
                    },
                    "data_model": {
                        "schemas": "all"
                    },
                    "download": {
                        "schemas": "full"
                    },
                    "details": "yes"
                }
            }
        },
        "revision": revision_id
    }
    response = session.put(update_permissions_url, json=update_permissions_payload)
    elapsed += response.elapsed

    # Three
    response = session.get(get_permissions_url)
    elapsed += response.elapsed
    revision_id = response.json()["revision"]
    update_permissions_payload = {
        "groups": {
            group_id: {
                db_id: {
                    "data": {
                        "native": "write",
                        "schemas": "all"
                    }
                }
            }
        },
        "revision": revision_id
    }
    response = session.put(update_permissions_url, json=update_permissions_payload)
    elapsed += response.elapsed

    # Four
    response = session.get(get_permissions_url)
    elapsed += response.elapsed
    revision_id = response.json()["revision"]
    update_permissions_payload = {
        "groups": {
            group_id: {
                db_id: {
                    "data": {
                        "native": "none",
                        "schemas": "all"
                    },
                    "data_model": {
                        "schemas": "all"
                    },
                    "download": {
                        "schemas": "full"
                    },
                    "details": "yes"
                }
            }
        },
        "revision": revision_id
    }
    response = session.put(update_permissions_url, json=update_permissions_payload)
    elapsed += response.elapsed

    # Five
    response = session.get(get_permissions_url)
    elapsed += response.elapsed
    revision_id = response.json()["revision"]
    update_permissions_payload = {
        "groups": {
            group_id: {
                db_id: {
                    "data": {
                        "native": "write",
                        "schemas": "all"
                    }
                }
            }
        },
        "revision": revision_id
    }
    response = session.put(update_permissions_url, json=update_permissions_payload)
    elapsed += response.elapsed

    print(f"{i} db: {db_time} group: {group_time} user: {user_time} graph: {graph_time} permission: {permission_time} final permissions change: {elapsed}")