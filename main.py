import json
from classifier.classify import classify
from analysis.weakness_score import weakness
from generator.practice_gen import gen_problems

with open("data/submissions.json") as f:
    subs = json.load(f)

# sub = subs[0]

# with open(sub["code_file"]) as f:
#     code = f.read()

# result = classify(sub["question"], code)
# print(result)

classifications = []
for sub in subs:
    with open(sub["code_file"]) as f:
        code = f.read()

    res = classify(sub["question"], code)
    classifications.append(res)

scores = weakness(classifications)
# print(scores)

result = gen_problems(scores)
print(result)