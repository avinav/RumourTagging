'''
Created on Jul 26, 2015

@author: avinav
'''
import Tokenizer.tokenize as tk
from Graph import TweetGraph
import numpy as np

def get_term_list(phrase):
    word_list = phrase.split()
    term_list = tk.tokenize(word_list)
    return term_list

def edges_between(tweetGraph, source_name, target_name):
    source_vs = tweetGraph.graph.vs.select(name=source_name)
    target_vs = tweetGraph.graph.vs.select(name=target_name)
    n_edges = 0
#     print "--",source_name,target_name
    for source in source_vs:
        for target in target_vs:
            print "----",source,target
            n_edges += len(tweetGraph.graph.es.select(_source=source,_target=target)) 
    return n_edges

def subgraph_score(tweetGraph1, tweetGraph2):
    score = 0
    for edge in tweetGraph1.graph.es:
        sname = tweetGraph1.graph.vs[edge.source]["name"]
        tname = tweetGraph1.graph.vs[edge.target]["name"]
        if (edges_between(tweetGraph2, sname, tname) != 0):
#             print sname, tname
            score += 1
    return score

def query(text, tgMap, termMap):
    term_list = get_term_list(text)
    text_graph = TweetGraph(id = 10, term_list = term_list, termMap = termMap)
    print text_graph.graph
    score_dict = {}
    for _id, tweetGraph in tgMap.items():
        score_dict[_id] = subgraph_score(text_graph, tweetGraph)
    return score_dict

def result_tag(score_dict, docMap, thresh = -1):
    score = np.array(list(score_dict.values()))
    ind = np.argmax(score)
    if (score[ind] < thresh):
        return "NA"
    doc_id = list(score_dict.keys())[ind]
    return docMap[doc_id].name