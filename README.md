# EnglishFastText
Use wikipedia to train your fastText embedding model!

## Preprocess wiki data 
1. Download Wikipedia database dump [here](https://dumps.wikimedia.org/)
> mkdir wiki\_dump
> wget https://dumps.wikimedia.org/wikidatawiki/20xxxxxx/wikidatawiki-20xxxxxx-pages-articles-multistream.xml.bz2 -O wiki\_dump/

2. Process wikipedia using [wikiextractor](https://github.com/attardi/wikiextractor)
> git clone https://github.com/attardi/wikiextractor.git
> mkdir wikidata -p
> python3 wikiextractor/WikiExtractor.py wikidatawiki-20xxxxxx-pages-articles-multistream.xml.bz2 -o wikiextract --processes 8 \
		--no-templates

according to official documentation, "--no-templates" will "significantly" speedup the extractor.

## FastText
1. Build fastText package. [reference](https://github.com/facebookresearch/fastText.git)
> wget https://github.com/facebookresearch/fastText/archive/v0.1.0.zip
> unzip v0.1.0.zip
> cd fastText-0.1.0
> make 

2. Start training your model ! 
>  /fasttext skipgram -input data.txt -output model -dim 300 -minn 1 -maxn 6
