print("Hello World")

if __name__=="__main__":
    print("スクリプト実行時に実行されるよ")
a=2

if a%15==0:
    print("FizzBuzz")
elif a%5==0:
    print("Buzz")
elif a%3==0:
    print("Fizz")
else:
    print(a)

for item in [0,1,2,3,4,5]:
    print(item)

for item in range(0,6):
    print(item)

def fibo(n):
    if n == 0 or n == 1: return 1
    return fibo(n - 1) + fibo(n - 2)

