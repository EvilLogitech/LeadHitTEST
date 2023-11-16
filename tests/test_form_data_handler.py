import pytest
import json
import os
from pathlib import Path


rootpath = Path(__file__).parent.parent
test_path = os.path.join(rootpath, 'tests', 'fixtures')
with open(os.path.join(test_path, 'test_cases.json')) as f:
    test_data = json.load(f)
with open(os.path.join(test_path, 'expected.json')) as f:
    expected = json.load(f)

testdata = list(zip(test_data, expected))


def test_closed_pages(client):
    responce = client.get('/')
    assert responce.status_code == 404
    responce = client.get('/get_forms')
    assert responce.status_code == 404


@pytest.mark.parametrize("input, expected", testdata)
def test_forms_data(client, input, expected):
    responce = client.post('/get_form', data=input)
    print(responce.text)
    try:
        res = json.loads(responce.text)
        assert expected == res
    except json.decoder.JSONDecodeError:
        assert expected == responce.text
