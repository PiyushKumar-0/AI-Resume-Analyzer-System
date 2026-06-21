def calculate_skill_match(
    resume_skills,
    job_skills
):

    matched = list(
        set(resume_skills)
        &
        set(job_skills)
    )

    if len(job_skills) == 0:
        return 0, matched

    percentage = (
        len(matched)
        /
        len(job_skills)
    ) * 100

    return round(
        percentage,
        2
    ), matched