import json
from classifier.classify import classify

with open("data/submissions.json") as f:
    subs = json.load(f)

sub = subs[0]

with open(sub["code_file"]) as f:
    code = f.read()

result = classify(sub["question"], code)
print(result)