import json
from classifier.classify import classify
from analysis.weakness_score import weakness
from generator.practice_gen import gen_problems

with open("data/submissions.json") as f:
    subs = json.load(f)

classifications = []

for sub in subs:
    with open(sub["code_file"]) as f:
        code = f.read()

    res = classify(sub["question"], code)
    classifications.append(res)

scores = weakness(classifications)

weakest = None
highest = 0

for pattern in scores:
    if scores[pattern] > highest:
        weakest = pattern
        highest = scores[pattern]

print(f"Your weakest topic is: {weakest} ({highest: .1f})")

problems = gen_problems(scores)
for p in problems:
    print(f"\n{p["title"]} ({p["difficulty"]})\n{p["description"]}")