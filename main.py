#DESCRIPTION:
#Email-Slicer: A program that extracts the username and domain from an email.

#DETAILS:
#The user will be asked to his/her email address.
#The program returns the username and domain

#CODE:
lst = list(map(str, input("Enter E-Mail ID/s separated by commas: ").split(",")))

for a in lst:
    username = a[:a.index('@')]
    domain = a[a.index('@') + 1:]
    print(f"{a} --> username: {username} , domain: {domain}")
