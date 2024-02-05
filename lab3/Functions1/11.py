def is_palindrome(word):
    cleaned_word = ''.join(word.lower().split())
    return cleaned_word == cleaned_word[::-1]


word_to_check = "salas"
if is_palindrome(word_to_check):
    print(f"{word_to_check} is a palindrome.")
else:
    print(f"{word_to_check} is not a palindrome.")
