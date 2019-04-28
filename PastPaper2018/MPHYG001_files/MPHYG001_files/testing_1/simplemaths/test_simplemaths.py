import pytest
from simplemaths.simplemaths import SimpleMaths as sm


class TestSimpleMaths():


    def test_fail_with_non_integer(self):
        with pytest.raises(ValueError) as exception:
            sm(1.5)
        with pytest.raises(ValueError) as exception:
            sm(0.99)
        with pytest.raises(ValueError) as exception:
            sm(-1000.2)


    def test_negative_input_square(self):
        assert sm(-2).square() == 4
        assert sm(-4).square() == 16
        with pytest.raises(ValueError) as exception:
            sm(1.5).square()


    def test_positive_input_square(self):
        assert sm(2).square() == 4
        assert sm(4).square() == 16


    def test_factorial(self):
        assert sm(3).factorial() == 6
        assert sm(4).factorial() == 24


    def test_power(self):
        assert sm(2).power(8) == 256
        assert sm(-3).power(2) == 9
        assert sm(2).power(-2) == 0.25


    def test_power_default(self):
        assert sm(2).power() == 8
        assert sm(-4).power() == -64


    def test_odd(self):
        assert sm(1).odd_or_even() == 'Odd'
        assert sm(-5).odd_or_even() == 'Odd'


    def test_even(self):
        assert sm(4).odd_or_even() == 'Even'
        assert sm(0).odd_or_even() == 'Even'
        assert sm(-2).odd_or_even() == 'Even'
    
    
    def test_square_root(self):
        assert sm(4).square_root() == 2


