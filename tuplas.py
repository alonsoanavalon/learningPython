nums = [1,2,3,4,5,6,7,8,9]

for n in nums:
    if n % 2 == 0:
        print("{} es par".format(n))
    else:
        print("{} es impar".format(n))





while True:
    for n in nums:
        if n == 3:
            continue
        print(n)
  
    break
