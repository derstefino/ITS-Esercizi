'''5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th",
and each result should be on a separate line.
'''

list_n:list[int] = []  

for n in range(1,10):
    list_n.append(n)

for n in list_n:
    if n==1:
        print("\n1st\n\n")
    elif n==2:
        print("\n2nd")
    elif n==3:
        print("\n3rd")
    else:
        print(f"\n{n}th")


