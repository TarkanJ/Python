import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("0/1") == 0

def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):  # Test na ddělení nulou
        convert("1/0")

def test_convert_invalid_format():
    with pytest.raises(ValueError):  # Neplatný formát zlomku
        convert("three/four")
    with pytest.raises(ValueError):  # Nesprávný formát zlomku
        convert("5/4")

def test_gauge():
    assert gauge(99) == "F"   # Hodnota 99 by měla vrátit "F"
    assert gauge(100) == "F"  # Hodnota 100 by měla vrátit "F"
    assert gauge(1) == "E"    # Hodnota 1 by měla vrátit "E"
    assert gauge(0) == "E"    # Hodnota 0 by měla vrátit "E"
    assert gauge(50) == "50%" # Střední hodnota vrátí procento s %
