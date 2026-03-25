import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture

def pre_and_post():
    print("open the browser")
    print("maximize the browser")
    print("Enter")
    print("login")
    yield
    print("logout")
    print("Close")


def test_tc_001(pre_and_post):
    print("Check the digital download")
    print("Click oon the digital download")


def test_tc_002(pre_and_post):
    print("Check 25$")
    print("add to cart")

def test_tc_003(pre_and_post):
    print("click radio buttons in community pole")

