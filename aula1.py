# math operations

add = 3 + 5

# print(add)

sub = 10 - 2

# print(sub)

div = 16 / 2

# print(div)

mult = 4 * 2

# print(mult)

# Number birthday

fav_number = 13

message = "Happy " + str(fav_number) + "rd Birthday"

# print(message)

# create list

names_friends = ["Bob", "John", "Ana"]

# acess items

# print(names_friends[0])

message_friends = "Hellou " + names_friends[2]

# print(message_friends)

names_friends[0] = "Pedro"

# print(names_friends[0])

names_friends.append("Bruna")

names_friends.insert(3, "Carlos")

del names_friends[3]

names_friends.pop()

# print(names_friends)

# pop()

list_original = ["Bob", "John", "Ana"]
# acess item removed
list_modified = list_original.pop()

# print(list_modified)
# print(list_original)

# remove()

remove_item_lists = list_original.remove("Bob")

print(remove_item_lists)
print(list_original)
