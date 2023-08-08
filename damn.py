def reverse_words():
    words = input("Enter five words separated by spaces: ").split()
    reversed_words = words[::-1]
    print(" ".join(reversed_words))

reverse_words()
