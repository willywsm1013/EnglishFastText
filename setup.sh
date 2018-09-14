extract_dir=wikidata
final_output=data.txt
# download wiki dump
wget https://dumps.wikimedia.org/enwiki/20180901/enwiki-20180901-pages-articles-multistream.xml.bz2

# extract wiki from xml 
git clone https://github.com/attardi/wikiextractor.git
mkdir $extract_dir -p
python3 wikiextractor/WikiExtractor.py enwiki-20180901-pages-articles-multistream.xml.bz2 -o $extract_dir --processes 8  --no-templates

# merge extracted wiki data
python3 merge.py $extract_dir $final_output


