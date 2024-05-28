def make_snippet(string):
    if len(string) > 5:
        return string[:5] + '...'
    return string

def count_words(string):
    return len(string.split())