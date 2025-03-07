'''5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py.

Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

list = ["gabagool"]

one = 1
two = 2

jamaica = "Jamaica"

print("gabagool" in list)
print("hello" in list)
print("hello" in list and "gabagool" in list)
print("hello" in list or "gabagool" in list)

print(one < two)

print(jamaica == jamaica.lower())