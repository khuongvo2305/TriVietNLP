pip3 install vncorenlp
# # To perform word segmentation, POS tagging, NER and then dependency parsing
#     $ vncorenlp -Xmx2g <FULL-PATH-to-VnCoreNLP-jar-file> -p 9000 -a "wseg,pos,ner,parse"
    
#     # To perform word segmentation, POS tagging and then NER
#     # $ vncorenlp -Xmx2g <FULL-PATH-to-VnCoreNLP-jar-file> -p 9000 -a "wseg,pos,ner"
#     # To perform word segmentation and then POS tagging
#     # $ vncorenlp -Xmx2g <FULL-PATH-to-VnCoreNLP-jar-file> -p 9000 -a "wseg,pos"
#     # To perform word segmentation only
#     # $ vncorenlp -Xmx500m <FULL-PATH-to-VnCoreNLP-jar-file> -p 9000 -a "wseg"
vncorenlp -Xmx2g F:\\Named Entity Recognition for Vietnamese\\TriVietNLP\\VnCoreNLP\\VnCoreNLP-1.1.1.jar -p 58644 -a "wseg,pos,ner,parse"