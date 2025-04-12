'''4-10. Slices: Using one of the programs you wrote in this chapter,
add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:.
Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. 
Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. 
Then use a slice to print the last three items in the list.'''

list:list = [] 

for n in range(3,31,3):
    list.append(n)

slice = list[:2]

print("the first three items in the list are:")

print(list[:3])

print("three items from the middle of the list are:")

print(list[4:7])

print("the last three items in the list are:")

print(list[7:10])
