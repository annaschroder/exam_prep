import yaml
import os
import pytest
from ..laboratory import Laboratory


def read_fixture():
    with open(os.path.join(os.path.dirname(__file__),
                           'fixtures.yml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)
    return fixtures


@pytest.mark.parametrize("fixture", read_fixture())
def test_laboratory(fixture):
    answer = fixture.pop('answer')
    assert Laboratory(**fixture).run_full_experiment(**fixture) == answer


def three_shelves():
    shelf1 = ["A", "antiB", "C"]
    shelf2 = ["antiC", "antiA"]
    shelf3 = ["A"]
    return Laboratory(shelf1, shelf2, shelf3,
                      False).run_full_experiment(shelf1, shelf2, shelf3, False)


def test_three_shelves():
    with pytest.raises(TypeError):
        three_shelves()


def one_shelf():
    shelf1 = ["A", "antiB", "C"]
    return Laboratory(shelf1, False).run_full_experiment(shelf1, False)


def test_one_shelf():
    with pytest.raises(TypeError):
        one_shelf()
