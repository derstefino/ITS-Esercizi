'''Suppose that you need to find the sum of integers from 1 to 10, 20 to 37, and 35 to 49.
Write a Python program that
compute these three different sums.'''

sum_1:int = 0
sum_2:int = 0
sum_3:int = 0

for i in range(1,11):
    sum_1+=i

for i in range(20,38):
    sum_2+=i

for i in range(35,50):
    sum_3+=i

print(sum_1)
print(sum_2)
print(sum_3)

def sumInRange(a:int, b:int):
    result:int = 0
    for i in range(a, b+1):
        result = result + i
    return result

mysum = sumInRange(1,10)

print(mysum)




def subtract(a:int, b:int) -> int:
    result = a-b
    return result


sottrazione = subtract(3,1)

print(sottrazione)

