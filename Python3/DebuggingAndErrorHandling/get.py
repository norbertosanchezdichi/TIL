def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

d = {"name": "Ricky"}
print(get(d, "city"))