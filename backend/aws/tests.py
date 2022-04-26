import requests
import unittest


def test_get_aws_api():
    response = requests.get("http://127.0.0.1:8000/api/aws/virtualmachine")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body[0]["account_id"] == "1243548"
    assert response_body[1]["image_name"] == "arlene"
    assert response_body[2]["region"] == "region 4A"
    assert response_body[3]["account_id"] == "liandro"


def test_get_aws_api_first_object():
    response = requests.get("http://127.0.0.1:8000/api/aws/virtualmachine/1353643")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["account_id"] == "1243548"
    assert response_body["image_name"] == "arlene"
    assert response_body["region"] == "region 4"


def test_get_aws_api_second_object():
    response = requests.get("http://127.0.0.1:8000/api/aws/virtualmachine/gonzales17")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["account_id"] == "arlene123"
    assert response_body["image_name"] == "arl111"
    assert response_body["region"] == "region 4A"


def test_get_aws_api_third_object():
    response = requests.get("http://127.0.0.1:8000/api/aws/virtualmachine/johnlian19")
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["account_id"] == "liandro"
    assert response_body["image_name"] == "lian"
    assert response_body["region"] == "NCR"

class TestStringMethod(unittest.TestCase):
    def test_id(self):
        object = "1353643"
        id = "1353643"
        message = "object has no match instance id"
        self.assertEqual(object, id, message)


if __name__ == '__main__':
    unittest.main()