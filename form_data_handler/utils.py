import re
import validators
from datetime import date

phone_regex = r'\+7( \d{3}){2}( \d{2}){2}'
date_regex = r'(\d{2})\.(\d{2})\.(\d{4})'


def parse_form(form_dict):
    pattern = {}
    for key, value in form_dict.items():
        pattern[key] = get_type_of_field(value)
    return pattern


def get_template_name_if_exists(pattern, templates):
    keys = set(pattern.keys())

    for template in templates:
        equality = True
        name = template.pop('name')
        template_keys = set(template.keys())
        if template_keys != template_keys & keys:
            continue
        for key in template_keys:
            if template[key] != pattern.get(key, None):
                equality = False
        if equality:
            return name
    return pattern


def get_type_of_field(value):
    if validators.email(value):
        return 'email'
    if re.match(phone_regex, value):
        return 'phone'
    isodate = value
    if re.match(date_regex, value):
        isodate = re.sub(date_regex, r'\3-\2-\1', value)
    try:
        _ = date.fromisoformat(isodate)
        return 'date'
    except (ValueError):
        pass
    return 'text'
