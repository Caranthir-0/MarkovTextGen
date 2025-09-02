from collections import defaultdict
import random

# unused function
#def build_bigrams(tokens):
#    bigrams = []
#    for i in range(len(tokens) - 1):
#        head = tokens[i]
#        tail = tokens[i + 1]
#        bigrams.append((head, tail))
#    return bigrams

def build_trigrams(tokens):
    trigrams = []
    for i in range(len(tokens) - 2):
        head = tokens[i] + " " + tokens[i + 1]  # head: 2 słowa
        tail = tokens[i + 2]  # tail: 1 słowo
        trigrams.append((head, tail))
    return trigrams

def build_markov_model(bigrams):
    model = defaultdict(lambda: defaultdict(int))
    for head, tail in bigrams:
        model[head][tail] += 1
    return model

def generate_pseudo_sentence(model, min_len=5):
    while True:
        head = random.choice(list(model.keys()))
        first_word = head.split()[0]
        if first_word[0].isupper() and not first_word.endswith(('.', '!', '?')):
            break

    sentence = head.split()

    while True:
        tails = list(model[head].keys())
        weights = list(model[head].values())
        if not tails:  # dead end
            sentence.append('.')
            break

        tail = random.choices(tails, weights=weights, k=1)[0]
        sentence.append(tail)

        if len(sentence) >= min_len and tail.endswith(('.', '!', '?')):
            break

        head = " ".join(sentence[-2:])  # przesuwamy head

    return " ".join(sentence)

def main():
    filename = input()
    if not filename.endswith(".txt"):
        filename += ".txt"

    with open(filename, 'r', encoding='utf-8') as f:
        tokens = f.read().split()


    trigrams = build_trigrams(tokens)
    model = build_markov_model(trigrams)

    # Generate 10 pseudo-sentences
    for _ in range(10):
        print(generate_pseudo_sentence(model))

if __name__ == "__main__":
    main()