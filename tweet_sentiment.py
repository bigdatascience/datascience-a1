import sys
import json


def hw(sent_file, tweet_file):
    scores = {};
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        message = json.loads(line)


def lines(fp):
    print str(len(fp.readlines()))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    lines(sent_file)
    lines(tweet_file)


if __name__ == '__main__':
    main()
