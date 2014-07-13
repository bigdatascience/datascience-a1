import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)
    scores = {}
    for line in open(sys.argv[1]):
        term, score = line.split("\t")
        scores[term] = int(score)
    for line in open(sys.argv[2]):
        message = json.loads(line)
        sentiment = 0
        if "text" in message:
            words = line.split(" ")
            for word in words:
                if word in scores:
                    sentiment += scores[word]
        print sentiment

if __name__ == '__main__':
    main()