def is_palindrome(word: str) -> bool:
    return word.lower() == word.lower()[::-1]
if __name__ == "__main__":
    print(is_palindrome("Level"))
