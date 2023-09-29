from practice import square
import pytest


def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_nagative():
    assert square(-2) == 4
    assert square(-3) == 9
def test_zero():
    assert square(0) == 0

# Now at first we see 'FF.' it means first 2 programs failed and the last one passed. 
# If we fix the problem again then we'll see '...'. It means all 3 passed.
# What the user gives str instead of an integer num?
# We have to test it too .

# We can see if we run the program without solving the program and if we give an input which is str but not integer, then we can see the error TypeError.

# As matter of fact we can find a function of pytest. 
# So we are now going to import pytest.
# The function in that library called 'raises' that allows me to express that I can expect an exception to be raised.
def test_str():
    with pytest.raises(TypeError):
        square("cat")
# We have to use 'with' in this case.
# Now we can see that all 4 now are successful.
