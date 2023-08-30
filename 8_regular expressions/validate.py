import re
#email = input("what's your email?").strip()
email = "divyagandreti1997@gmail.com"



username, domain = email.split('@')

# if username and ('.' in domain):
#     print("valid")
# else:
#     print("inavlid")

#if re.search(r"^[A-Za-z1-9]+@.+\.com$", email):
print(re.findall(r"^[A-Za-z1-9_]+@[A-Za-z1-9_]+\.com$", email))
print(re.findall(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE))