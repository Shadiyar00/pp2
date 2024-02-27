import re
word = input()
swith = re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()
print(swith)