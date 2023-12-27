import jsonpickle
from models import User


def main():
    user_json = serialize()
    user = deserialize(user_json)
    print(user_json)  # noqa T201
    print(user)  # noqa T201


def serialize():
    user = User(name="John", password="*%!U8n9erx@GdqK(@J")
    return jsonpickle.dumps(user, indent=4)


def deserialize(json_data):
    return jsonpickle.loads(json_data)


if __name__ == "__main__":
    main()
