import pytest
from Bowling_Game import BowlingGame

@pytest.fixture
def game():
    return BowlingGame()

# Função auxiliar para rolar múltiplas vezes
def roll_many(game, pins, times):
    for _ in range(times):
        game.roll(pins)

# Função auxiliar para rolar um spare
def roll_spare(game):
    game.roll(5)
    game.roll(5)  # 5 + 5 = spare

# Função auxiliar para rolar um strike
def roll_strike(game):
    game.roll(10)

def test_gutter_game(game):
    roll_many(game, 0, 20)
    assert game.score() == 0

def test_all_ones(game):
    roll_many(game, 1, 20)
    assert game.score() == 20

def test_one_spare(game):
    roll_spare(game)
    game.roll(3)
    roll_many(game, 0, 17)
    assert game.score() == 16

def test_one_strike(game):
    roll_strike(game)
    game.roll(4)
    game.roll(3)
    roll_many(game, 0, 16)
    assert game.score() == 24

def test_perfect_game(game):
    roll_many(game, 10, 12)
    assert game.score() == 300

def test_spare_in_last_frame(game):
    roll_many(game, 0, 18)
    game.roll(7)
    game.roll(3)  # Spare no 10º frame
    game.roll(5)  # Bônus
    assert game.score() == 15

def test_strike_in_last_frame(game):
    roll_many(game, 0, 18)
    game.roll(10)  # Strike no 10º frame
    game.roll(10)
    game.roll(10)
    assert game.score() == 30

def test_two_consecutive_strikes(game):
    roll_strike(game)
    roll_strike(game)
    game.roll(3)
    game.roll(4)
    roll_many(game, 0, 14)
    assert game.score() == 47  # Correto: 23 + 17 + 7

def test_all_spares(game):
    for _ in range(10):
        roll_spare(game)
    game.roll(5)  # Bônus no 10º frame
    assert game.score() == 150  # Correto: 10 spares com bônus de 5


def test_alternate_strikes_and_spares(game):
    # Frame 1: Strike
    roll_strike(game)
    # Frame 2: Spare (5 + 5)
    roll_spare(game)
    # Frame 3: Strike
    roll_strike(game)
    # Frame 4: 4 + 4
    game.roll(4)
    game.roll(4)
    # Rest: tudo 0
    roll_many(game, 0, 12)
    expected_score = (
        10 + 5 + 5 +  # Frame 1
        10 + 10 +     # Frame 2
        10 + 4 + 4 +  # Frame 3
        8             # Frame 4
    )
    assert game.score() == expected_score
