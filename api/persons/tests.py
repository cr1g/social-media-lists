from common.tests import CustomTestCase


class PersonManagementTest(CustomTestCase):
    def setUp(self):
        super().setUp()

        self._user = {
            'username': 'admin', 'password': 'complexpassword'
        }
        r = self.client.post('/api/auth/token/', self._user)
        self._access_token = r.data['access']
        self._refresh_token = r.data['refresh']

        self._person_payload = {'username': 'jones'}
        
        r = self.client.post(
            '/api/persons/', self._person_payload, auth=self._access_token
        )
        self._person_id = r.data['id']

    def test_can_not_create_if_not_authenticated(self):
        r = self.client.post('/api/persons/', self._person_payload)
        
        assert r.status_code == 401

    def test_can_not_create_with_invalid_data(self):
        self._person_payload.pop('username')
        r = self.client.post(
            '/api/persons/', self._person_payload, auth=self._access_token
        )

        assert r.status_code == 400  
        assert 'username' in r.data

    def test_can_create_with_valid_data(self):
        self._person_payload['username'] = 'trace'
        r = self.client.post(
            '/api/persons/', self._person_payload, auth=self._access_token
        )

        assert r.status_code == 201
        assert r.data['username'] == self._person_payload['username']

    def test_can_not_create_with_existing_username(self):
        r = self.client.post(
            '/api/persons/', self._person_payload, auth=self._access_token
        )

        assert r.status_code == 400
        assert 'username' in r.data

    def test_can_list(self):
        r = self.client.get(
            f'/api/persons/', auth=self._access_token
        )

        assert r.status_code == 200
        assert len(r.data) == 1

    def test_can_read_details(self):
        r = self.client.get(
            f'/api/persons/{self._person_id}/', auth=self._access_token
        )

        assert r.status_code == 200
        assert r.data['username'] == self._person_payload['username']

    def test_can_update_details(self):
        username = 'yves'
        r = self.client.put(
            f'/api/persons/{self._person_id}/', {'username': username}, 
            auth=self._access_token
        )

        assert r.status_code == 200
        assert r.data['username'] == username

    def test_can_destroy(self):
        r = self.client.delete(
            f'/api/persons/{self._person_id}/', auth=self._access_token
        )

        assert r.status_code == 204

        r = self.client.get(
            f'/api/persons/{self._person_id}/', auth=self._access_token
        )

        assert r.status_code == 404


class AccountManagementTest(CustomTestCase):
    def setUp(self):
        super().setUp()

        self._user = {
            'username': 'admin', 'password': 'complexpassword'
        }
        r = self.client.post('/api/auth/token/', self._user)
        self._access_token = r.data['access']
        self._refresh_token = r.data['refresh']

        r = self.client.post(
            '/api/persons/', {'username': 'jones'}, auth=self._access_token
        )
        self._person_id = r.data['id']

        r = self.client.post(
            '/api/social-networks/', {'name': 'aWert'}, auth=self._access_token
        )
        self._network_id = r.data['id']

        self._account_payload = {
            'email': 'account@b4y.com', 'first_name': 'George', 
            'last_name': 'Nitro', 'person': self._person_id, 
            'network': self._network_id
        }
        r = self.client.post(
            '/api/accounts/', self._account_payload, auth=self._access_token
        )
        self._account_id = r.data['id']

    def test_can_not_create_if_not_authenticated(self):
        r = self.client.post('/api/accounts/', self._account_payload)
        
        assert r.status_code == 401

    def test_can_not_create_with_invalid_data(self):
        self._account_payload.pop('first_name')
        r = self.client.post(
            '/api/accounts/', self._account_payload, auth=self._access_token
        )

        assert r.status_code == 400  
        assert 'first_name' in r.data

    def test_can_create_with_valid_data(self):
        self._account_payload['email'] = 'account2@b4y.com'
        r = self.client.post(
            '/api/accounts/', self._account_payload, auth=self._access_token
        )

        assert r.status_code == 201
        assert 'email' in r.data

    def test_can_not_create_with_existing_email_on_same_network(self):
        r = self.client.post(
            '/api/accounts/', self._account_payload, auth=self._access_token
        )

        assert r.status_code == 400
        assert 'email' in r.data['non_field_errors'][0]

    def test_can_list(self):
        r = self.client.get(
            f'/api/accounts/', auth=self._access_token
        )

        assert r.status_code == 200
        assert len(r.data) == 1

    def test_can_read_details(self):
        r = self.client.get(
            f'/api/accounts/{self._account_id}/', auth=self._access_token
        )

        assert r.status_code == 200
        assert r.data['email'] == self._account_payload['email']

    def test_can_update_details(self):
        first_name = 'norris'
        r = self.client.put(
            f'/api/accounts/{self._account_id}/', {'first_name': first_name}, 
            auth=self._access_token
        )

        assert r.status_code == 200
        assert r.data['first_name'] == first_name

    def test_can_destroy(self):
        r = self.client.delete(
            f'/api/accounts/{self._account_id}/', auth=self._access_token
        )

        assert r.status_code == 204

        r = self.client.get(
            f'/api/accounts/{self._account_id}/', auth=self._access_token
        )

        assert r.status_code == 404
