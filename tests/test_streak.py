from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_non_positive():
    assert longest_positive_streak([-1, -2, 0, -4, -5]) == 0

def test_mixed_numbers():
    assert longest_positive_streak([1, 2, -3, 4, 5, 0, 7, 8, 9]) == 3

def test_streak_at_beginning():
    assert longest_positive_streak([1, 2, 3, 0, -1]) == 3

def test_streak_at_end():
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4]) == 4

def test_multiple_streaks():
    assert longest_positive_streak([1, 0, 1, 2, 0, 1, 2, 3]) == 3

def test_single_positive():
    assert longest_positive_streak([1]) == 1

def test_single_non_positive():
    assert longest_positive_streak([-1]) == 0

def test_zeros():
    assert longest_positive_streak([0, 0, 0]) == 0

def test_long_list():
    assert longest_positive_streak([1] * 1000) == 1000