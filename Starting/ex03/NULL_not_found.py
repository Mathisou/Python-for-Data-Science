def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
        return 0
    elif isinstance(obj, float):
        print(f"Cheese: {obj} {type(obj)}")
        return 0
    elif obj == 0 and isinstance(obj, int):
        print(f"Zero: {obj} {type(obj)}")
        return 0
    elif obj == "" and isinstance(obj, str):
        print(f"Empty: {type(obj)}")
        return 0
    elif obj is False and isinstance(obj, bool):
        print(f"Fake: {obj} {type(obj)}")
        return 0
    else:
        print("Type not Found")
        return 1
