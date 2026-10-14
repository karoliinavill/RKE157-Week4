#meie ülesanne on luua lihtne vorm kasutaja andmete kontrollimiseks – nimelt kasutajanime ja parooli kontroll.

username = input("Enter username: ")
password = input("Enter password: ")

#classical if else
""" 
if username == "user":
    if password == "1234":
        print("Welcome!")
    else:
        print("Access denied.")
else:
    print("Access denied.") 
"""

#and operator
""" 
if username == "user" and password == "1234":
    print("Welcome!")
else:
    print("Access denied.") 
 """

#or operator
if username != "user" or password != "1234":
    print("Access denied.")
else:
    print("Welcome!")