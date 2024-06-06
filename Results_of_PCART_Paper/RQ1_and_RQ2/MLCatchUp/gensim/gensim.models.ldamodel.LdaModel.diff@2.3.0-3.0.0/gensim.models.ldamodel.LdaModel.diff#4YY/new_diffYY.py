from gensim.models import LdaModel
from gensim.corpora.dictionary import Dictionary
documents = ['文档1的文本内容', '文档2的文本内容']
texts = [[word for word in document.lower().split()] for document in documents]
dictionary = Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda1 = LdaModel(corpus, id2word=dictionary, num_topics=10)
lda2 = LdaModel(corpus, id2word=dictionary, num_topics=10)
diff = lda1.diff(lda2, distance='kullback_leibler', diagonal=False, annotation=True)
