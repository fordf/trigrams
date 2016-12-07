"""Program that uses creates trigram text."""


import io
import re


def main(src, num):
    """Main function."""
    tri_dict = parse_into_dict(src)
    return gen_text(tri_dict, num)


def parse_into_dict(src):
    """Take file and return trigram dictionary."""
    text = io.open(src, encoding="utf-8").read()
    text = cleanup(text).split(' ')
    tri_dict = {}
    for i in range(len(text) - 2):
        next_two = text[i] + ' ' + text[i + 1]
        try:
            tri_dict[next_two].append(text[i + 2])
        except:
            tri_dict.setdefault(next_two, [text[i + 2]])
    return tri_dict


def cleanup(text):
    clean_text = text.lower().replace('\n', ' ')
    clean_text = clean_text.replace('--', ' ')
    clean_text = re.sub('[^a-zA-Z0-9.\-]', ' ', clean_text)
    return clean_text
