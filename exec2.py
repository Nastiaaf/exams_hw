# Second assignment - API testing

import unittest
import requests
import json

# A help function to connect to the API
def connect():
    # Get access token
    url = 'http://localhost:8000/api/auth'
    myobj = {'username':'test', 'password':'1234'}
    headers = {'Content-type': 'application/json'}
    access_token = requests.post(url, headers = headers, json = myobj)
    access_token = json.loads(access_token.text)
    return access_token["access_token"]

class MyTestCase(unittest.TestCase):
    # Test correct connection to the API
    def test_correct_connection(self):
        url = 'http://localhost:8000/api/auth'
        myobj = {'username': 'test', 'password': '1234'}
        headers = {'Content-type': 'application/json'}
        access_token = requests.post(url, headers=headers, json=myobj)
        self.assertEqual(access_token.status_code, 200)

    # Test incorrect connection to API with incorrect username
    def test_incorrect_connection(self):
        url = 'http://localhost:8000/api/auth'
        myobj = {'username': 'false_username', 'password': '1234'}
        headers = {'Content-type': 'application/json'}
        access_token = requests.post(url, headers=headers, json=myobj)
        self.assertEqual(access_token.status_code, 401)

    # Try to insert a valid PolyData
    def test_insert_valid_polydata(self):
        access_token = connect()
        url = 'http://localhost:8000/api/poly'
        myobj = {"data": [ { "key": "1234", "val": "Hello, world!", "valType": "str" } ] }
        headers = {'Content-type': 'application/json', "Authorization": "Bearer {"+access_token+"}"}
        res = requests.post(url, headers = headers, json = myobj)
        self.assertEqual(res.status_code, 200)

    # Try to insert invalid empty data
    def test_insert_empty_data(self):
        access_token = connect()
        url = 'http://localhost:8000/api/poly'
        myobj = {}
        headers = {'Content-type': 'application/json', "Authorization": "Bearer {"+access_token+"}"}
        res = requests.post(url, headers = headers, json = myobj)
        self.assertEqual(res.status_code, 400)

    # Try to insert invalid non-empty data
    def test_insert_invalid_data(self):
        access_token = connect()
        url = 'http://localhost:8000/api/poly'
        myobj = {"nope": "epic_fail"}
        headers = {'Content-type': 'application/json', "Authorization": "Bearer {"+access_token+"}"}
        res = requests.post(url, headers = headers, json = myobj)
        self.assertEqual(res.status_code, 400)

    # Try to retrieve existing data
    def test_retrieve_all_polydata(self):
        access_token = connect()
        url = 'http://localhost:8000/api/poly'
        headers = {'Content-type': 'application/json', "Authorization": "Bearer {" + access_token + "}"}
        res = requests.get(url, headers = headers)
        self.assertEqual(res.status_code, 200)

    # Try to retrieve non existing data with id -1
    def test_retrieve_non_existant_polydata(self):
        access_token = connect()
        url = 'http://localhost:8000/api/poly/-1'
        headers = {'Content-type': 'application/json', "Authorization": "Bearer {" + access_token + "}"}
        res = requests.get(url, headers=headers)
        self.assertEqual(res.status_code, 401)

    # Try to insert a Polydata with wrong valtype - int
    def test_insert_wrong_type(self):
        access_token = connect()
        url = 'http://localhost:8000/api/poly'
        myobj = {"data": [ { "key": "1234", "val": "Hello, world!", "valType": "int" } ] }
        headers = {'Content-type': 'application/json', "Authorization": "Bearer {"+access_token+"}"}
        res = requests.post(url, headers = headers, json = myobj)
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
