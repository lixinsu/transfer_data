#!/usr/bin/env python
# coding: utf-8

import json

part = 4

filename  = 'qid_query_mapping.json'
qid_query = json.load(open(filename))
print('Total {}'.format(len(qid_query)))
collected_qids = set([json.loads(line)['qid'] for line in open('qp.jsonl')])
for k in list(qid_query.keys()):
    if k in collected_qids:
        qid_query.pop(k)

print('Under process {}'.format(len(qid_query)))
qid_query_list = list(qid_query.items())
step =int( (len(qid_query) + part - 1 )  / part)
for p in range(part):
    sub_file = filename + '.' + str(p)
    json.dump(dict(qid_query_list[p*step: (p+1)*step]), open(sub_file, 'w'), indent=2)




