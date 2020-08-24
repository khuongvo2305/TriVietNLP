#### Table of contents
1. [Introduction](#introduction)
2. [Usage for Python users](#usage)
3. [Implement in Python](#python)
4. [Experimental results](#exp)

# TriVietNLP: Identify the most popular people in a dataset <a name="introduction"></a>

## Usage for Python users  <a name="usage"></a>
1. Clone this Respository.
```sh
git clone https://github.com/khuongvo2305/TriVietNLP
```
2. Paste your datasets to `/input` folder.
3. Run TRIVIETNER.ipynb in jupyter notebook or google colab.
4. Get the results.
## Implement of TRIVIETNER.ipynb in Python <a name="python"></a>

1. Connect to Google Drive if using google colab, otherwise skip.
2. Extract input to /data
3. Clone VNCoreNLP and Facebook's FastText:
4. Annoate Document: Use VNCore NLP to segmentation, POS tagging, NER, classify and then dependency parsing raw data in data/mnt/doc/doc3/ and save as DataFrame in `output/result_labeled_test.csv`
5. Process Annoated Document:
  - Normalize and Clean DataFrames
  - Find the most popular people and their keywords and save in `input/4_df_input_getKeyw.csv`
6. Identify Person:
  We use our heuristic to match people found in (5.) to our labeled profile saved in PerfectProfile.csv, and display our result on console window.<br>
  You can add more profile to PerfectProfile.csv with structure: {name:text,alias:list<text>,keyword:list<Dictionary()>,description:text}<br>
  With: Keyword[0] contain kocation keywords and its count, Keyword[1] contain Location Person keyword its count, Keyword[2] contain other keywords and its count.<br>
  Example:
  name |	alias |	keywords |	description<br>
  Cầu Thủ Quang Hải<br>|	[hải,quang_hải]<br>|	[{'mỹ_đình':1}, {'quang_hải': 3, 'huỳnh_anh': 3}, {'đối_mặt': 2, 'nhiều': 2, 'áp_lực': 2, 'antifan': 2, 'chuyện': 2, 'tình_cảm': 2}]<br>| Mô tả cầu thủ Quang Hải
  
## Results <a name="exp"></a>
