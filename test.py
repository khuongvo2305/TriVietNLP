from vncorenlp import VnCoreNLP
import pandas as pd
annotator = VnCoreNLP(address="http://127.0.0.1", port=58644) 

# Input 

text = """Cách đây ít giờ đồng hồ, BXH Billboard Social 50 đã công bố 50 thứ hạng trong tuần lễ vừa qua, hoàn toàn bất ngờ khi Sơn Tùng M-TP đã lọt vào BXH này ở vị trí thứ 28 - thứ hạng ngay dưới TWICE và đứng trên cả MONSTA X! 
Thành tích đáng tự hào này đang gây xôn xao không nhỏ khắp các trang mạng xã hội, tiếp tục góp thêm vào cơn mưa thành tích quốc tế mà Sơn Tùng M-TP mang về cho Vpop.
Đình Khương đẹp trai vãi.
Tùng Sơn mới từ Mỹ về.
Nguyễn Thị Nguyễn Thị chào Nguyễn Tùng Sơn.
"""

# To perform word segmentation, POS tagging, NER and then dependency parsing
annotated_text = annotator.annotate(text)   

# To perform word segmentation only
# word_segmented_text = annotator.tokenize(text)

# print(annotated_text)


def readFile:
    





df = pd.DataFrame()
s = annotated_text
for i in range(len(s['sentences'])):
    for x in [s['sentences'][i]]:
    # print(x)
    # for y in x:
        df = df.append(pd.DataFrame(list(x)), True)
# print(df.describe)
print(df.query('posTag == "Np"'))
# Drop : 2 Np gần nhau 
print(df)
