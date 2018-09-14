# EnglishFastText
Use wikipedia to train your fastText embedding model!

## Preprocess wiki data 
1. Download Wikipedia database dump [here](https://dumps.wikimedia.org/)
> wget https://dumps.wikimedia.org/enwiki/20XXXXXX/enwiki-20XXXXXX-pages-articles-multistream.xml.bz2

2. Process wikipedia using [wikiextractor](https://github.com/attardi/wikiextractor)
> git clone https://github.com/attardi/wikiextractor.git \
> python3 wikiextractor/WikiExtractor.py wikidatawiki-20xxxxxx-pages-articles-multistream.xml.bz2 -o <wiki_dir> --processes 8 --no-templates

according to official documentation, "--no-templates" will "significantly" speedup the extractor.

3. merge extracted wiki data
> python3 merge.py <wiki_dir> <output_file name>

see setup.sh for example

## FastText
1. Build fastText package. [reference](https://github.com/facebookresearch/fastText.git)
> wget https://github.com/facebookresearch/fastText/archive/v0.1.0.zip \
> unzip v0.1.0.zip \
> cd fastText-0.1.0 \
> make 

2. Start training your model ! 
>  /fasttext skipgram -input data.txt -output model -dim 300 -minn 1 -maxn 6
