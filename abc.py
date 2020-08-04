import pandas as pd
import sys
import numpy as np
import stopwords



def preprocessing(file = "result99.csv"):
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

# df_postProcessing = df
# df_postProcessing.to_csv('data_postprocessing.csv', index=False, encoding='utf-8-sig')


def merge2Rows(df, prev, i, curRow):
    prev[1].form = str(prev[1].form) + "_" + str(curRow.form)
    df.at[prev[0], "form"] = prev[1].form
def get_df_person(file = "result99.csv"):
    df = preprocessing(file)
    # Query person
    df.query('(nerLabel == "B-PER") or (nerLabel == "I-PER")', inplace = True)
    # Merge rows to get full-name person
    for i, curRow in df.iterrows():
        if (curRow.nerLabel == "I-PER"):
            merge2Rows(df, prev, i, curRow) 
        else:
            prev = [i, curRow]
    # Query to get full-name person
    df.query('(nerLabel == "B-PER")', inplace = True)
    # return df

    dup = df.groupby(['form']).size().reset_index(name="counts")
    dup.sort_values(by=['counts'], ascending=False, inplace=True)
    print(dup)

get_df_person()


# df_person = df

# df_keywords = df_person.groupby(['form']).size().reset_index(name="counts")
# dup.sort_values(by=['counts'], ascending=False, inplace=True)
# print(dup)




# # df_temp.sort_values(by=['depLabel'], ascending=False, inplace=True)

# # print(df_temp)

# # def foo(x):
# #     print(x[0])

# # df_person.apply(lambda x: foo(x) , axis = 1)
# # print(df_person)
# # df_person.to_csv('z.csv', index=False, encoding='utf-8-sig')





# dup = df_person.groupby(['form']).size().reset_index(name="counts")
# dup.sort_values(by=['counts'], ascending=False, inplace=True)
# print(dup)
# dup.to_csv('z.csv', index=False, encoding='utf-8-sig')


sw = stopwords.getStopwordsVN_ENG()
full = preprocessing()
arr = ["là", "có", "khi", "người", "được", "nhiều", "bạn", "tôi", "ngày", "phải", "nó", "đi" + "_"]
full['form'] = full['form'].apply(lambda x: ''.join([word for word in x.split() if word not in (sw + arr)]))
full['form'].replace('', np.nan, inplace=True)


full = full.dropna()
print(full)
full.to_csv('z.csv', index=False, encoding='utf-8-sig')














# from docx import *

# document = Document('path_to_your_files')
# document = "AàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬb ÁạẠăĂằẰẳẲẵẴắẮặ z𝐳𝘇𝒛𝙯"
# bolds=[]
# italics=[]
# for para in document.paragraphs:
#     for run in para.runs:
#         if run.italic :
#             italics.append(run.text)
#         if run.bold :
#             bolds.append(run.text)

# boltalic_Dict={'bold_phrases':bolds,
#               'italic_phrases':italics}

# print(boltalic_Dict)