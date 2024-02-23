import re
"""
nom = "^[A-Z]{1}[a-z]{2,9}$"   #{min,max}
tel = "^(06|07)[0-9]d{8}$"  #d{10}
email1 = "^[a-zA-z]+[a-zA-z0-9_.-]+@[A-Za-z0-9_.-]+[a-z]+\.[a-z]{3}$"
age = "^[0-9]{,3}$"
"""

email = input("Donner votre email :")
regex = "^[a-zA-Z][a-zA-Z0-9_.-]+@[a-zA-Z][a-zA-Z0-9_.-]+\.[a-zA-Z]+$"
if re.search(regex,email):
    print("Valid Email")
else:
    print("Invalid Email")
