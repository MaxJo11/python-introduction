from src import *

def test_shitty_player() :
    assert jeu("-- -- -- -- -- -- -- -- -- --") == 0

def test_bowling() :
    assert jeu("11 11 11 11 11 11 11 11 11 11") == 20

def test_bowling_2() :
    assert jeu("9- 23 -1 47 22 71 -- 45 71 42 ") == 61

def test_bowling_3() :
    assert jeu("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/") == 150

def test_bowling_4() :
    assert jeu ("0/ 1/ 2/ 3/ 4/ 5/ 0/ 1/ 2/ 3/") == 125
