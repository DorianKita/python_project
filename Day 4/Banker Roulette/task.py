import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# random_name= int(random.random() * len(friends))
# print(friends[random_name])

# print(random.choice(friends))

random_number = random.randint(0, len(friends) -1 )
print(friends[random_number])