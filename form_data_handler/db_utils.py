from tinydb import TinyDB, Query


db = TinyDB('templates.json')
Templates = Query()


def get_unique_template(fields_set, db_name=db, query_object=Templates):
    template = db_name.search(query_object.fragment(fields_set))
    if len(template) == 1:
        pattern = template[0].copy()
        name = pattern.pop('name')
        if set(fields_set.keys()) == set(pattern.keys()):
            return name


def get_all_templates(db_name=db):
    templates = db_name.all()
    templates.sort(key=lambda k: len(k), reverse=True)
    return templates


def clear_database(db_name=db):
    db_name.truncate()
