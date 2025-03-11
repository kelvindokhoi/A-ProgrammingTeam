import re

# Example showing different regex concepts in Python

def demo_basic_patterns():
    # Basic character matching
    text = "The quick brown fox jumps over the lazy dog"
    print("Basic matching:", re.findall(r"fox", text))  # Finds 'fox'
    
    # Character classes
    print("Word chars:", re.findall(r"\w+", text))  # Splits into words
    print("Numbers:", re.findall(r"\d+", "There are 365 days in a year and 24 hours in a day"))
    print("Custom class:", re.findall(r"[aeiou]", text))  # Finds all vowels

def demo_quantifiers():
    # Different quantifier examples
    text = "aaaabbbccd"
    print("Greedy (*): ", re.search(r"a*", text).group())   # Matches 'aaaa'
    print("Greedy (+): ", re.search(r"a+", text).group())   # Matches 'aaaa'
    print("Lazy (*?):  ", re.search(r"a*?", text).group())  # Matches '' (empty)
    print("Lazy (+?):  ", re.search(r"a+?", text).group())  # Matches 'a' (just one)
    print("Exact {n}:  ", re.search(r"a{2}", text).group()) # Matches 'aa'
    print("Range {n,m}:", re.search(r"a{2,3}", text).group()) # Matches 'aaa'

def demo_groups_and_references():
    # Capturing groups
    text = "hello world hello"
    match = re.search(r"(hello) world \1", text)
    if match:
        print("Full match:", match.group(0))  # 'hello world hello'
        print("Group 1:", match.group(1))     # 'hello'
    
    # Named groups
    date_pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
    match = re.search(date_pattern, "Today's date: 2023-05-15")
    if match:
        print(f"Date: {match.group('year')}-{match.group('month')}-{match.group('day')}")

def demo_lookarounds():
    # Lookahead examples
    passwords = ["password123", "Password123", "PASSWORD", "pass"]
    pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"  # At least 8 chars, 1 uppercase, 1 digit
    
    print("Password validation:")
    for pwd in passwords:
        valid = "✓" if re.match(pattern, pwd) else "✗"
        print(f"  {pwd}: {valid}")
    
    # Practical lookbehind example - getting prices
    text = "Products: $15.99, €20.00, and £25.50"
    prices = re.findall(r"(?<=\$)\d+\.\d{2}", text)
    print("Dollar prices:", prices)  # ['15.99']

def demo_python_specific():
    # Verbose mode for readable patterns
    phone_pattern = re.compile(r"""
        \(?\d{3}\)?  # Area code
        [-.\s]?      # Separator
        \d{3}        # First 3 digits
        [-.\s]?      # Separator
        \d{4}        # Last 4 digits
    """, re.VERBOSE)
    
    text = "Call me at (555) 123-4567 or 555.987.6543"
    print("Phone numbers:", phone_pattern.findall(text))

if __name__ == "__main__":
    print("===== BASIC PATTERNS =====")
    demo_basic_patterns()
    
    print("\n===== QUANTIFIERS =====")
    demo_quantifiers()
    
    print("\n===== GROUPS AND REFERENCES =====")
    demo_groups_and_references()
    
    print("\n===== LOOKAROUNDS =====")
    demo_lookarounds()
    
    print("\n===== PYTHON-SPECIFIC FEATURES =====")
    demo_python_specific()