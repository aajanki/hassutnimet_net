#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import random


word_start = '^'
word_end = '$'


class Markov(object):
    def __init__(self, n, statistics, forbidden):
        self.n = n
        self.statistics = statistics
        self.forbidden = forbidden


def ngrams(n, word):
    for i in range(len(word) - n + 1):
        yield word[i:i+n]


def unzip(list_of_pairs):
    return [list(t) for t in zip(*list_of_pairs)]


def collect_statistics(rows, n):
    word_prefix = word_start * (n-1)
    
    names = []
    samples = {}
    for row in rows:
        word = row['Name']
        names.append(word)
        count = int(float(row['Count']))
        prepared_word = word_prefix + word + word_end
        for ngram in ngrams(n, prepared_word):
            prefix = ngram[:-1]
            successor = ngram[-1]

            counts = samples.get(prefix, {})
            counts[successor] = counts.get(successor, 0) + count
            samples[prefix] = counts

    markov_weights = {}
    for prefix, values in samples.items():
        markov_weights[prefix] = tuple(unzip(values.items()))
        
    return Markov(n, markov_weights, set(names))


def markov_sample(markov):
    context = (markov.n - 1) * word_start

    sample = []
    while True:
        successors, weights = markov.statistics[context]
        next_letter = random.choices(successors, weights)[0]
        if next_letter == word_end:
            break

        sample.append(next_letter)
        context = context[1:] + next_letter
        
    return ''.join(sample)

def markov_sample_forbidden(markov):
    while True:
        sample = markov_sample(markov)
        if sample not in markov.forbidden:
            return sample


def sample_name(first_chain, last_chain):
    num_first_names = random.choices([1, 2, 3], cum_weights=[60, 90, 100])[0]
    names = []
    for _ in range(num_first_names):
        names.append(markov_sample_forbidden(first_chain))
    names.append(markov_sample_forbidden(last_chain))
    return ' '.join(names)


def read_data(csvfilename):
    with open(csvfilename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row


def main():
    male_chain = collect_statistics(read_data('data/first-names-male.csv'), 3)
    female_chain = collect_statistics(read_data('data/first-names-female.csv'), 3)
    last_chain = collect_statistics(read_data('data/last-names.csv'), 4)

    for i in range(20):
        first_chain = male_chain if i % 2 == 0 else female_chain
        print(sample_name(first_chain, last_chain))


if __name__ == '__main__':
    main()
