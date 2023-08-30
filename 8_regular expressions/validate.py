import re
email = input("what's your email?").strip()
username, domain = email.split('@')

if username and ('.' in domain):
    print("valid")
else:
    print("inavlid")


print(re.findall(r"^[A-Za-z1-9_]+@[A-Za-z1-9_]+\.com$", email))
print(re.findall(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE))