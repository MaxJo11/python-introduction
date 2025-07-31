from src import *

def test_shitty_player() :
    assert jeu("-- -- -- -- -- -- -- -- -- --") == 0

def test_bowling() :
    assert jeu("11 11 11 11 11 11 11 11 11 11") == 20

def test_bowling_2() :
    assert jeu("9- 23 -1 47 22 71 -- 45 71 42 ") == 61
