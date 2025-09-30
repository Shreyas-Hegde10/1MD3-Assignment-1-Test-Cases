import pytest
from assignment1 import is_valid_number, is_valid_term,approx_equal, degree_of, get_coefficient

@pytest.mark.parametrize("num, expected", [
    # Valid integers
    ("0", True),
    ("10", True),
    ("-124", True),
    ("999999", True),

    #Valid decimals
    ("12.9", True),
    ("-2.3", True),
    ("0.0", True),
    ("-0.75", True),

    # invalid: multiple dots
    ("12.9.0", False),
    ("1.2.3", False),

    # Invalid: misplaced or multiple '-'
    ("-", False),
    ("2-24", False),
    ("-2-24", False),
    ("--5", False),

    # Invalid: non-digit characters
    ("abc", False),
    ("12a3", False),

    # Edge cases with decimal placement
    (".", False),
    ("5.", True),
    (".5", True),
    ("-.3", True),

    # Empty string
    ("", False),

    # Edge cases with spacing 
    (" 123", False), 
])

def test_is_valid_number(num, expected): 
    assert is_valid_number(num) == expected 

@pytest.mark.parametrize("term, expected", [
    # Valid terms: integers and floats with x
    ("44.4x^6", True),
    ("-7x", True),
    ("9.9", True),
    ("x^3", False),
    ("x", False),
    ("0x^0", False),
    ("123", True),
    ("-0.5x^2", True),
    ("-x^1", False),
    ("5x^0", False),

    # Invalid variable or format
    ("7y**8", False),
    ("7*x^8", False),
    ("7x^8.8", False),
    ("7*x^8.8", False),
    ("7x^ 8.8", False),
    ("x^-3", False),
    ("x^", False),

    # Malformed coefficients
    ("--3x^2", False),
    ("3.4.5x", False),
    ("3x^^2", False),
    ("3xx^2", False),

    # Edge cases
    ("0", True),
    ("-0", True),
    ("x0", False),
    ("", False),
])

def test_is_valid_term(term, expected): 
    assert is_valid_term(term) == expected 

@pytest.mark.parametrize("x, y, tol, expected", [
    # Exact matches
    (5, 5, 0, True),
    (0, 0, 0, True),

    # Within tolerance
    (5, 4, 1, True),
    (0.999, 1, 0.0011, True),
    (-1, -1.1, 0.1, True),
    (100.0, 100.01, 0.01, True),

    # Outside tolerance
    (5, 3, 1, False),
    (0.999, 1, 0.0001, False),
    (-1, -1.2, 0.1, False),
    (100.0, 100.02, 0.01, False),
])
def test_approx_equal(x, y, tol, expected):
    assert approx_equal(x, y, tol) == expected

@pytest.mark.parametrize("term, expected", [
    # Numbers only
    ("252.192", 0),
    ("0", 0),
    ("-2", 0),
    ("123.456", 0),
    ("-0.001", 0),

    # Variable without exponent
    ("x", 1),
    ("-x", 1),
    ("3x", 1),
    ("-1.5x", 1),
    ("0x", 1),

    # Variable with exponent
    ("x^3", 3),
    ("-x^1", 1),
    ("55x^6", 6),
    ("7x^0", 0),
    ("-0.5x^10", 10),
    ("123.45x^2", 2),

    # Edge cases
    ("x^999", 999),
    ("-x^999", 999),
])
def test_degree_of(term, expected):
    assert degree_of(term) == expected

@pytest.mark.parametrize("term, expected", [
    # Numbers only
    ("252.192", 252.192),
    ("0", 0.0),
    ("-2", -2.0),
    ("123.456", 123.456),
    ("-0.001", -0.001),

    # Variable without exponent
    ("3x", 3.0),
    ("-1.5x", -1.5),
    ("0x", 0.0),

    # Variable with exponent
    ("55x^6", 55.0),
    ("7x^0", 7.0),
    ("-0.5x^10", -0.5),
    ("123.45x^2", 123.45),
])
def test_get_coefficient(term, expected):
    assert get_coefficient(term) == expected