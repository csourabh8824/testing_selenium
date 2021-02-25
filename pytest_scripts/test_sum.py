# import math 
# import pytest

# @pytest.fixture
# def input_value():
#     input = 10
#     return input

# @pytest.fixture
# def input_value2():
#     input = 25
#     return input

# def test_sum(input_value):
#     num = input_value+10
#     assert num == 20

# def test_sqr(input_value2):
#     num1 = input_value2
#     assert num1 == 5*5



import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output