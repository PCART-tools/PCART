from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import common_texts
documents = [TaggedDocument(doc, [i]) for (i, doc) in enumerate(common_texts)]
model = Doc2Vec(documents, vector_size=5, window=2, min_count=1, workers=4)
doc_words1 = ['human', 'interface', 'computer']
doc_words2 = ['system', 'response', 'user']
similarity = model.similarity_unseen_docs(doc_words1=doc_words1, doc_words2=doc_words2, alpha=0.025)
