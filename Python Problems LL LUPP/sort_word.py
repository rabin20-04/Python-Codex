def sort_word(input_string):
    words = input_string.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w) // 2 :] for w in words]
    # w for w in words copies each element into a new list without modifying them.
    return " ".join(words)


print(sort_word("Hello what is up world"))
