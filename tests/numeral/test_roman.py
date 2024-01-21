"""test cases for Roman numerals"""

#standard library


# 3rd perty library
import pytest

# project library
from numeral.roman import to_roman


def test_calling_funtions():
    """call a romam numeral funtion."""
    
@pytest.mark.parametrize(
    "arabic_num, roman_num",
    [
        (1, "I"),
        (5, "V"),
        
        (2, "II"),
        (3, "III"),
        (6, "VI"),
        
        (4,"IV"),
        (9, "IX")
    ]
)
def test_to_roman(arabic_num, roman_num):
    """convert arabic to roman"""
    # Arrange
    
    # Act
    result = to_roman(arabic_num)
        
    # Assert
    assert result == roman_num