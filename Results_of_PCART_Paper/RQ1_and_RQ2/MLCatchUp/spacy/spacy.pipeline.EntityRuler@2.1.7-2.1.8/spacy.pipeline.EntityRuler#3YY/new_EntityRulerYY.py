import spacy
from spacy.pipeline import EntityRuler
nlp = spacy.load('en_core_web_sm')
patterns = [{'label': 'ORG', 'pattern': 'OpenAI'}, {'label': 'GPE', 'pattern': [{'LOWER': 'san'}, {'LOWER': 'francisco'}]}]
entity_ruler = EntityRuler(nlp, 'LOWER', validate=False)
entity_ruler.add_patterns(patterns)
nlp.add_pipe(nlp.create_pipe('entity_ruler'))
doc = nlp('OpenAI is based in San Francisco.')
for ent in doc.ents:
    print(ent.text, ent.label_)
