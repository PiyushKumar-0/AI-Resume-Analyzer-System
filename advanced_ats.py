from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def advanced_ats_score(
    resume_text,
    job_text,
    resume_skills,
    job_skills
):

    if len(job_skills) > 0:

        skill_score = (
            len(
                set(resume_skills).intersection(
                    set(job_skills)
                )
            )
            /
            len(job_skills)
        ) * 100

    else:

        skill_score = 0

    vectorizer = TfidfVectorizer()

    matrix = vectorizer.fit_transform(
        [resume_text, job_text]
    )

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0] * 100

    final_score = (
        0.6 * skill_score
        +
        0.4 * similarity
    )

    return round(final_score, 2)