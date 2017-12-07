import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds129776.mlab.com:29776/odstuff

host = "ds129776.mlab.com"
port = 29776
db_name = "odstuff"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
