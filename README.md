#### Table of contents
1. [Introduction](#introduction)
2. [Usage for Python users](#usage)
3. [Implement in Python](#python)
4. [Experimental results](#exp)

# TriVietNLP: Identify the most popular people in a dataset <a name="introduction"></a>

## Usage for Python users  <a name="usage"></a>
### 1. Clone this Respository.
```sh
git clone https://github.com/khuongvo2305/TriVietNLP
```
### 2. Paste your datasets to `/input` folder.
### 3. Run TRIVIETNER.ipynb in jupyter notebook or google colab.
### 4. Get the results.
## Implement of TRIVIETNER.ipynb and how to modify it in Python <a name="python"></a>
### 1. Connect to Google Drive if using google colab, otherwise skip.
### 2. Extract input to /data
### 3. Clone VNCoreNLP and Facebook's FastText:
### 4. Annoate Document: 
We use VNCore NLP to segmentation, POS tagging, NER, classify and then dependency parsing raw data in data/mnt/doc/doc3/ and save as DataFrame in `output/result_labeled_test.csv`
### 5. Process Annoated Document:
  - Normalize and Clean DataFrames
  - Find the most popular people and their keywords and save in `input/4_df_input_getKeyw.csv`
### 6. Add more Profile:
  You can add more profile to our labeled profile saved in `PerfectProfile.csv` with structure: `{name:text,alias:list<text>,keyword:list<Dictionary()>,description:text}`<br>
  With: `Keyword[0]` contain kocation keywords and its count, `Keyword[1]` contain Location Person keyword its count, `Keyword[2]` contain other keywords and its count.<br>
  Example:
  `name |	alias |	keywords |	description`<br>
  `Cầu Thủ Quang Hải<br>|	[hải,quang_hải]<br>|	[{'mỹ_đình':1}, {'quang_hải': 3, 'huỳnh_anh': 3}, {'đối_mặt': 2, 'nhiều': 2, 'áp_lực': 2, 'antifan': 2, 'chuyện': 2, 'tình_cảm': 2}]<br>| Mô tả cầu thủ Quang Hải`
 ### 7. Identify Person:
 We use our heuristic to match people found in `5` to our labeled profile saved in `PerfectProfile.csv`, and display our result on console window.
## Results <a name="exp"></a>
### 1. Recognize and display the most popular people in raw datasets:
```
10 first rows:
form,label,counts
trump,the_gioi,74
ngọc,doi_song,58
phương,doi_song,39
hồ_duy_hải,phap_luat,24
joe_biden,the_gioi,22
diệu_linh,suc_khoe,21
mai_phương,doi_song,20
hải,phap_luat,19
phanxicô,the_gioi,19
```
### 2. Identify most popular people:
We use our algorithms to identify 10 documents saved in `/input` and these are our result:
```
Document 0: 
Person: sơn_tùng_m-tp
Score: 
[0.01647653 0.0009299  0.00079761 0.00163723 0.         0.00096869
 0.00207021 0.         0.00162338]
Predict: 
Perdict person: Sơn Tùng M-TP
Description: Nguyễn Thanh Tùng (sinh ngày 5 tháng 7 năm 1994), thường được biết đến với nghệ danh Sơn Tùng M-TP, là một nam ca sĩ, nhạc sĩ và diễn viên người Việt Nam.

Person: nguyễn_thanh_tùng
Score: 
[0.01647653 0.0009299  0.00079761 0.00163723 0.         0.00096869
 0.00207021 0.         0.00162338]
Predict: 
Perdict person: Sơn Tùng M-TP
Description: Nguyễn Thanh Tùng (sinh ngày 5 tháng 7 năm 1994), thường được biết đến với nghệ danh Sơn Tùng M-TP, là một nam ca sĩ, nhạc sĩ và diễn viên người Việt Nam.

-------------------------
Document 1: 
Person: sơn_tùng_m-tp
Score: 
[0.02237971 0.00138163 0.00137664 0.00106146 0.00050607 0.00115116
 0.00148515 0.         0.0018315 ]
Predict: 
Perdict person: Sơn Tùng M-TP
Description: Nguyễn Thanh Tùng (sinh ngày 5 tháng 7 năm 1994), thường được biết đến với nghệ danh Sơn Tùng M-TP, là một nam ca sĩ, nhạc sĩ và diễn viên người Việt Nam.
```
<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Reference
[VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP)<br />
[Underthesea](https://github.com/undertheseanlp/underthesea)<br />
[Vietnamese Stopwords](https://github.com/stopwords/vietnamese-stopwords)<br />
<!-- MARKDOWN LINKS & IMAGES -->
