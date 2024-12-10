# game of banker roulette

import random

friends = ['Arjun', 'Bimal', 'Bijay', 'Manish', 'Pasnuri', 'Pallavi', 'Nima', 'Nura', 'Bhagwati']

count_random_choice = {
    friend: 0 for friend in friends
}
for i in range(900):
    #value_of_key = friends[random.randint(0, len(friends)-1)]
    value_of_key = random.choice(friends)
    if value_of_key in count_random_choice:
        count_random_choice[value_of_key] += 1      #it may seem like the key should be incremented, but when dict[key] is input, we are looking up the value for that key
    
print(count_random_choice)


#print(f"\nToday's bill will be paid by: {friends[random.randint(1, len(friends))]}\n")
# print(f"\nToday's bill will be paid by: {random.choice(friends)}\n")

