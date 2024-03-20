# Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


def find_first_index(haystack: str,  needle: str) -> int:
    return -1


def test_find_first_index():
    haystack = "sadbutsad"
    needle = "sad"
    # "sad" occurs at index 0 and 6, so returns 0
    assert find_first_index(haystack, needle) == 0

    haystack = "sabutsad"
    needle = "sad"
    # "sad" occurs at index 5, so returns 5
    assert find_first_index(haystack, needle) == 5
    
    haystack = "sabutsa"
    needle = "sad"
    # no "sad" found, so returns -1
    assert find_first_index(haystack, needle) == -1
    
    haystack = "oracle"
    needle = "orak"
    # no "orak" found in "oracle", so returns -1
    assert find_first_index(haystack, needle) == -1
