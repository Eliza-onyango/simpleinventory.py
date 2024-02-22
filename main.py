# a program to enable user add names, sort and count
names = []

while True:
    name = input("Enter a name (or 'quit' to stop): ")

    if name.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'

    names.append(name)  # Add the entered name to the list
    names.sort()
print("You entered the following names:")
print(len(names))
for name in names:
    print(name)



