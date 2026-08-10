# Get Grandchildren

Source: HackerRank Style Unit 5 Assessment, Version A

## Question

The following Person class defines a person with a last name, first name, and list of children. Each child in
the list of children is an instance of Person.
The method add_child() adds a child to a person's list of children.
Add a method to the Person class called get_grandchildren() that returns a list of the person's
grandchildren.

Example 1:
# johndoe = Person("John", "Doe")
# janedoe = Person("Jane", "Doe")
# jimmydoe = Person("Jimmy", "Doe")
# johndoe.add_child(janedoe)
# janedoe.add_child(jimmydoe)

# johndoe.get_grandchildren()
Output: # [jimmydoe]
Example 2:
# johndoe = Person("John", "Doe")
# janedoe = Person("Jane", "Doe")
# johndoe.add_child(janedoe)
# johndoe.get_grandchildren()
Output: # []
