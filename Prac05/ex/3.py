text = "hello_world test_var a_b_c"
result = re.findall(r"[a-z]+_[a-z]+", text)
print(result)