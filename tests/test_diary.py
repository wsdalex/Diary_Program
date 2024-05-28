from lib.diary import *

def test_make_snippet_returns_shortened_string():
    result = make_snippet('Hello my name is Will!')
    assert result == 'Hello...'

def test_make_snippet_returns_string_if_shorter_than_5_chars():
    result = make_snippet('Will')
    assert result == 'Will'


def test_count_words():
    result = count_words('Hello my name is will!')
    assert result == 5

def test_single_word():
    result = count_words('Hello')
    assert result == 1