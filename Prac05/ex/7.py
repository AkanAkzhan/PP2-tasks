def snake_to_camel(s):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s)

print(snake_to_camel("hello_world_test"))