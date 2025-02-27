import re

# Example 1: Finding a Simple Match
print("Example 1: Finding a Simple Match")
text1 = "Hello, my number is 12345."
match1 = re.search(r"number", text1)
if match1:
    print("Found:", match1.group())
print()

# Example 2: Matching Digits
print("Example 2: Matching Digits")
text2 = "My phone is 555-123-4567."
numbers = re.findall(r"\d+", text2)
print("Numbers found:", numbers)
print()

# Example 3: Email Validation
print("Example 3: Email Validation")
text3 = "Contact me at user@example.com or test@domain.co."
emails = re.findall(r"[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}", text3)
print("Emails found:", emails)
print()

# Example 4: Replacing Text
print("Example 4: Replacing Text")
text4 = "Call me at 555-123-4567."
result = re.sub(r"\d{3}-\d{3}-\d{4}", "XXX-XXX-XXXX", text4)
print("After replacement:", result)
print()

# Example 5: Groups and Capturing
print("Example 5: Groups and Capturing")
text5 = "Date: 2025-02-27"
match5 = re.search(r"(\d{4})-(\d{2})-(\d{2})", text5)
if match5:
    year, month, day = match5.groups()
    print(f"Year: {year}, Month: {month}, Day: {day}")


# CHEATSHEET
#     re.search(pattern, string): Searches for the first match of the pattern in the string.
#     re.match(pattern, string): Checks if the pattern matches at the start of the string.
#     re.findall(pattern, string): Returns all non-overlapping matches of the pattern in the string as a list.
#     re.sub(pattern, replacement, string): Replaces matches with a new string.


# Regex uses special characters to define patterns. Here’s a quick cheat sheet:
#     .: Matches any single character (except newline).
#     *: Matches 0 or more occurrences of the previous character.
#     +: Matches 1 or more occurrences of the previous character.
#     ?: Matches 0 or 1 occurrence of the previous character.
#     \d: Matches any digit (0-9).
#     \w: Matches any word character (a-z, A-Z, 0-9, _).
#     \s: Matches any whitespace (spaces, tabs, etc.).
#     [abc]: Matches any one character in the set (e.g., a, b, or c).
#     [^abc]: Matches any character not in the set.
#     ^: Anchors the match to the start of the string.
#     $: Anchors the match to the end of the string.