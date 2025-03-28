
def recursiveCountdown(n:int) -> None:
    
    if n<0:
        print("Error!")
    elif n==0:
        print(0)
    else:
        
        print(n)
        
        recursiveCountdown(n-1)





def recursiveSum(n:int) -> int:

    if n<0:
        print("Error!")
        return 0
    
    elif n==0:
        return 0
    
    else:
        sum = n + recursiveSum(n-1)
        return sum
    

def sumInRange(a:int, b:int) -> int:
# if a > b, swap values of a and b
    if a > b:
# define a temporary variable called temp, containing value of a
        temp:int = a
# swap values of a and b
        a = b
        b = temp # now b = a
# define a sum
    sum:int = 0
# compute sum until b = a
    while b>=a:
        sum = sum + b
        b = b -1
# return sum
    return int(sum)




# sum in range ricorsiva

def sumInRange(a:int, b:int) -> int:

    if a > b:
        temp:int = a
        a = b
        b = temp

    sum:int = 0

    if a == b:
       sum += a
       return sum
    else:
        sum += a + sumInRange(a+1, b)
        return sum


print(sumInRange(10,100))