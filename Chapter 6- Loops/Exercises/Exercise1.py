
prompt = "\nWhich topping do you prefer on your pizza?"
prompt+= "\n Enter'quit'when you are done:- "

while True:
  topping = input(prompt)
  if topping != "quit":
    print(topping + " topping will be added to your pizza" )
  else:
     break 

    