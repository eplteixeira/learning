
def summultiple(n):
    numbers = []
    for i in range(1,n):
        if (i % 3) == 0 or (i % 5) == 0 or (i % 7) == 0:
            numbers.append(i)
    
    print("NUMBERS ", numbers)
    
    total = 0
    for num in numbers:
        total += num
        
    print("TOTAL ", total)
