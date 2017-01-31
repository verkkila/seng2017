#!/usr/bin/python
# -*- coding: utf-8

import pytest
import mycrypt
import timeit

''' Unit tests for mycrypt function. Basically ROT13, but also
capitalize or uncapitalize, and for numbers, replace with shifted
versions.

tr 'A-Za-z0-9!"#€%&/()=' 'n-za-mN-ZA-M!"#€%&/()=0-9'

If characters outside allowed ones are used as input, raise ValueError'''


@pytest.mark.parametrize("test_input,expected", [
    ("a", "N"),
    ("b", "O"),
    ("123", '!"#'),
    ("4", u'€')
])
def test_encode(test_input, expected):
    assert(mycrypt.encode(test_input)) == expected


@pytest.mark.parametrize("test_input", [
    'a', 'b', 'c', 'abbaacdc', u'!#€%#€%#€%#€%#'
])
def test_encode_decode(test_input):
    assert(mycrypt.decode(mycrypt.encode(test_input))) == test_input


@pytest.mark.parametrize("invalid_input", ['+', 'Ö', 'abcÖÄÖ'])
def test_invalid_char(invalid_input):
    with pytest.raises(ValueError):
        mycrypt.encode(invalid_input)


@pytest.mark.parametrize("invalid_input", [None, [6, 7]])
def test_invalid_types(invalid_input):
    with pytest.raises(TypeError):
        mycrypt.encode(invalid_input)
