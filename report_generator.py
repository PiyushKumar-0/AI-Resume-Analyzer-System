from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    filename,
    score,
    skill_match,
    resume_skills,
    missing_skills,
    recommendations
):

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Resume Screening Report",
            styles['Title']
        )
    )

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            f"ATS Score: {score}%",
            styles['Normal']
        )
    )

    content.append(
        Paragraph(
            f"Skill Match: {skill_match}%",
            styles['Normal']
        )
    )

    content.append(
        Spacer(1, 15)
    )

    content.append(
        Paragraph(
            "Skills Found",
            styles['Heading2']
        )
    )

    for skill in resume_skills:
        content.append(
            Paragraph(
                f"• {skill}",
                styles['Normal']
            )
        )

    content.append(
        Spacer(1, 15)
    )

    content.append(
        Paragraph(
            "Missing Skills",
            styles['Heading2']
        )
    )

    for skill in missing_skills:
        content.append(
            Paragraph(
                f"• {skill}",
                styles['Normal']
            )
        )

    content.append(
        Spacer(1, 15)
    )

    content.append(
        Paragraph(
            "Recommendations",
            styles['Heading2']
        )
    )

    for rec in recommendations:
        content.append(
            Paragraph(
                f"• {rec}",
                styles['Normal']
            )
        )

    doc.build(content)