import re

patern = r"\d{11}"

def task(text):
    return re.findall(patern, text)

print(task("My phone numbers are 12345678901 and 10987654321 and 12345678910 not 123123 or 1231221"))