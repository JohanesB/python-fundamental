# PART 1
text = "The agent's phone number is 408-555-1234. Call Soon!"

import re
pattern = "phone"

match = re.search(pattern, text)
print(match)
print(match.span())
print(match.start())
print(match.end())

# PART 2

text = "My phone number is 408-555-1234"
phone = re.search('408-555-1234', text)
print(phone)

phone = re.search("\d{3}\W\d{3}-\d{4}", text)
print(phone)
print(phone.group())