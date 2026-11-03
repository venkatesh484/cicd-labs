import pytest
from app import disk_usage_status


def test_ok():
    assert disk_usage_status(10, 100) == "OK"


def test_warning():
    assert disk_usage_status(80, 100) == "WARNING"


def test_critical():
    assert disk_usage_status(95, 100) == "CRITICAL"


def test_invalid_total():
    with pytest.raises(ValueError):
        disk_usage_status(10, 0)
