import requests
import json
from pathlib import Path
import os

rootpath = Path(__file__).parent.parent
test_path = os.path.join(rootpath, 'tests', 'fixtures', 'test_cases.json')
with open(test_path) as f:
    test_cases = json.load(f)


def send_post_request(test_case):
    url = 'http://127.0.0.1:5000/get_form'
    r = requests.post(url, data=test_case)
    print(r.text)


for test in test_cases:
    send_post_request(test)
