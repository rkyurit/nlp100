
def bigram(sentence):
    words = sentence.split(' ')
    chars = list(sentence.replace(' ', ''))

    return ([words[i] + words[i+1] for i in range(len(words)) if i + 1 < len(words)],
            [chars[i] + chars[i+1] for i in range(len(chars)) if i + 1 < len(chars)])


if __name__ == "__main__":
    sentence = 'I am an NLPer'
    w, c = bigram(sentence)
    print(w)
    print(c)
