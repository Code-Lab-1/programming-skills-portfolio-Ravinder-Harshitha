
def biggest_number(a,b,c):
  if a >= b and a >= c: 
    print("The biggest number from the above numbers is: " + str(a)) 
  elif b >= a and b >= c:
    print("The biggest number from the above numbers is: " + str(b))
  else:
    print("The biggest number from the above numbers is: " + str(c))

biggest_number(42,27,39)

