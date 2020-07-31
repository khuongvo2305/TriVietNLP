import pandas as pd
import sys
import numpy as np

file = r'a.csv'
df = pd.read_csv(file)

df.query('(posTag == "Ny") or (posTag == "Np") or (nerLabel == "B-ORG") or (nerLabel == "B-LOC") or (nerLabel == "B-PER") or (nerLabel == "I-ORG") or (nerLabel == "I-LOC") or (nerLabel == "I-PER") or ((posTag == "N" or posTag == "A" or posTag == "V") and nerLabel == "O")', inplace = True)

df = df.replace(r'[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ\-_]', '', regex=True)

df["form"] = df["form"].str.lower()

df_postProcessing = df
# print(df_postProcessing)
# df_postProcessing.to_csv('data_postprocessing.csv', index=False, encoding='utf-8-sig')

df_person = df\
# df.drop_duplicates()

# print(a)

df_person.query('(nerLabel == "B-PER") or (nerLabel == "I-PER")', inplace = True)

# df_temp.sort_values(by=['depLabel'], ascending=False, inplace=True)

# print(df_temp)

# def foo(x):
#     print(x[0])

# df_person.apply(lambda x: foo(x) , axis = 1)
# print(df_person)
# df_person.to_csv('z.csv', index=False, encoding='utf-8-sig')


def merge2Rows(prevRow, j, i):
    prevRow[1].form = str(prevRow[1].form) + "_" + str(j.form)
    df_person.at[prevRow[0], "form"] = prevRow[1].form


for i, j in df_person.iterrows():
    if (j.nerLabel == "I-PER"):
        merge2Rows(prevRow, j, i) 
    else:
        prevRow = [i, j]

df_person.query('(nerLabel == "B-PER")', inplace = True)
# print(df_person)
# df_person.to_csv('z.csv', index=False, encoding='utf-8-sig')

# df_temp = df_person.groupby(['form']).agg(np.size)
# df_temp.sort_values(by=['depLabel'], ascending=False, inplace=True)
# # df_person.to_csv('z.csv', index=False, encoding='utf-8-sig')
# print(df_temp["form"])


# dup = df_person.pivot_table(index="form",aggfunc={'form': np.size})
dup = df_person.groupby(['form']).size().reset_index(name="counts")
dup.sort_values(by=['counts'], ascending=False, inplace=True)
print(dup)
dup.to_csv('z.csv', index=False, encoding='utf-8-sig')


















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