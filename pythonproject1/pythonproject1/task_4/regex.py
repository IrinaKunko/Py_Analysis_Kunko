import re

result = re.match(r'\d{2}', '123 - no string')
not_result = re.match(r'\d{2}', 'string')
print(result.group())
print(not_result)

result = re.search(r'\d{2}', 'string, 123 - no string')
print(result.group())

result = re.findall(r'\d{2}', '12 string, 34 - no string 56')
print(result)

result = re.fullmatch(r'\d{3}', '123')
not_result = re.fullmatch(r'\d{3}', '123 - no string')
print(result.group())
print(not_result)

def check(s):
    return bool(re.fullmatch(r'\w+@\w+\.\w+', s))


print(check('aaa@afds.dasf'))