import pytest
from form_data_handler.utils import parse_form, get_template_name_if_exists


testdata = [
    ({}, {}),
    ({'username': 'Jackson'}, {'username': 'text'}),
    ({'comment': '666'}, {'comment': 'text'}),
    ({'spam_here': 'spam@me.now'}, {'spam_here': 'email'}),
    ({'contact': '+7 812 500 00 00'}, {'contact': 'phone'}),
    ({'contact': '+7 (812) 500 00 00'}, {'contact': 'text'}),
    ({'created_at': '2010-01-01'}, {'created_at': 'date'}),
    ({'created_at': '20.12.1999'}, {'created_at': 'date'}),
    ({'created_at': '2010-20-20'}, {'created_at': 'text'}),
    ({'created_at': '30.02.1999'}, {'created_at': 'text'}),
    (
        {
            'first_name': 'Michael',
            'last_name': 'Jackson',
            'phone': '+7 100 100 00 00',
            'email': 'noreply@jackson.com',
            'some_text': 'I really like your music',
            'send': '2020-01-08'
        },
        {
            'first_name': 'text',
            'last_name': 'text',
            'phone': 'phone',
            'email': 'email',
            'some_text': 'text',
            'send': 'date'
        }
    )
]


single_testdata = [
    ({'text': 'text'}, 'Text form'),
    ({'date': 'date'}, 'Date form'),
    ({'phone': 'phone'}, 'Phone form'),
    ({'email': 'email'}, 'Email form'),
    ({'text': 'text', 'text2': 'text'}, 'Text form'),
]

double_testdata = [
    ({'username': 'text', 'email': 'email'}, 'User email form'),
    ({'username': 'text', 'phone': 'phone'}, 'User phone form'),
    ({'username': 'text', 'date': 'date'}, 'User date form'),
    ({'username': 'text', 'fullname': 'text'}, 'User surname form'),
    (
        {'first_name': 'text', 'last_name': 'text'},
        {'first_name': 'text', 'last_name': 'text'}
    )
]


@pytest.mark.parametrize("input, expected", testdata)
def test_parser(input, expected):
    assert parse_form(input) == expected


@pytest.fixture
def single_name_forms():
    return [
        {'name': 'Email form', 'email': 'email'},
        {'name': 'Phone form', 'phone': 'phone'},
        {'name': 'Date form', 'date': 'date'},
        {'name': 'Text form', 'text': 'text'}
    ]


@pytest.fixture
def double_form_names():
    return [
        {'name': 'User email form', 'username': 'text', 'email': 'email'},
        {'name': 'User phone form', 'username': 'text', 'phone': 'phone'},
        {'name': 'User date form', 'username': 'text', 'date': 'date'},
        {'name': 'User surname form', 'username': 'text', 'fullname': 'text'}
    ]


@pytest.mark.parametrize("input, expected", single_testdata)
def test_template_name_single_getter(input, expected, single_name_forms):
    assert get_template_name_if_exists(input, single_name_forms) == expected


@pytest.mark.parametrize("input, expected", double_testdata)
def test_template_name_double_getter(input, expected, double_form_names):
    assert get_template_name_if_exists(input, double_form_names) == expected
