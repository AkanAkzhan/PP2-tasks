import re

text = "abbb a ab abb"
result = re.findall(r"ab*", text)
print(result)