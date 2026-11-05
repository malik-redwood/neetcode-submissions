from typing import List

def contains_duplicate(words: List[str]) -> bool:
    original_size = len(words)
    my_list = set()
    for i in range(len(words)):
        my_list.add(words[i])
    
    if original_size == len(my_list):
        return False
    else:
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
