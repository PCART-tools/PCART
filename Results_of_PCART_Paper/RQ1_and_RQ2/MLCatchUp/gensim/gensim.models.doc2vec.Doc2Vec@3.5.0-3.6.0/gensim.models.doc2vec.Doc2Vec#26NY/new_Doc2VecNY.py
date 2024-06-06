from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import common_texts
model = Doc2Vec(None, None, dm=1, dbow_words=0, dm_concat=0, dm_tag_count=1, corpus_file=None)
