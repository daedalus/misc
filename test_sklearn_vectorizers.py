#!/usr/bin/env python
# Author Dario Clavijo 2018
# GPLv3

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

from sklearn.decomposition import TruncatedSVD
from sklearn.random_projection import sparse_random_matrix
import pandas as pd

mydocuments = [
    "hola",
    "hola mundo",
    "hi",
    "hello world",
    "hello how are you?",
    "konichiwa",
    "toire wa doko desu ka",
    "gde moya sobaka",
]


def vectorice(documents):
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(documents)
    # print X_train_counts
    pdd = pd.DataFrame(X_train_counts.toarray(), columns=count_vect.get_feature_names())
    return pdd


def TfidfVec(documents):
    vectorizer = TfidfVectorizer()
    trsfm = vectorizer.fit_transform(documents)
    pdd = pd.DataFrame(trsfm.toarray(), columns=vectorizer.get_feature_names())
    return pdd


def SVDred(data, n=None):
    if n == None:
        import math

        n = int(round(math.sqrt(data.shape[1])))
    svd = TruncatedSVD(n_components=n, n_iter=7, random_state=42)
    ret = svd.fit_transform(data)
    return ret


def test(documents):
    print "=" * 76
    print "Ground Truth"
    print "-" * 76
    print documents
    print "=" * 76
    print "Count Vectorize:"
    print "" * 76
    X = vectorice(documents)
    print X
    print "-" * 76
    print "SVD recuction:"
    print "-" * 76
    Y = SVDred(X)
    print Y
    print Y.shape
    print "=" * 76
    print "Tfidf Vectorize:"
    print "-" * 76
    X = TfidfVec(documents)
    print X
    print "-" * 76
    print "SVD recuction:"
    print "-" * 76
    Y = SVDred(X)
    print Y
    print Y.shape
    print "-" * 76


test(mydocuments)
