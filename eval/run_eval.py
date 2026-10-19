import json
from classifier.classify import classify

with open("data/labeled_eval.json") as f:
    eval_data = json.load(f)

correct = 0
total = 0

for sub in eval_data:
    with open(sub["code_file"]) as f:
        code = f.read()

    res = classify(sub["question"], code)
    if sub["true_pattern"] == res["patterns_used"]:
        correct += 1

    total += 1

accuracy = correct / total
print(accuracy)