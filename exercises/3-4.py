# guest list
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