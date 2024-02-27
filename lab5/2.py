import re
text = input()

pattern = r'ab{2,3}'

matches = re.findall(pattern, text)

for match in matches:
    print(match)

