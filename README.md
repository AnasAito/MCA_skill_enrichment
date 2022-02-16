# MCA skill enrichment (using ESCO skills)
##  ℹ️ Overview : 

- This repo contains a simple version of NESTA code to extract skills served as an independent package 
- You can find an **Example notebook**  that illustrate the enrichment of csv file containing 
job descriptions from Rekrute.com 

## 🚀 How to run 
- **Step 1** : clone the repo 
- **Step 2** : install requirements (pickle,pandas , tqdm,spacy )
- **Step 3** : install spacy and  en_core_web_sm (spacy NLP pipeline  ) using this code
```cli
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm
```
- **Step 4** : open Example.ipynb and explore it (code is documented)

## Notes : 
- Data folder contains a toy dataset parsed from rekrute before enrichment (data/rekrute_data.csv) and after (data/rekrute_data_output.csv)


