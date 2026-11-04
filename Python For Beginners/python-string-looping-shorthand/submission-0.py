def print_string_characters(word1: str, word2: str) -> None:
    word = word1 + word2
    for i in range(len(word)):
        print(word[i])

# do not modify below this line
print_string_characters("Hello, World!", "Good Job!")
