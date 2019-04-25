def test_assigments(client, auth):

    with client:
        auth.login()
        response = client.get('/assignments/create')
        assert response.status_code == 200
        assert b'Assignments' in response.data
        assert b'<form method = "post">' not in response.data


def test_assignment_create(client, auth):
    # get the page
    with client:
        response = auth.login()
        assert response.status_code == 200

        response = client.get('/assignments/create')
        assert response.status_code == 200
        assert b'<form method = "post">' not in response.data

        response = client.get('/assignments/create')
        assert response.status_code == 200
        assert b'form class="create-assignment"' in response.data
        assert b'Success!' not in response.data

        response = client.post('/assignments/create', data={
            'name': 'Test 1',
            'due_date': '1999-04-14',
            'description': 'Zach day',
        })
        assert response.status_code == 200
        assert b'Success!' in response.data

def test_assignment_update(client, auth):
    with client:
        response = auth.login()
        assert response.status_code == 200

        response = client.get('/assignments/create')
        assert response.status_code == 200
        assert b'form class="create-assignment"' in response.data
        assert b'Success!' not in response.data

        response = client.post('/assignments/create', data={
            'name': 'Test 1',
            'due_date': '2019-04-25',
            'description': 'Zach day',
        })

        response = client.get('/assignments/1/update')

        response = client.post('/assignments/1/update', data={
            'name': 'Test 1',
            'due_date': '2019-05-08',
            'description': 'Yes',
        })
