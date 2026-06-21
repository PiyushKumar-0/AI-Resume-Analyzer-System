from parser import extract_text_from_pdf
from preprocess import clean_text
from skill_extractor import extract_skills
from ats_score import calculate_ats_score

from suggestions import (
    missing_skills,
    generate_suggestions
)

resume_text = extract_text_from_pdf(
    "resumes/Piyush_Resume.pdf"
)

clean_resume = clean_text(resume_text)

job_description = """
Looking for a Python Developer

Required Skills:

Python
SQL
Machine Learning
AWS
Docker
Git
"""

clean_job = clean_text(job_description)

resume_skills = extract_skills(clean_resume)

job_skills = extract_skills(clean_job)

score = calculate_ats_score(
    clean_resume,
    clean_job
)

missing = missing_skills(
    job_skills,
    resume_skills
)

recommendations = generate_suggestions(
    missing
)

print("\nATS Score:")
print(score, "%")

print("\nResume Skills:")
print(resume_skills)

print("\nMissing Skills:")
print(missing)

print("\nRecommendations:")

for rec in recommendations:
    print("-", rec)