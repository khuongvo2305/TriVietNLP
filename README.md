#### Table of contents
1. [Introduction](#introduction)
2. [Usage for Python users](#usage)
3. [Implement in Python](#python)
4. [Experimental results](#exp)

# TriVietNLP: Identify the most popular people in a dataset <a name="introduction"></a>

## Usage for Python users  <a name="usage"></a>
1. Clone this Respository.
2. Save datasets to `/input` folder.
3. Run TRIVIETNER.ipynb in jupyter notebook or google colab.
4. Get the results.
## Implement in Python <a name="python"></a>

1. Connect to Google Drive if using google colab, otherwise skip.
```
from google.colab import drive
drive.mount('/content/drive')
```
2. Extract input to /data

```
import tarfile
def extracttar(fname):
  if fname.endswith("tar.gz"):
      tar = tarfile.open(fname, "r:gz")
      tar.extractall()
      tar.close()
  elif fname.endswith("tar"):
      tar = tarfile.open(fname, "r:")
      tar.extractall()
      tar.close()
extracttar("/data/doc3.tar.gz")
```
3. Clone VNCoreNLP and Facebook's FastText:
```
!git clone https://github.com/vncorenlp/VnCoreNLP
!git clone https://github.com/facebookresearch/fastText.git
%cd fastText
!pip install .
%cd ..

```
4. Install Libraries
```
!pip3 install vncorenlp
!pip3 install underthesea
!underthesea download tc_general
!underthesea download tc_bank
!pip install unidecode
!pip3 install mechanize

```
5. Import Libraries
```
import fastText
import unidecode
from underthesea import classify
from vncorenlp import VnCoreNLP
import pandas as pd
import glob
import sys
import numpy as np
from collections import Counter 
```
6. Annoate Document: Use VNCore NLP to segmentation, POS tagging, NER, classify and then dependency parsing raw data in data/mnt/doc/doc3/ and save as DataFrame in output/result_labeled_test.csv
```
# annotator = VnCoreNLP(address="http://127.0.0.1", port=58644) 
def annotateDocument(folderInput = 'data/mnt/doc/doc3/', folderOutput = 'output/'):
  annotator = VnCoreNLP("VnCoreNLP/VnCoreNLP-1.1.1.jar", annotators="wseg,pos,ner,parse", max_heap_size='-Xmx2g')
  dataurl = glob.glob(folderInput + "/*.txt")
  df = pd.DataFrame()
  j = -1
  for url in dataurl:
    j = j + 1
    text = open(url).read()
    try:
      s = annotator.annotate(text)
      for i in range(len(s['sentences'])):
        for x in [s['sentences'][i]]:
          df_temp = pd.DataFrame(list(x))
          if not ((df_temp.nerLabel == 'B-PER').any()):
            continue
          label = classify(text)
          df_temp.insert(0, "document", j)
          df_temp.insert(1,"label",label[0])
          df = df.append(df_temp,True)   
    except:
      pass
  df.to_csv(folderOutput + "result_labeled.csv", index = False, encoding='utf-8-sig')
  return df

annotateDocument()

```
7. Processing:
```
def preprocessing(file = r'/output/result_labeled.csv'):
    """
    input: filename 

    output: dataframe after preprocessing
    """
    df = pd.read_csv(file)
    # Filter to get Noun, Verb, Object, Location/Organization, Person.
    df.query('(posTag == "Ny") or (posTag == "Np") or (nerLabel == "B-ORG") or (nerLabel == "B-LOC") or (nerLabel == "B-PER") or (nerLabel == "I-ORG") or (nerLabel == "I-LOC") or (nerLabel == "I-PER") or ((posTag == "N" or posTag == "A" or posTag == "V") and nerLabel == "O")', inplace = True)
    # Filter unicode
    df = df.replace(r'[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ\-_]', '', regex=True)
    # Lower case
    df["form"] = df["form"].str.lower()
    return df


def merge2Rows(df, prev, i, curRow):
    """
    a sub-function for mergeFullNamePerson()
    """
    prev[1].form = str(prev[1].form) + "_" + str(curRow.form)
    df.at[prev[0], "form"] = prev[1].form
def mergeFullNamePerson(file = r'/output/result_labeled.csv'):
    """
    return a dataframe which gets fullname person by merging some rows which have firstname and lastname person
    """
    df = preprocessing(file)
    # Merge rows to get full-name person
    for i, curRow in df.iterrows():
        if (curRow.nerLabel == "I-PER"):
            merge2Rows(df, prev, i, curRow) 
        else:
            prev = [i, curRow]
    # Query to get full-name person
    df.query('(nerLabel == "B-PER")', inplace = True)
    return df


def groupbyPersonLabel(file = r'/output/result_labeled.csv'):
    """
    groupby 'form' and 'label' to show axactly this person and the lists of documents have them
    """
    df = mergeFullNamePerson(file)
    df.query('(nerLabel == "B-PER")', inplace = True)
    df = df.groupby(['form','label']).document.apply(list).reset_index()
    return df

def getKeyw_doc(file = r'/output/result_labeled.csv'):
    
    df = pd.read_csv('input/processing/3_df_input_mergeFullNamePerson.csv')
    df_all = pd.read_csv('input/processing/2_df_input_preprocessing.csv')
    temp = []
    description = []

    for doc in range(df_all['document'].max()+1):
        keywLO = []
        keywP = []
        keyw = []
        key = []
        df_key = df_all[df_all['document']==doc]
        totalscore = 0
        for m,n in df_key.iterrows():
            if (n.nerLabel =='B-LOC' or n.nerLabel =='B-ORG'or n.nerLabel =='I-LOC' or n.nerLabel =='I-ORG'):
                keywLO = keywLO + [n.form]
                totalscore += 2
            elif (n.nerLabel =='B-PER'or n.nerLabel=='I-PER'):
                keywP = keywP + [n.form]
                totalscore += 3
            else:
                keyw = keyw +[n.form]
                totalscore += 1
        my_dict = [{i:keywLO.count(i)*2/totalscore for i in keywLO},{i:keywP.count(i)*3/totalscore for i in keywP},{i:keyw.count(i)/totalscore for i in keyw}]
        temp = temp + [my_dict]
    keyw_in_doc = []
    for i,j in df.iterrows():
        keyw_in_doc = keyw_in_doc + [temp[j.document]]
    df.insert(8,"keywords",keyw_in_doc)
    return df
```
8. Export Processing File:

```
def processingDoc(folderInput = 'input/', folderOutput = 'output/'):
  df = pd.DataFrame()
  df = annotateDocument(folderInput, folderOutput)
  if (df.empty):
    print("Không có tên người")
    return
  df.to_csv("input/processing/1_df_input.csv", index = False, encoding='utf-8-sig')
  df = preprocessing(file = r'input/processing/1_df_input.csv')
  df.to_csv("input/processing/2_df_input_preprocessing.csv", index = False, encoding='utf-8-sig')
  df = mergeFullNamePerson(file = r'input/processing/1_df_input.csv')
  df.to_csv("input/processing/3_df_input_mergeFullNamePerson.csv", index = False, encoding='utf-8-sig')
  df = getKeyw_doc()
  df.loc[df.astype(str).drop_duplicates(subset=['document','form']).index].to_csv("input/processing/4_df_input_getKeyw.csv", index = False, encoding='utf-8-sig')
  return df
df = processingDoc()

```
9. Identify Person:
```
# -*- coding: utf-8 -*-
from collections import Counter 
import ast
import math


def score(df_train, df_test_each_person):
    test_person = df_test_each_person.form
    test_keywords = ast.literal_eval(df_test_each_person.keywords)
    test_keywords = dict(Counter(test_keywords[0]) + Counter(test_keywords[1]) + Counter(test_keywords[2]))
    # print(df_train)

    result = np.zeros(int(df_train.shape[0]))

    for i, row in df_train.iterrows():
        train_alias = row.alias.replace('[', '').replace(']', '').split(",")
        train_keywords = ast.literal_eval(row.keywords)
        total = 0
        if(train_keywords[0]):
            total += sum(train_keywords[0].values())*2
        if(train_keywords[1]):
            total += sum(train_keywords[1].values())*3
        if(train_keywords[2]):
            total += sum(train_keywords[2].values())
        # print(total)
        per = 0
        if test_person in train_alias:
            # result[i] += 1
            # print(test_person)

            per += 1
        for test_keyword in test_keywords.keys():
            result[i] += int(Counter(train_keywords[0])[test_keyword])*test_keywords[test_keyword] 
            result[i] += int(Counter(train_keywords[1])[test_keyword])*test_keywords[test_keyword] 
            result[i] += int(Counter(train_keywords[2])[test_keyword])*test_keywords[test_keyword]
        # print(per)
        result[i]=(result[i]/total)*math.exp(per)
    # print(result)
    return result



def classifyDoc():
    attribute = []
    df_train = pd.read_csv('PerfectProfile.csv')
    df_test = pd.read_csv('input/processing/4_df_input_getKeyw.csv')

    for i in range(0, df_train.shape[0] + 1): # nRow in df_train
        eachDoc = df_test.query(str('(document == ' + str(i) + ')'), inplace = False)
        print("Document " + str(i) + ": ")
        for iPerson, j in eachDoc.iterrows():
            scorePerson = score(df_train, j) 
            predictPerson = df_train.loc[np.where(scorePerson == np.amax(scorePerson))] # a row in df_train
            print("Person: " + j.form)
            print("Score: ")
            print(scorePerson) # array
            print("Predict: ")
            print("Perdict person: " + str(predictPerson.name.values[0]))
            print("Description: " + str(predictPerson.description.values[0]))
            print()
        print("-------------------------")

classifyDoc()
```
## Results <a name="exp"></a>
