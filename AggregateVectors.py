# Aggregates each document vector by average

def aggregate_vectors(corpus, model):
    all_aggr = []
    for doc in corpus:
        vec = model.wv[doc]
        aggr = vec.sum(axis=0)
        aggr = aggr / len(doc)
        all_aggr.append(aggr)
    return all_aggr
