import re

claim = 'People love Python.'

print(re.search(r'Python', claim).group())
# => Python

print(re.match(r'Python', claim))
# => None

print(re.search(r'People', claim).group())
# => People

print(re.match(r'People', claim).group())
# => People