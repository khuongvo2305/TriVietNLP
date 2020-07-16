from vncorenlp import VnCoreNLP
annotator = VnCoreNLP(address="http://127.0.0.1", port=58644) 

# Input 
text = """Cách đây ít giờ đồng hồ, BXH Billboard Social 50 đã công bố 50 thứ hạng trong tuần lễ vừa qua, hoàn toàn bất ngờ khi Sơn Tùng M-TP đã lọt vào BXH này ở vị trí thứ 28 - thứ hạng ngay dưới TWICE và đứng trên cả MONSTA X! 
Thành tích đáng tự hào này đang gây xôn xao không nhỏ khắp các trang mạng xã hội, tiếp tục góp thêm vào cơn mưa thành tích quốc tế mà Sơn Tùng M-TP mang về cho Vpop.
Đình Khương đẹp trai vãi.
Tùng Sơn mới từ Mỹ về.
"""

# To perform word segmentation, POS tagging, NER and then dependency parsing
annotated_text = annotator.annotate(text)   

# To perform word segmentation only
# word_segmented_text = annotator.tokenize(text)

print(annotated_text)

# print(word_segmented_text)
