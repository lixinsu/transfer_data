#!/usr/bin/env python
# coding: utf-8

import json

from bsearch import bing_search


def load_data(filename):
    qid_query_mapping = {}
    qid_query_mapping_2 = {}
    for line in open(filename):
        data = line.strip().split('\t')
        if len(data) != 6:
            print(data)
            continue
        qid_query_mapping[data[1]] = data[3]
        qid_query_mapping_2[data[2]] = data[4]
    print(len(qid_query_mapping))
    print(len(qid_query_mapping_2))
    return qid_query_mapping, qid_query_mapping_2


qid_query_mapping, qid_query_mapping_2 = load_data('train.tsv')
qid_query_mapping.update( qid_query_mapping_2)
print(len(qid_query_mapping))
json.dump(qid_query_mapping, open('qid_query_mapping.json', 'w'), indent=2)

