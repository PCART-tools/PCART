from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
documents = [['cat', 'dog', 'mouse'], ['dog', 'wolf', 'rabbit'], ['fish', 'shark', 'whale']]
dictionary = Dictionary(documents)
corpus = [dictionary.doc2bow(doc) for doc in documents]
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=3)
coherence_model = CoherenceModel(lda_model, documents, dictionary, topics=None, window_size=None, topn=10)
