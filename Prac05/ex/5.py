text = "a123b axxb a---b ab"
result = re.findall(r"a.*b", text)
print(result)