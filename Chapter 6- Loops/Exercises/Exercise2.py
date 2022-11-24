
prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are done. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You can get in for free!")
    elif age < 13:
        print(" The price of your ticket is $10.")
    else:
        print(" The price of your ticket is $15.")

        