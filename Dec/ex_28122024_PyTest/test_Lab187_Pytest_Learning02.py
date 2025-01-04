import pytest

def method1():
    print("Hello World")

@pytest.mark.smoke
def test_method2():
    print("test1")
    assert 1-1 == 2

@pytest.mark.regression
def test_method3():
    print("test2")
    assert 1 + 1 == 2





"""
def test_method2():
    print("test1")
    assert 1 - 1 == 0


def test_method3():
    print("test2")
    assert 1 + 1 == 2


# To run both the method in one go,
# In terminal, type pytest followed by the "name of pah from Content root."
"""
#pytest Dec/ex_28122024_PyTest/test_Lab187_Pytest_Learning02.py --html=report.html

#pytest --html=report.html Dec/ex_28122024_PyTest/test_Lab187_Pytest_Learning02.py


