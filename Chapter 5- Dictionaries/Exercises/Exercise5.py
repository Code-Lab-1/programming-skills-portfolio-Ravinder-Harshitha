pets = []
pet = {
    'Animal type': 'Bird',
    'Name': 'Johnny',
    'Owner': 'Robert',
    'Weight': 43,
    'Eats': 'seeds',
}
pets.append(pet)

pet = {
    'Animal type': 'Goldfish',
    'Name': 'Goldie',
    'Owner': 'Lolita',
    'Weight': 0.02,
    'Eats': 'fish food',
}
pets.append(pet)

pet = {
    'Animal type': 'Dog',
    'Name': 'Rambo',
    'Owner': 'Ronnie',
    'Weight': 37,
    'Eats': 'Dog food',
}
pets.append(pet)

for pet in pets:
    print(f"\nInformation I have about {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")



