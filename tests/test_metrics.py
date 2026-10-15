import pytest

from toyapp.metrics import units_per_hour


def test_units_per_hour_basic():
    assert units_per_hour(120, 2) == 60


def test_negative_inputs_rejected():
    with pytest.raises(ValueError):
        units_per_hour(-1, 2)
