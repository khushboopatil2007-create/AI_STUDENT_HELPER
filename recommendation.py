# AI Student Help Expert System
# This file matches student problems with the knowledge base.

from rules import rules


def get_recommendation(subject, problem):
    for rule in rules:
        if rule["subject"] == subject and rule["problem"] == problem:
            return rule["recommendation"]

    return "No specific recommendation found. Try studying the basic concepts of this topic."


# Test the function
if __name__ == "__main__":
    result = get_recommendation("Python", "basics")
    print("Recommendation:", result)