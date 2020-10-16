from itertools import islice

model_type = "albert"

idx2result = {}
for line in islice(open(f"../output/{model_type}/test_results_wnli.txt"), 1, None):
    line_sp = line.strip().split("\t")
    idx2result[line_sp[0]] = line_sp[1]

idx = 0
with open(f"../datas/result/{model_type}_result.tsv", "w", encoding="utf-8") as w:
    for line in islice(open("../datas/real/test.tsv"), 1, None):
        line_sp = line.strip().split("\t")
        idx1, idx2 = line_sp[0].split("-")
        w.write("\t".join([idx1, idx2, idx2result[str(idx)]]) + "\n")
        idx += 1
print("done")
