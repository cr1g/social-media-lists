from common.tests import CustomTestCase


class PostManagementTest(CustomTestCase):
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

        self._post_payload = {
            'content': 'Just a sentence that has no meaning.', 
            'url': 'http://bar.foo',
            'date_posted': '2022-01-01 00:00:00',
            'account': self._account_id
        }
        r = self.client.post(
            '/api/posts/', self._post_payload, auth=self._access_token
        )
        self._post_id = r.data['id']

    def test_can_not_create_if_not_authenticated(self):
        r = self.client.post('/api/posts/', self._post_payload)
        
        assert r.status_code == 401

    def test_can_not_create_with_invalid_data(self):
        self._post_payload.pop('url')
        r = self.client.post(
            '/api/posts/', self._post_payload, auth=self._access_token
        )

        assert r.status_code == 400  
        assert 'url' in r.data

    def test_can_create_with_valid_data(self):
        r = self.client.post(
            '/api/posts/', self._post_payload, auth=self._access_token
        )

        assert r.status_code == 201

    def test_can_list(self):
        r = self.client.get(
            f'/api/posts/', auth=self._access_token
        )

        assert r.status_code == 200
        assert len(r.data) == 1

    def test_can_read_details(self):
        r = self.client.get(
            f'/api/posts/{self._post_id}/', auth=self._access_token
        )

        assert r.status_code == 200
        assert r.data['url'] == self._post_payload['url']

    def test_can_update_details(self):
        url = 'http://foo.bar'
        r = self.client.put(
            f'/api/posts/{self._post_id}/', {'url': url}, 
            auth=self._access_token
        )

        assert r.status_code == 200
        assert r.data['url'] == url

    def test_can_destroy(self):
        r = self.client.delete(
            f'/api/posts/{self._post_id}/', auth=self._access_token
        )

        assert r.status_code == 204

        r = self.client.get(
            f'/api/posts/{self._post_id}/', auth=self._access_token
        )

        assert r.status_code == 404
