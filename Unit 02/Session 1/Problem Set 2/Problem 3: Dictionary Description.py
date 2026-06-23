def get_description(info, keys):
    for key in keys:
        print(info[key])

info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)
