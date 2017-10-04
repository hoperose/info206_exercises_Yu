import re

your_pattern = r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
email_regex = re.compile(r"[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
emails = ["joesmith@excite.com", "pythonista@python.org", "wha.t.`1an?ug{}ly@email.com"]

for email in emails:
    if not email_regex.match(email):
        print("%s is not a valid email address" % (email))
    elif not your_pattern:
        print("Please enter a pattern to match: ")
    else:
        print("Pass")


        

