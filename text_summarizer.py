import pickle as pickle #data preprocessing
from collections import Counter #tokenization
import keras #ML
# import utils
# import conv_utils
# import backend as K
import tensorflow as tf
import postprocessing as pr #helper

# #Step 1 - Load data
# with open('data/%s.pkl','rb') as fp:
#     heads, desc, keywords = pickle.load(fp)

# #headings
# i=0
# heads[i]

# #Articles
# desc[i]


# #Tokenize text
# def get_vocab(lst):
#     vocabcount, vocab = Counter(w for txt in lst for w in txt.split())
#     return vocab, vocabcount

# vocab, vocabcount = get_vocab(head+desc)

# print(vocab[:50])
# print ('....' , len(vocab))

# #Create word embeddings with GloVe
# path = 'glove.6B.zip'
# glove_weights = get_glove_weights(path, origin="http://nlp.stanford.edu/data/glove.6B.zip")
# word_embeddings = pr.build_glove_matrix(glove_weights, vocab)

# #3stacked LSTM RNN
# def build_model(embedding):
#     model = Sequential()
#     model.add(Embedding(weights=[embedding], name='embedding_1'))
#     for i in range(3):
#         lstm = LSTM(rnn_size,name='lstm_%d'%(i+1))
#         model.add(lstm)
#         model.add(Dropout(p_dense,name='dropout_%d'%(i+1)))
#     model.add(Dense())
#     model.add(Activation('softmax', name='activation'))
#     return model

# #Initialize Encoder RNN with Embeddings
# encoder = biuld_model(embedding)
# encoder.compile(loss='categorical_crossentropy',optimizer'rmsprop')
# encoder.save_weights('embeddings.pkl', overwrite=True)

# #Initialize Decoder RNN with Embeddigs
# with open('embeddings.pkl', 'rb')
#     embeddings = pickle.load(fp)
# decoder = build_model(embeddings)

# #Convert a given article to a headline
# headline1 = pr.gen_headline(decoder, desc[1])

# #Convert a given article to a headline
# headline2 = pr.gen_headline(decoder, desc[2])

