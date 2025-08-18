def NULL_not_found(obj: any) -> int:
    if obj is None:
        print(f"Nothing: {obj} {type(obj)}")
        return 0
    elif isinstance(obj, float) and obj != obj:
        print(f"Cheese: {obj} {type(obj)}")
        return 0
    elif obj == 0 and type(obj) == int:
        print(f"Zero: {obj} {type(obj)}")
        return 0
    elif obj == "" and type(obj) == str:
        print(f"Empty: {type(obj)}")
        return 0
    elif obj is False and type(obj) == bool:
        print(f"Fake: {obj} {type(obj)}")
        return 0
    else:
        print("Type not Found")
        return 1