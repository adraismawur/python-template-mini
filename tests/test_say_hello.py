import sys

from your_project_name.module1.funct_say_hello import say_hello


def test_say_hello_valid():
    assert say_hello("not/a/file") is None
