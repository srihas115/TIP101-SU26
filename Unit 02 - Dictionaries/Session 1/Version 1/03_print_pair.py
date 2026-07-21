def print_pair(dictionary, target):
    if target in dictionary:
        print(f"Key: {target}")
        print(f"Value: {dictionary[target]}")
    else:
        print("That pair does not exist!")

dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
