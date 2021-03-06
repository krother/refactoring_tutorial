import io
import pytest

from space_game import travel


# the actual solution to the game
SOLUTION = [
    "2",
    "2",  # go to sirius and win quiz
    "1",
    "1",
    "yes",  # go to centauri and buy GPU drive
    "2",
    "yes",  # hire copilot on orion
    "2",
    "3",
    "yes",  # jump into black hole
    "42",
    "1",  # get crystal
]

DIE_BY_BLACK_HOLE = [
    "2",
    "2",  # go to sirius and win quiz
    "1",
    "1",
    "yes",  # go to centauri and buy GPU drive
    "2",
    "no",  # hire copilot on orion
    "2",
    "3",
    "yes",  # jump into black hole
]

# text sniplets that should appear literally in the output
PHRASES = [
    "The stars are waiting for you",
    "Betelgeuse",
    "credits",
    "tech-savvy copilot",
    "buy",
    "Do you want to hire them",
    "Black Hole",
    "stupid idea",
    "Return to your people in peace",
    "THE END",
]


@pytest.fixture
def solution_input():
    """helper function to hijack the keyboard for testing"""
    return io.StringIO("\n".join(SOLUTION))


def test_travel(monkeypatch, solution_input):
    """game finishes"""
    monkeypatch.setattr("sys.stdin", solution_input)
    travel()


def test_output(monkeypatch, capsys, solution_input):
    """text output is not empty"""
    monkeypatch.setattr("sys.stdin", solution_input)

    travel()

    captured = capsys.readouterr()
    assert len(captured.out) > 0


def test_die(monkeypatch, capsys):
    """player dies"""
    monkeypatch.setattr("sys.stdin", io.StringIO("\n".join(DIE_BY_BLACK_HOLE)))

    travel()

    captured = capsys.readouterr()
    assert "crunches" in captured.out


@pytest.mark.parametrize("phrase", PHRASES)
def test_output_phrases(monkeypatch, capsys, solution_input, phrase):
    """check for some key phrases in the output"""
    monkeypatch.setattr("sys.stdin", solution_input)

    travel()

    captured = capsys.readouterr()
    assert phrase in captured.out
