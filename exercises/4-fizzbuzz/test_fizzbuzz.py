from src import fizzbuzz



def test_1_should_return_1():
    assert fizzbuzz(1) == '1'

def test_2_should_return_2():
    assert fizzbuzz(2) == '2'

def test_3_should_return_3():
    assert fizzbuzz(3) == 'Fizz'

def test_4_should_return_4():
    assert fizzbuzz(5) == 'Buzz'

def test_5_should_return_5() :
    assert fizzbuzz(15) == 'FizzBuzz'
