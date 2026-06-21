from collections import Counter

def top_keywords(text):

    words = text.split()

    counter = Counter(words)

    return counter.most_common(10)