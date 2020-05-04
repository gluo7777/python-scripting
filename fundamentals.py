
# Function with return type


def returnObject(num) -> str:
    return str(object=num)


def double(num: int) -> int:
    return num * 2


if __name__ == "__main__":
    print(double(3))
