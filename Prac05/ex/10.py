def camel_to_snake(s):
    return re.sub(r"([A-Z])", r"_\1", s).lower().strip("_")

print(camel_to_snake("helloWorldTest"))