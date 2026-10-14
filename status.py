""" 
Kirjuta Pythoni programm, mis kontrollib kliendi staatust tema kulutuste põhjal.
Tingimused:
- Kui klient on kulutanud vähemalt 5000 €, siis tema staatus on Platinum.
- Kui klient on kulutanud vähemalt 1000 €, siis staatus on Gold.
- Kui klient on kulutanud vähemalt 500 €, siis staatus on Silver.
- Kui klient on kulutanud vähemalt 100 €, siis staatus on Bronze.
- Kui vähem kui 100 €, siis on ta Tavaline klient. 
"""

spent = int(input("How much have you spent at our store? "))

#classical if else
""" 
if spent >= 5000:
    print("Your status is Platinum.")
elif spent >= 1000:
    print("Your status is Gold.")
elif spent >= 500:
    print("Your status is Silver.")
elif spent >= 100:
    print("Your status is Bronze.")
else:
    print("You are a regular customer.") 
"""

#and operator (not ideal)
if spent < 100:
    print("You are a regular customer.")
elif spent >= 100 and spent < 500:
    print("Your status is Bronze.")
elif spent >= 500 and spent < 1000:
    print("Your status is Silver.")
elif spent >= 1000 and spent < 5000:
    print("Your status is Gold.")  
else:
    print("Your status is Platinum.")