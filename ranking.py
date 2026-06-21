from ats_score import calculate_ats_score

def rank_candidates(resumes, job_description):

    rankings = []

    for name, text in resumes.items():

        score = calculate_ats_score(
            text,
            job_description
        )

        rankings.append(
            (name, score)
        )

    rankings.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return rankings