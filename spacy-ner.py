import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Apple iPhone 8 4.7" Display 64GB UNLOCKED Smartphone US $499.99')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)