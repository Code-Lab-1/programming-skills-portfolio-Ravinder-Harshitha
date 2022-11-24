
sandwich_orders = ['chicken sandwich', 'pastrami', 'roast beef sandwich', 'grilled cheese', 'ham sandwich']
finished_sandwiches = []

while sandwich_orders:
  current_sandwich = sandwich_orders.pop()
  print("I am preparing your " + current_sandwich + " sandwich." )
  finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
  print("I made your " + sandwich + " sandwich.")

