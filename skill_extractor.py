import pandas as pd

skills_db = pd.read_csv("datasets/skills.csv")

skills_list = skills_db["skill"].tolist()

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill.lower() in text:

            found_skills.append(skill)

    return found_skills