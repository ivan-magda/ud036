import os
import urllib


def read_text():
    file_path = os.getcwd() + "/movie_quotes.txt"

    quotes = open(file_path)
    content = quotes.read()
    print(content)
    quotes.close()

    check_profanity(content)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()


read_text()
