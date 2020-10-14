from collections import defaultdict

unsupervised_corpus = []
idx2queries = {}
for line in open("../datas/train/train.query.tsv"):
    line_sp = line.strip().split("\t")
    idx2queries[line_sp[0].strip()] = line_sp[1].strip()
    unsupervised_corpus.append(line_sp[1].strip())

with open("../datas/train/train.tsv", "w", encoding="utf-8") as w:
    for line in open("../datas/train/train.reply.tsv"):
        line_sp = line.strip().split("\t")
        idx = line_sp[0]
        pos = line_sp[1]
        text = line_sp[2]
        label = line_sp[3]
        query = idx2queries.get(idx)
        w.write("\t".join([query, text, pos, label]) + "\n")
        unsupervised_corpus.append(text)

for line in open("../datas/test/test.query.tsv"):
    line_sp = line.strip().split("\t")
    unsupervised_corpus.append(line_sp[1].strip())

for line in open("../datas/test/test.reply.tsv"):
    line_sp = line.strip().split("\t")
    unsupervised_corpus.append(line_sp[2].strip())

with open("../datas/train/lm_corpus.tsv", "w", encoding="utf-8") as writer:
    for text in unsupervised_corpus:
        writer.write(text.strip() + "\n")

print("done")
