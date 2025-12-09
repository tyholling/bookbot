# bookbot

bookbot is a tool to analyze text files to calculate word count and symbol frequency.

This is a guided project from https://www.boot.dev.

# usage
```
$ mkdir books
$ curl -L https://www.gutenberg.org/ebooks/41445.txt.utf-8 -o books/frankenstein.txt
$ python3 main.py books/frankenstein.txt
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
 : 70480
e: 44538
t: 29493
a: 25894
o: 24494
...
============= END ===============
```
