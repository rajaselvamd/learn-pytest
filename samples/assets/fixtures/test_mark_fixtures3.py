import pytest

"""
fixtures called from central file conftest.py
"""

def test_1(tc_setup):
    print("Test 1 executed")

def test_2(tc_setup):
    print("Test 2 executed")

def test_3():
    print("Test 3 executed")


