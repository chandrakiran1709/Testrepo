import sys
from wordcount import words_count
if len(sys.argv) != 2:
    print("Usage: python wordcount.py <filename>")
else:
    filename = sys.argv[1]
    w_count = words_count(filename)
    if w_count:
        for word, count in w_count.items():
            print(f"{word}: {count} times")