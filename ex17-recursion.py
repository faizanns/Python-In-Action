def palindrome(word):
    if len(word) <= 1:
        return "Hurray, it's a Palindrome!"
    elif word[0] == word[len(word) - 1]:
        return(palindrome(word[1:len(word) - 1]))
    else:
        return "No, it isn't a Palindrome :("

print(palindrome("anna"))
print(palindrome("tacocat"))