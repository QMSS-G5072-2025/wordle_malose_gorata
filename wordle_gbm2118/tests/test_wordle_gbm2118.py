import wordle_gbm2118
import pytest
from wordle_gbm2118 import (
    validate_guess,
    check_guess
)
# Word list for testing
WORD_LIST = [
    "crane", "apple", "hello", "world", "python", 
    "house", "water", "light", "music", "dream",
    "happy", "smile", "peace", "heart", "brain",
    "table", "chair", "phone", "paper", "green"
]


# =============================================================================
# PART 1: BASIC TESTING
# =============================================================================
# Note: Each test function can contain multiple related assertions.
# This is standard practice - you're testing the same function with different
# inputs to verify it handles various scenarios correctly.

def test_validate_guess():
    """
    Test the validate_guess function with various inputs.
    
    Implement this test function with:
    - Valid guesses (correct length, lowercase, alphabetic)
    - Invalid guesses (wrong length, uppercase, non-alphabetic)
    - Edge cases (empty string, None, non-string inputs)
    """
    # Valid guess
    result_1 = validate_guess("prays")
    expected_1 = True
    assert result_1 == expected_1
    
    # Contains uppercase
    result_2 = validate_guess("Prays")
    expected_2 = False
    assert result_2 == expected_2
    
    # Wrong length
    result_3 = validate_guess("prayers")
    expected_3 = False
    assert result_3 == expected_3
    
    # Non-alphabetic
    result_4 = validate_guess("12345")
    expected_4 = False
    assert result_4 == expected_4
    
    # Edge case: empty string
    result_5 = validate_guess("")
    expected_5 = False
    assert result_5 == expected_5
    
    # Edge case: None
    result_6 = validate_guess(None)
    expected_6 = False
    assert result_6 == expected_6
    
    # Edge case: non-string input
    result_7 = validate_guess(12345)
    expected_7 = False
    assert result_7 == expected_7


def test_check_guess_basic():
    """
    Test basic check_guess functionality.
    
    Implement this test function with:
    - Perfect match (all green)
    - No matches (all gray)
    - Mixed results (green, yellow, gray combinations)
    - Edge cases (different lengths)
    
    """
    # Test wih perfect match
    result_1 = check_guess("water", "water")
    expected_1 = [('w', 'green'), ('a', 'green'), ('t', 'green'), ('e', 'green'), ('r', 'green')]
    assert result_1 == expected_1
    
    # Test with no match
    result_2 = check_guess("water", "pluck")
    expected_2 = [('p', 'gray'), ('l', 'gray'), ('u', 'gray'), ('c', 'gray'), ('k', 'gray')]
    assert result_2 == expected_2
    
    # Test with mixed results
    result_3 = check_guess("water", "waste")
    expected_3 = [('w', 'green'), ('a', 'green'), ('s', 'gray'), ('t', 'yellow'), ('e', 'yellow')]
    assert result_3 == expected_3
    
    # Test with edge case with different length
    result_4 = check_guess("water", "waters")
    expected_4 = []
    assert result_4 == expected_4
