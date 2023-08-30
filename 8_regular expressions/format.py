import re

name = input("what is your name?").strip()

# if input is lastname, firtsname format


if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
    print(f"hello, {name}")

#regex solution
if (matches := re.search("^(.+), *(.+)$", name)):

    last = matches.group(2)
    first = matches.group(1)
    name = f"{first} {last}"
    print(f"hello, {name}")


