import pytest 
from calculate import * 

@pytest.fixture
def template():
    num = 10
    return num
    
def test_calculate_square(template):
    result = calculate_square(template)
    assert result == 100