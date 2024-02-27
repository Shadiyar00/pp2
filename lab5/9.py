import re


text = input()


formatted_text = re.sub(r'(?<=[a-z])([A-Z])', r' \1', text)

print(formatted_text)
