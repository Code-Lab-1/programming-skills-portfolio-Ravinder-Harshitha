guests = ["APJ Abdul Kalam","Swami Vivekananda","Nicola Tesla"]

invite = ("Greetings! " + guests[0]+" , please join us for dinner.")
print(invite)
invite = ("Greetings! " + guests[1]+" , please join us for dinner.")
print(invite)
invite = ("Greetings! " + guests[2]+" , please join us for dinner.")
print(invite)

name = guests[2]
print("\nSorry, "+guests[2]+" will not be able to make it to the dinner")

del(guests[2])
guests.insert(2, "Elon Musk")

invite = ("\nGreetings! " + guests[0]+" , please join us for dinner.")
print(invite)
invite = ("Greetings! " + guests[1]+" , please join us for dinner.")
print(invite)
invite = ("Greetings! " + guests[2]+" , please join us for dinner.")
print(invite)

print("\nSorry, we can only invite two people for dinner.")

print("\nSorry, "+ guests[2] + " there's no room at the table.")
name = guests.pop()

invite = ("\nGreetings! " + guests[0]+" ,please join us for dinner.")
print(invite)
invite = ("Greetings! " + guests[1]+" , please join us for dinner.")
print(invite)


del(guests[0])
del(guests[0])
print(guests)