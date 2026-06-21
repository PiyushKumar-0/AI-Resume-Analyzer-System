def missing_skills(job_skills, resume_skills):

    missing = list(
        set(job_skills) - set(resume_skills)
    )

    return missing


def generate_suggestions(missing):

    suggestions = []

    for skill in missing:

        if skill == "aws":
            suggestions.append(
                "Learn AWS and complete a cloud project."
            )

        elif skill == "docker":
            suggestions.append(
                "Learn Docker and containerization."
            )

        elif skill == "git":
            suggestions.append(
                "Learn Git and GitHub for version control."
            )

        elif skill == "machine learning":
            suggestions.append(
                "Build Machine Learning projects and mention them in your resume."
            )

        elif skill == "sql":
            suggestions.append(
                "Practice SQL queries and database projects."
            )

        else:
            suggestions.append(
                f"Consider learning {skill}."
            )

    return suggestions