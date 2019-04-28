import pytest
from simplemaths.simplemaths import SimpleMaths as sm
import yaml
import os


#try with fixtures file

def read_fixture():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures.yml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
    return fixtures


@pytest.mark.parametrize("fixture", read_fixture())
def test_negative_input_square(fixture):
    answer = fixture.pop('answer')
    assert sm(**fixture).square() == answer
        
    with pytest.raises(ValueError) as exception:
        sm(1.5).square()



def test_fail_with_non_integer():
    with pytest.raises(ValueError) as exception:
        sm(1.5)
    with pytest.raises(ValueError) as exception:
        sm(0.99)
    with pytest.raises(ValueError) as exception:
        sm(-1000.2)
