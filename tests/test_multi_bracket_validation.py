from data_structures_and_algorithm.challenge.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation
# import pytest
# @pytest.fixture
# def input:


def test_multi_bracket_validation_curly():
    expected = True
    actual = multi_bracket_validation("{}")
    assert actual == expected

def test_multi_bracket_validation_parenthes():
    expected = True
    actual = multi_bracket_validation("()")
    assert actual == expected

def test_multi_bracket_validation_brackets():
    expected = True
    actual = multi_bracket_validation("[]")
    assert actual == expected

def test_multi_bracket_validation_Curly_with_parenthes():
    expected = True
    actual = multi_bracket_validation("{}(){}")
    assert actual == expected

def test_multi_bracket_validation_curly_with_double_brackets():
    expected = True
    actual = multi_bracket_validation("(){}[[]]")
    assert actual == expected

def test_multi_bracket_validation_brackets_with_string():
    expected = True 
    actual = multi_bracket_validation("{}{Code}[Fellows](())")
    assert actual == expected

def test_multi_bracket_validation_all():
    expected = True
    actual = multi_bracket_validation("(){}[[]]")
    assert actual == expected

def test_multi_bracket_validation_missing_one_bracket():
    expected = False 
    actual = multi_bracket_validation("(](")
    assert actual == expected

def test_multi_bracket_validation_parenthes_inside_curly():
    expected = False
    actual = multi_bracket_validation("{(})")
    assert actual == expected

def test_multi_bracket_validation_one_opening_curly():
    expected = False
    actual = multi_bracket_validation("{")
    assert actual == expected

def test_multi_bracket_validation_different_closing_opening():
    expected = False
    actual = multi_bracket_validation("[)")
    assert actual == expected

def test_multi_bracket_validation_one_closing_parenthes():
    expected = False
    actual = multi_bracket_validation(")")
    assert actual == expected

def test_multi_bracket_validation_string_with_closing_opening_different():
    expected = False
    actual = multi_bracket_validation("{sadsad)")
    assert actual == expected

def test_multi_bracket_validation_string_with_one_closing_parenthes():
    expected = False
    actual = multi_bracket_validation("fsads(")
    assert actual == expected

def test_multi_bracket_validation_string_only():
    expected = False
    actual = multi_bracket_validation("FFads")
    assert actual == expected