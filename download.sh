echo Download HotpotQA dev set
wget http://curtis.ml.cmu.edu/datasets/hotpot/hotpot_dev_fullwiki_v1.json


# multi-hop
echo Download multi-hop models results
wget -O multihop.zip https://surfdrive.surf.nl/files/index.php/s/hiNeHPTuFZ3HtEp/download?path=%2Fhybrid_retrieval_for_efficient_qa%2Fmulti-hop

unzip multihop.zip
rm multihop.zip

# single-hop
echo Download single-hop models results
wget -O singlehop.zip https://surfdrive.surf.nl/files/index.php/s/hiNeHPTuFZ3HtEp/download?path=%2Fhybrid_retrieval_for_efficient_qa%2Fsingle-hop

unzip singlehop.zip
rm singlehop.zip
