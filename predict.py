# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import glob
from collections import Counter 
import ast


def score(df_train, df_test_each_person):
    test_person = df_test_each_person.form
    test_keywords = ast.literal_eval(df_test_each_person.keywords)
    test_keywords = dict(Counter(test_keywords[0]) + Counter(test_keywords[1]) + Counter(test_keywords[2]))

    result = np.zeros(int(df_train.shape[0]))

    for i, row in df_train.iterrows():
        train_alias = row.alias
        # train_keywords = ast.literal_eval(row.keywords)
        # print(type(train_keywords))
        if test_person in train_alias:
            result[i] += 10
        
        
        


    return 0



def classifyDoc():
    attribute = []
    df_train = pd.read_csv('PerfectProfile.csv')
    df_test = pd.read_csv('input/4_df_input_getKeyw-2.csv')
    # df_test = np.zeros((len(dataurl), 10, int(df_train.shape[0])))
    n_doc = range(0, df_train.shape[0] + 1)
    # print(doc)
    for i in n_doc:
        eachDoc = df_test.query(str('(document == ' + str(i) + ')'), inplace = False)
        for i,j in eachDoc.iterrows():
            attribute.append([      j.form, j.keywords, score(df_train, j)      ])
            

    # for url in dataurl:
    #     pd_temp = pd.read_csv(url)
    #     for a, b in pd_temp.iterrows():
    #         pass
    #     i = i + 1

classifyDoc()