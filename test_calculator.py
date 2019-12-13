from calculator import add,multiply
#Test addition
def test_add_zeros_function():
    assert add(0,0) == 0

def test_add_negatives_function():
    assert add(-1,-1) == -2 

def test_add_positives_function():
    assert add(4,5)  == 9  

def test_add_multiples_function():
    assert add(1,2,3,4) == 10  

#Test multiply

def test_multiply_positives_function():
    assert multiply(1,2) == 2

def test_multiply_many_function():
    assert multiply(1,2,3,4) == 24   

