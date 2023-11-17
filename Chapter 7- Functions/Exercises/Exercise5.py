
def describe_city(city, country = 'India'):
  msg = city.title() + " is in " + country.title() + "."
  print(msg)

describe_city('New Delhi')
describe_city('Mumbai')  
describe_city('Venice', 'Italy')
describe_city('Paris', 'France')  



