from flask import Flask, request, jsonify
from .utils import parse_form, get_template_name_if_exists
from .db_utils import get_unique_template, get_all_templates


app = Flask(__name__)


@app.post('/get_form')
def parse_form_data():
    form_data = request.form
    pattern = parse_form(form_data)
    template = get_unique_template(pattern)
    if template:
        return template
    template = get_template_name_if_exists(pattern, get_all_templates())
    return jsonify(template)
