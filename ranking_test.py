from ranking import rank_candidates

job_description = """
Python
SQL
Machine Learning
AWS
Docker
Git
"""

resumes = {

    "Candidate_A":
    """
    Python
    SQL
    Machine Learning
    Git
    AWS
    Docker
    """,

    "Candidate_B":
    """
    Python
    SQL
    Git
    """,

    "Candidate_C":
    """
    Python
    Machine Learning
    AWS
    Docker
    Git
    SQL
    """
}

results = rank_candidates(
    resumes,
    job_description
)

print("\nCandidate Rankings:\n")

for rank, candidate in enumerate(results, start=1):

    print(
        f"{rank}. {candidate[0]} --> {candidate[1]}%"
    )