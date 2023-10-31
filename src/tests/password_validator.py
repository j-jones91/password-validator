import pytest
from validator.password_validator import PasswordValidator 

@pytest.fixture
def validator():
    return PasswordValidator()

def test_valid_password(validator):
    validator.password = "Valid_123"
    assert validator.is_valid() == True

def test_short_password(validator):
    validator.password = "Sh_1"
    assert validator.is_valid() == False

def test_missing_uppercase(validator):
    validator.password = "missingupper_1"
    assert validator.is_valid() == False

def test_missing_lowercase(validator):
    validator.password = "MISSINGLOWER_1"
    assert validator.is_valid() == False

def test_missing_number(validator):
    validator.password = "MissingNumber_"
    assert validator.is_valid() == False

def test_missing_underscore(validator):
    validator.password = "MissingUnderscore1"
    assert validator.is_valid() == False
