def fizzbuzz(number: int) -> str:
    if number % 3 == 0 and number % 5 == 0 :
        return "FizzBuzz"
    elif number % 3 == 0 or "3" in str(number) :
        return "Fizz"
    elif number % 5 == 0 or "5" in str(number) :
        return "Buzz"
    return str(number)

def fizzbuzz2 ():
    for i in range(1,101) :
        print(fizzbuzz(i))