import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc=nlp(text)
    entities={
        "NAME": [],
        "SKILLS": [],
        "EXPERIENCE":[],
        "EDUCATION":[],
    }


    for ent in doc.ents:
        if ent.label_=="PERSON":
            entities["NAME"].append(ent.text)
        elif ent.label_ =="ORG" and "University" in ent.text:
            entities["EDUCATION"].append(ent.text)
        elif ent.label_ == "ORG" and "Company" in ent.text:
            entities["EXPERIENCE"].append(ent.text)
        elif ent.label_ == "SKILL":
            entities["SKILLS"].append(ent.text)
        return entities
