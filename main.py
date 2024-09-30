# ------------------------------------------------------------------------

# Lab 1
# Problem 1
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.

# Problem 2
# Put your solution here, make sure I can run it by running this file. Do not submit it commented out.

# -----------------------------------------------------------------------------


# Importing sys for test function
import sys

# Test Function
def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
    print(msg)

# Function 1: count_vowels
def count_vowels(s):
    """ Returns the number of vowels in the string s. """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Unit Tests for count_vowels
def test_count_vowels():
    test(count_vowels("hello") == 2)
    test(count_vowels("why") == 0)
    test(count_vowels("aeiou") == 5)
    test(count_vowels("") == 0)
    test(count_vowels("bcdfg") == 0)
    test(count_vowels("aeiouAEIOU") == 10)
    test(count_vowels("HELLO") == 2)
    test(count_vowels("aEiOu") == 5)
    test(count_vowels("a e i o u") == 5)
    test(count_vowels("rhythm") == 0)

# Function 2: merge_lists
def merge_lists(list1, list2):
    """ Merges two sorted lists into one sorted list. """
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    return merged

# Unit Tests for merge_lists
def test_merge_lists():
    test(merge_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([], []) == [])
    test(merge_lists([1], [2]) == [1, 2])
    test(merge_lists([1, 1], [2, 2]) == [1, 1, 2, 2])
    test(merge_lists([1, 3, 5], []) == [1, 3, 5])
    test(merge_lists([], [2, 4, 6]) == [2, 4, 6])
    test(merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6])
    test(merge_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    test(merge_lists([1, 1, 2, 3], [1, 2, 2, 3]) == [1, 1, 1, 2, 2, 2, 3, 3])

# Function 3: word_lengths
def word_lengths(words):
    """ Returns a list with the lengths of each word in the list of words. """
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

# Unit Tests for word_lengths
def test_word_lengths():
    test(word_lengths(["hello", "world", "python"]) == [5, 5, 6])
    test(word_lengths([]) == [])
    test(word_lengths(["word"]) == [4])
    test(word_lengths(["short", "mediummm", "longesttttt"]) == [5, 8, 10])
    test(word_lengths(["", "a", "ab", "abc"]) == [0, 1, 2, 3])
    test(word_lengths(["  ", "a b", " c "]) == [2, 3, 3])

# Function 4: reverse_string
def reverse_string(s):
    """ Reverses the given string s. """
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

# Unit Tests for reverse_string
def test_reverse_string():
    test(reverse_string("python") == "nohtyp")
    test(reverse_string("") == "")
    test(reverse_string("a") == "a")
    test(reverse_string("aaa") == "aaa")
    test(reverse_string("Hello, World!") == "!dlroW ,olleH")
    test(reverse_string("12345") == "54321")
    test(reverse_string("  spaces  ") == "  secaps  ")

# Function 5: intersection
def intersection(list1, list2):
    """ Returns the intersection of two lists as a new list. """
    result = []
    for elem in list1:
        if elem in list2 and elem not in result:
            result.append(elem)
    return result

# Unit Tests for intersection
def test_intersection():
    test(intersection([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4])
    test(intersection([], []) == [])
    test(intersection([1, 2], [3, 4]) == [])
    test(intersection([1, 2], [1, 2]) == [1, 2])
    test(intersection([1, 2, 2, 3], [2, 2, 3, 4]) == [2, 3])
    test(intersection([1, 2, 3], [4, 5, 6]) == [])
    test(intersection([1, 2, 3], [1, 2, 3]) == [1, 2, 3])

# Test Suite
def test_suite():
    test_count_vowels()
    test_merge_lists()
    test_word_lengths()
    test_reverse_string()
    test_intersection()

# Run Test Suite
test_suite()

