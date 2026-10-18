def weakness(classifications):
    total = {}
    wrong = {}
    for c in classifications:
        curr = c["patterns_used"]
        if c["approach_match"] == False or c["user_time_complexity"] != c["optimal_time_complexity"]:
            wrong[curr] = wrong.get(curr, 0) + 1
        total[curr] = total.get(curr, 0) + 1    

    weak_scores = {}
    for pattern in total:
        weak_scores[pattern] = wrong.get(pattern, 0) / total.get(pattern, 1)

    return weak_scores