
rivers = {
    'Ganga': 'India',
    'Thames': 'United Kingdom',
    'Amazon': 'Peru',
    'Tigris': 'Turkey',
    }
for river, country in rivers.items():
  print("The " + river.title() + " flows through " + country.title() + ".")  

print('\nThe names of the following rivers are included in the dictionary, are as follows:-')  
for river in rivers.keys():
  print('=' + river.title())  

print('\nThe names of the following countries are included in the dictionary, are as follows:-')
for country in rivers.values():
  print('=' + country.title())  


  