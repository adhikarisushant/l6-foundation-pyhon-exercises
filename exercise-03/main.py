import random2 as random

for i in range(3):
    print(random.random())
    print(random.randint(1,10))



members = ["ram", "shyam", "hari", "guru"]
leader = random.choice(members)
print(leader)