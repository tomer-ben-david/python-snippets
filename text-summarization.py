#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:55:49 2018

@author: tomer.bendavid
"""

import sys

print('sys.version_info: ' + str(sys.version_info))

# 1. Cleanup
# 2. Word Freq (title + description)
# 3. Print first words based on weight.
# ***4*** enhance with the below stemmer

## Use this to enhance albgorithms pass all words through it!!! ##
from typing import Dict, Set, Any, Tuple

from nltk import FreqDist
from nltk.probability import FreqDist

import nltk
from nltk.stem.porter import *
stemmer = PorterStemmer()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string


def remove_punctuations(s: str) -> str:
    table = str.maketrans({key: None for key in string.punctuation})
    return s.translate(table)

def stem(words): return map(lambda w: stemmer.stem(w), words)


def word_index(fullText: str, w: Tuple[str, int]) -> int:
    return fullText.lower().index(w[0])

def top_scores_sorted_by_text(someText: str, w_scores: FreqDist, k: int):
    return sorted(w_scores.most_common(k), key=lambda w: word_index(someText, w))


# Some text from wikipedia.
text: str = """
    Leonardo da Vinci
    Leonardo di ser Piero da Vinci (Italian: [leoˈnardo di ˌsɛr ˈpjɛːro da (v)ˈvintʃi] (About this sound listen); 15 April 1452 – 2 May 1519), more commonly Leonardo da Vinci or simply Leonardo, was an Italian polymath of the Renaissance, whose areas of interest included invention, painting, sculpting, architecture, science, music, mathematics, engineering, literature, anatomy, geology, astronomy, botany, writing, history, and cartography. He has been variously called the father of palaeontology, ichnology, and architecture, and is widely considered one of the greatest painters of all time. Sometimes credited with the inventions of the parachute, helicopter and tank,[1][2][3] he epitomised the Renaissance humanist ideal.

Many historians and scholars regard Leonardo as the prime exemplar of the "Universal Genius" or "Renaissance Man", an individual of "unquenchable curiosity" and "feverishly inventive imagination",[4] and he is widely considered one of the most diversely talented individuals ever to have lived.[5] According to art historian Helen Gardner, the scope and depth of his interests were without precedent in recorded history, and "his mind and personality seem to us superhuman, while the man himself mysterious and remote".[4] Marco Rosci notes that while there is much speculation regarding his life and personality, his view of the world was logical rather than mysterious, and that the empirical methods he employed were unorthodox for his time.[6]

Born out of wedlock to a notary, Piero da Vinci, and a peasant woman, Caterina, in Vinci in the region of Florence, Leonardo was educated in the studio of the renowned Florentine painter Andrea del Verrocchio. Much of his earlier working life was spent in the service of Ludovico il Moro in Milan. He later worked in Rome, Bologna and Venice, and he spent his last years in France at the home awarded to him by Francis I of France.

Leonardo was, and is, renowned primarily as a painter. Among his works, the Mona Lisa is the most famous and most parodied portrait[7] and The Last Supper the most reproduced religious painting of all time.[4] Leonardo's drawing of the Vitruvian Man is also regarded as a cultural icon,[8] being reproduced on items as varied as the euro coin, textbooks, and T-shirts.

A painting by Leonardo, Salvator Mundi, sold for a world record $450.3 million at a Christie's auction in New York, 15 November 2017, the highest price ever paid for a work of art.[9] Perhaps fifteen of his paintings have survived.[nb 1] Nevertheless, these few works, together with his notebooks, which contain drawings, scientific diagrams, and his thoughts on the nature of painting, compose a contribution to later generations of artists rivalled only by that of his contemporary, Michelangelo.

Leonardo is revered for his technological ingenuity. He conceptualised flying machines, a type of armoured fighting vehicle, concentrated solar power, an adding machine,[10] and the double hull. Relatively few of his designs were constructed or even feasible during his lifetime, as the modern scientific approaches to metallurgy and engineering were only in their infancy during the Renaissance. Some of his smaller inventions, however, such as an automated bobbin winder and a machine for testing the tensile strength of wire, entered the world of manufacturing unheralded. A number of Leonardo's most practical inventions are nowadays displayed as working models at the Museum of Vinci. He made substantial discoveries in anatomy, civil engineering, geology, optics, and hydrodynamics, but he did not publish his findings and they had no direct influence on later science.[11]"""

# Removing stop words and making frequency table

text = remove_punctuations(text)
text = text.lower()
words = word_tokenize(text)
stop_words: Set[str] = set(stopwords.words("english"))
words = [w for w in words if not w in stop_words]
text = ' '.join(words)

# words = stem(words)

# Word freq table
words_score: FreqDist = FreqDist()
for word in words:
    words_score[word.lower()] += 1

# Score to sentences

summary = top_scores_sorted_by_text(text, words_score, 7)
print(summary)

#maybe filter nounds now.

## Text Classification ## 

## Feature Matrix

# Create BOW bag of words

from sklearn.feature_extraction.text import CountVectorizer
import json

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train',categories=categories, shuffle=True, random_state=42)
twenty_train.target_names = ['alt.atheism', 'comp.graphics', 'sci.med', 'soc.religion.christian']
# Each distinct word is a feature!
# Use BOW as features, each word is a feature, sparse matrix.

count_vect = CountVectorizer() 
X_train_counts = count_vect.fit_transform(twenty_train.data) # Tokenize, Filter Stopwords, BOW Features, Transform to vetor, this returns Term Document Matrix! thanks sklearn
# > X_train_counts.shape
# > count_vect.vocabulary_.get(u'algorithm') # Get features.

# TFIDF: Occurences --> Relative Frequencies (Eliminate doc size factor)
from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts) # Transform a count matrix to a normalized tf or tf-idf representation
X_train_tf = tf_transformer.transform(X_train_counts) # Transform a count matrix to a tf or tf-idf representation # X_train_tf.shape
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)


## Train the classifier!

from sklearn.naive_bayes import MultinomialNB # Naive bayes classifier
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

## Predict!

docs_new = ["""
Abortion
Synonyms	Induced miscarriage, termination of pregnancy
Specialty	Obstetrics and gynecology
ICD-10-PCS	O04
ICD-9-CM	779.6
MeSH	D000028
MedlinePlus	007382
[edit on Wikidata]
Abortion is the ending of pregnancy by removing an embryo or fetus before it can survive outside the uterus.[note 1] An abortion that occurs spontaneously is also known as a miscarriage. An abortion may be caused purposely and is then called an induced abortion, or less frequently, "induced miscarriage". The word abortion is often used to mean only induced abortions. A similar procedure after the fetus could potentially survive outside the womb is known as a "late termination of pregnancy".[1]

When allowed by law, abortion in the developed world is one of the safest procedures in medicine.[2][3] Modern methods use medication or surgery for abortions.[4] The drug mifepristone in combination with prostaglandin appears to be as safe and effective as surgery during the first and second trimester of pregnancy.[4][5] Birth control, such as the pill or intrauterine devices, can be used immediately following abortion.[5] When performed legally and safely, induced abortions do not increase the risk of long-term mental or physical problems.[6] In contrast, unsafe abortions (those performed by unskilled individuals, with hazardous equipment, or in unsanitary facilities) cause 47,000 deaths and 5 million hospital admissions each year.[6][7] The World Health Organization recommends safe and legal abortions be available to all women.[8]

Around 56 million abortions are performed each year in the world,[9] with about 45% done unsafely.[10] Abortion rates changed little between 2003 and 2008,[11] before which they decreased for at least two decades as access to family planning and birth control increased.[12] As of 2008, 40% of the world's women had access to legal abortions without limits as to reason.[13] Countries that permit abortions have different limits on how late in pregnancy abortion is allowed.[13]

Historically, abortions have been attempted using herbal medicines, sharp tools, forceful massage, or through other traditional methods.[14] Abortion laws and cultural or religious views of abortions are different around the world. In some areas abortion is legal only in specific cases such as rape, problems with the fetus, poverty, risk to a woman's health, or incest.[15] In many places there is much debate over the moral, ethical, and legal issues of abortion.[16][17] Those who oppose abortion often maintain that an embryo or fetus is a human with a right to life, and so they may compare abortion to murder.[18][19] Those who favor the legality of abortion often hold that a woman has a right to make decisions about her own body.[20] Others favor legal and accessible abortion as a public health measure.[21]"""]
X_new_counts = count_vect.transform(docs_new) # Extract new doc features.
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))