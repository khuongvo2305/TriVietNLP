import pandas as pd
import sys
import numpy as np



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
    """
    a sub-function for mergeFullNamePerson()
    """
    prev[1].form = str(prev[1].form) + "_" + str(curRow.form)
    df.at[prev[0], "form"] = prev[1].form
def mergeFullNamePerson(file = "result_labeled.csv"):
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


def groupbyPersonLabel(file = "result_labeled.csv"):
    """
    groupby 'form' and 'label' to show axactly this person and the lists of documents have them
    """
    df = mergeFullNamePerson(file)
    df.query('(nerLabel == "B-PER")', inplace = True)
    df = df.groupby(['form','label']).document.apply(list).reset_index()
    return df


def classifyNewDocument(folder = "input"):
    df_spam = DataFrame()
    listFileInputs = glob.glob("*.txt")



# df = groupbyPersonLabel()
# def writeFileJson(file, x):
#     x.to_json(file, force_ascii=False)
#     # file.writelines("")
# with open('temp.json', 'w', encoding='utf-8') as file:
#     df['json'] = df.apply(lambda x: writeFileJson(file, x), axis=1)


def getKeyw():
    df = groupbyPersonLabel()
    df_all = preprocessing()
    temp = []
    keyword = dict()
    for i, j in df.iterrows():
        # temp[j.form]=pd.DataFrame()
        keyw = []
        for doc in j.document:
            df_each_doc = df_all[df_all['document']==doc]
                
            temp = df_key[df_key['nerLabel']=='B-LOC']['form'].values.ravel().tolist()
            keyw = keyw + temp
        print(keyw)


dup = df_person.groupby(['form']).size().reset_index(name="counts")
    #   df_key = df_all[df_all['document']==doc]
    #   # print(df_key[df_key['nerLabel']=='B-LOC']['form'].values)
    #   keyw = keyw + (df_key[df_key['nerLabel']=='B-LOC']['form'].values)
    # temp[j.form]=keyw
    # print(keyw) 
    # temp[j.form].append(keyw)
      # print(keyw)
  # return temp
#   return temp

getKeyw()
