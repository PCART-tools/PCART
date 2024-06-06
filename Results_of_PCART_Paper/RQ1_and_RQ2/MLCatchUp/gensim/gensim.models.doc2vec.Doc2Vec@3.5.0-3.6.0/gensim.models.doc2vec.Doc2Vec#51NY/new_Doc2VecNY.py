from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.test.utils import common_texts
model = Doc2Vec(None, None, 1, 0, dm_concat=0, dm_tag_count=1, docvecs=None, docvecs_mapfile=None, comment=None, corpus_file=None)
