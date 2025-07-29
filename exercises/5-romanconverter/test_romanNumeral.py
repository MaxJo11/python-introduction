from src import *

def test_1_should_return_1() :
    assert jn(1) == 'I'

def test_2_should_return_2() :
    assert jn(2) == 'II'

def test_3_should_return_3() :
    assert jn(3) == 'III'

def test_4_should_return_4() :
    assert jn(4) == 'IV'

def test_5_should_return_5() :
    assert jn(5) == 'V'

def test_6_should_return_6() :
    assert jn(10) == 'X'

def test_7_should_return_7() :
    assert jn(900) == 'CM'

def test_8_should_return_8() :
    assert jn(1000) == 'M'

def test_9_should_return_9() :
    assert jn(445) == 'CDXLV'


