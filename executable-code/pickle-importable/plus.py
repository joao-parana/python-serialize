def create_plus(x):
    def plus(y):
        return x + y

    return plus


plus_one = create_plus(1)
plus_two = lambda x: x + 2  # noqa E731

for i in range(5):
    print(f"{i = }")  # noqa T201
    print(f"{plus_one(i) = }")  # noqa T201
    print(f"{plus_two(i) = }")  # noqa T201
