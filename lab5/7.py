import re

snake = input()

camel = re.sub(r'(?:_)([a-zA-Z])', lambda x: x.group(1).upper(), snake)

print(camel)

