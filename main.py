from stats import count_words
from stats import count_characters
from stats import print_report
from stats import chars_dict_to_sorted_list
import sys

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(1)
bookfile = sys.argv[1]
def get_book_text(bookfile):
  with open(bookfile) as f:
    return f.read()
charcount = count_characters(get_book_text(bookfile))

def main():
  print(str(count_words(get_book_text(bookfile))) + " words found in the document")
  print(charcount)
  print_report(count_words(get_book_text(bookfile)), charcount, bookfile)

main()
