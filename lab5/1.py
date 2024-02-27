import re
text = input()
pattern = r'ab*'

matches = re.findall(pattern, text)

for match in matches:
    print(match)

