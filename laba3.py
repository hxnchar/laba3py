from math import log
import time
x = float(input("x = "))
if x==0:
    print("Error. We can't devide by 0.")
elif x==-1:
    print("Error. logarithm is not defined.")
else:
    n = 0
    sum1 = 0
    sum2 = 1
    start = time.time()
    finalResult = 0
    while abs(sum1-sum2)>10**(-6):
        n+=1
        sum2 = sum1
        sum1 += ((-1)**(n+1))*((x**(n+1))/n)
        if n%10000==0:
            print(f"Step #{n}: result = {'{0:.7f}'.format(sum1)};")
        tic = time.perf_counter()
        finalResult = int(sum1*1000000)/1000000
    print("-"*50)
    print("Code finished work.")
    print(f"Final result is {finalResult}.")
    print(f"Total steps spended: {n}.")
    print(f"Total time spended: {round((time.time() - start),3)} seconds.")