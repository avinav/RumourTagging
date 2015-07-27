'''
Created on Jul 26, 2015

@author: avinav
'''
from Graph import TweetGraph
from Graph import graph_processing as gp
import pickle
from Extras.RunnerExcel import generate_result

data = pickle.load(open('util/rumour.p','r'))
docMap = data['docMap']
docSpace = data['docSpace']
termMap = data['termMap']
index = data['index']
search_text_list = data['search_text_list']
true_labels = data['true_labels']
tgMap = {}

for _id, doc in docMap.items():
    tgMap[_id] = TweetGraph(doc = doc,termMap = termMap)
    print tgMap[_id].graph
    
print "------------------------"

pred_labels = []
thresh = 0.1
# text = "they may shutdown phone cell"
# score_dict = gp.query(text, tgMap, termMap)
# print score_dict
counter = 0
for text in search_text_list:
    if (counter >= 3):
        break;
    score_dict = gp.query(text, tgMap, termMap)
    print score_dict
    pred_labels.append(gp.result_tag(score_dict, docMap, thresh))
    counter += 1
    

# doc_names = ['R1','R3','R4','R5','R7','NA']
# title = "Graph_" +str(thresh)
# conf_matrix, conf_matrix_string, tpr, fpr, acc = generate_result(doc_names, true_labels, pred_labels, title)
