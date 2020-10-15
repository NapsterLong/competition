from collections import defaultdict
import random

unsupervised_corpus = []
idx2queries = {}
for line in open("../datas/train/train.query.tsv"):
    line_sp = line.strip().split("\t")
    idx2queries[line_sp[0].strip()] = line_sp[1].strip()
    unsupervised_corpus.append(line_sp[1].strip())

train_set = []
dev_set = []
test_test = []

for line in open("../datas/train/train.reply.tsv"):
    line_sp = line.strip().split("\t")
    idx = line_sp[0]
    pos = line_sp[1]
    text = line_sp[2]
    label = line_sp[3]
    query = idx2queries.get(idx)
    train_set.append([idx, query, text, label])
    unsupervised_corpus.append(text)

random.shuffle(train_set)
dev_test = train_set[:1000]
train_set = train_set[1000:]

with open("../datas/real/train.tsv", "w", encoding="utf-8") as w:
    w.write("\t".join(["index", "sentence1", "sentence2", "label"]) + "\n")
    for line in train_set:
        w.write("\t".join(line) + "\n")

with open("../datas/real/dev.tsv", "w", encoding="utf-8") as w:
    w.write("\t".join(["index", "sentence1", "sentence2", "label"]) + "\n")
    for line in dev_test:
        w.write("\t".join(line) + "\n")

idx2queries = {}
test_set = []
for line in open("../datas/test/test.query.tsv"):
    line_sp = line.strip().split("\t")
    idx2queries[line_sp[0].strip()] = line_sp[1].strip()
    unsupervised_corpus.append(line_sp[1].strip())

for line in open("../datas/test/test.reply.tsv"):
    line_sp = line.strip().split("\t")
    idx = line_sp[0]
    pos = line_sp[1]
    text = line_sp[2]
    query = idx2queries.get(idx)
    test_set.append([idx + "-" + pos, query, text])
    unsupervised_corpus.append(text)

with open("../datas/real/test.tsv", "w", encoding="utf-8") as w:
    w.write("\t".join(["index", "sentence1", "sentence2"]) + "\n")
    for line in test_set:
        w.write("\t".join(line) + "\n")

with open("../datas/train/lm_corpus.tsv", "w", encoding="utf-8") as writer:
    for text in unsupervised_corpus:
        writer.write(text.strip() + "\n")

print("done")
