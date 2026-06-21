def analyze_resume(score, missing):

    strengths = []
    weaknesses = []

    if score >= 80:
        strengths.append(
            "Excellent ATS compatibility"
        )

    elif score >= 60:
        strengths.append(
            "Good ATS compatibility"
        )

    else:
        weaknesses.append(
            "Low ATS compatibility"
        )

    if len(missing) <= 2:
        strengths.append(
            "Strong skill alignment"
        )

    else:
        weaknesses.append(
            "Several important skills are missing"
        )

    return strengths, weaknesses