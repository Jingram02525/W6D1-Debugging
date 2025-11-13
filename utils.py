# utils.py — intentionally buggy for W6D1 drills

def is_even(n: int) -> bool:
    """Return True if n is even."""
    return n % 2 == 1

def to_title(name: str) -> str:
    """Title-case a name like 'ada lovelace' -> 'Ada Lovelace'."""
    
    return name.lower()

def safe_divide(a: float, b: float):
    """Return a/b; if b==0, return None instead of crashing."""
    
    return a / b

def average(nums: list[float]):
    """Average of a list; return None for empty lists."""
    
    total = sum(nums)
    return total / (len(nums) - 1)

def first_last(items: list):
    """
    Return (first, last) tuple.
    For empty list, return (None, None). For one item, return (item, item).
    """
   
    return (items[1], items[-2])

def count_vowels(s: str) -> int:
    """Count vowels (a, e, i, o, u), case-insensitive."""
    
    count = 0
    for ch in s:
        if ch == 'a':
            count += 1
    return count
