import pandas as pd
import sys
import numpy as np
import stopwords



def preprocessing(file = "result_labeled.csv"):
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
    prev[1].form = str(prev[1].form) + "_" + str(curRow.form)
    df.at[prev[0], "form"] = prev[1].form
def mergeFullNamePerson():
    df = preprocessing()
    # Merge rows to get full-name person
    for i, curRow in df.iterrows():
        if (curRow.nerLabel == "I-PER"):
            merge2Rows(df, prev, i, curRow) 
        else:
            prev = [i, curRow]
    # Query to get full-name person
    df.query('(nerLabel == "B-PER")', inplace = True)
    return df



def groupbyPersonLabel():
    df = mergeFullNamePerson()
    df.query('(nerLabel == "B-PER")', inplace = True)
    df = df.groupby(['form','label']).document.apply(list).reset_index()
    return df

groupbyPersonLabel()

