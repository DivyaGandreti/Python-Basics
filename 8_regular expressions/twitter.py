#https://twitter.com/hellokitty
import re

url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "")
print(username)

# Syntax: re.sub(pattern, repl, string, count =0, flag =0)

username = re.sub("^(http(s)?://)?(www\.)?twitter\.com/", "", url)
print(username)


if matches:= re.search(r"^http(?:s)?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url):
    print(matches.group(1))



