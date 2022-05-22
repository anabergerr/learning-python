# guest list
from operator import ge


guest_list = ["Jhon", "Ana", "Gabriel", "Carol", "Jake"]
message = "you were invited "
message_cancellation = "guest canceled: "

for guest in guest_list:
    print(message + guest)
print(message_cancellation + guest_list[0])
guest_list.remove("Jhon")
print(guest_list)
guest_list.insert(0, "Renata")
print(guest_list)

# invited new list guest

for guest in guest_list:
    print(message + guest)

# add + 3 invited
news_guests = ["Vitoria", "Sabrina", "Fernanda"]

for guest in news_guests:
    guest_list.append(guest)

for guest in guest_list:
    print(message + guest)

print(guest_list)

# deixando apenas dois convidados

value = len(guest_list)
# for guest in guest_list:

for guest in range(value):
    guest_deleted = guest_list.pop()
    print("Sorry " + guest_deleted)
    if(len(guest_list) == 2):
        break


print(guest_list)
