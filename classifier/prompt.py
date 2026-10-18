def make_prompt(question, code):
    return f"""
    Imagine you are a DSA mentor. Assess the given code and its details to assess the user's approach towards the question and analyse the complexities and patterns of the question and give a final analysis. You should return your analysis in the below given JSON structure:

    Question: {question}
    Code: {code}

    Classify patterns only from this list: Two Pointer, Sliding Window, Dynamic Programming, Graphs, Binary Search, Backtracking, Greedy, Other.

    {{
    "patterns_used": ".....",
    "optimal_pattern": "....",
    "approach_match": "...."(true/false),
    "user_time_complexity": "...",
    "user_space_complexity": "...",
    "optimal_time_complexity": "..",
    "optimal_space_complexity": "...."
    }}


    Return the analysis strictly in JSON only.
"""