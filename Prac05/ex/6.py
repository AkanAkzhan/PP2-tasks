text = "Hello, world. Test string"
result = re.sub(r"[ ,\.]", ":", text)
print(result)