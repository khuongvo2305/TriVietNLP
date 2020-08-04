import glob
from nltk.corpus import stopwords

# Get stopwords Vi & Eng
def getStopwordsVN(arrayOfFileName):
    stopwords_VN = list()
    for fileName in arrayOfFileName:
        f = open(fileName, "r", encoding="utf-8")
        for each_word in f:
            stopwords_VN.append(f.readline().split('\n')[0])
        f.close()
    return stopwords_VN

def getStopwordsVN_ENG():
    # Return a array which has list of words
    stopwordsVN_fileNames = glob.glob("vietnamese-stopwords-dash.txt")
    stopwordsVN = getStopwordsVN(stopwordsVN_fileNames)
    stopwordsENG = stopwords.words('english')
    return stopwordsVN + stopwordsENG 