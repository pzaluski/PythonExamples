import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from URL.

    Args:
        url: URL of UTF-8 doc.
    
    Returns:
        A list of strings from document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_itmes(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_itmes(words)


if __name__ == '__main__':
    main(sys.argv[1])
