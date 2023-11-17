from lab1 import calculate


class TestNoRoots():
    def test_one(self):
        assert calculate(0, 0, 2) == "Решений нет"

    def test_two(self):
        assert calculate(123, 24.5, 314) == "Решений нет"


def test_x_any():
    assert calculate(0, 0, 0) == "X - любое число"


def test_two_roots():
    assert calculate(1.2, 5.5, 6) == "x1 = -1.7899335592169874\nx2 = -2.793399774116346"


class TestOneRoot:
    def test_one(self):
        assert calculate(0, 10, 5) == "x = -0.5"

    def test_two(self):
        assert calculate(1, 2, 1) == "x = -1.0"
