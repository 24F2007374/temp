def longest_positive_streak(nums: list[int]) -> int:
    """
    Returns the length of the longest run of consecutive positive numbers (>0).
    - Empty list returns 0.
    - Non-positive numbers reset the streak.
    - Must be deterministic and pure (no randomness, no prints, no global state).
    """
    if not nums:
        return 0

    max_streak = 0
    current_streak = 0
    for num in nums:
        if num > 0:
            current_streak += 1
        else:
            max_streak = max(max_streak, current_streak)
            current_streak = 0
    max_streak = max(max_streak, current_streak)
    return max_streak