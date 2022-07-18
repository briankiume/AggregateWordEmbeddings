# AggregateWord Embeddings
A simple function to quickly return aggregate Word Embeddings

## Description 
The function takes **a corpus** and **NLP model** as arguments. 

>*Corpus:* Follows the format *[['Data', 'is', 'fun'], ['Data', 'is', 'Hardwork']...]*
> 
> - Word tokens within each document

>*Model:* Can be Spacy generated Embeddings, Word2Vec...
> 
> - *example model:* Word2Vec(corpus, min_count=1, vector_size=100, sg=1, epochs=10, workers=6, window=2)


## Usage
The code below shows its usage on a word token, within a document, within a corpus.  
```
model = Word2Vec((filtered + filtered_2), min_count=1, vector_size=100, sg=1, epochs=10, workers=6, window=2)

all_aggr_1 = aggregate_vectors(filtered, model)
all_aggr_2 = aggregate_vectors(filtered_2, model)

```
 
## License
MIT License. Copyright (c) 2022 Brian Kiume