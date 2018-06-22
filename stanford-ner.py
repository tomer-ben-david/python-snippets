from nltk.tag.stanford import StanfordNERTagger
from nltk.tokenize import word_tokenize

def formatted_entities(classified_paragraphs_list):
    entities = {'organizations': list()}

    for classified_paragraph in classified_paragraphs_list:
        for entry in classified_paragraph:
            entry_value = entry[0]
            entry_type = entry[1]

            if entry_type == 'ORGANIZATION':
                entities['organizations'].append(entry_value)

    return entities


tagger = StanfordNERTagger('/Users/tomer.bendavid/Downloads/stanford-ner-2017-06-09/classifiers/english.all.3class.distsim.crf.ser.gz',
               '/Users/tomer.bendavid/Downloads/stanford-ner-2017-06-09/stanford-ner.jar',
               encoding='utf-8')


paragraphs = [
            'I just bought these Thomson Reuters shoes'
        ]

tokenized_paragraphs = list()

for text in paragraphs:
    tokenized_paragraphs.append(word_tokenize(text))

classified_paragraphs_list = tagger.tag_sents(tokenized_paragraphs)


formatted_result = formatted_entities(classified_paragraphs_list)
print(formatted_result)