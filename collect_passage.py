#!/usr/bin/env python
# coding: utf-8

import os
import sys
import json

from tqdm import tqdm
from loguru import logger

from bsearch import bing_search


filename = sys.argv[1]
qid_query_mapping = json.load(open(filename))
cnt = 0
cnt_fail = 0

outfile = filename.replace('json','jsonl')
done_qid = set([])
if os.path.exists(outfile):
    for line in open(outfile):
        done_qid.add(json.loads(line)['qid'])

with  open(outfile, 'a+') as fout:
    for k, v in qid_query_mapping.items():
        v = v.replace('\"', '').replace('\n', '').replace("\'", '')
        if k in done_qid:
            continue
        done_qid.add(k)
        try:
            texts = bing_search(v)
        except:
            logger.error('parsing error {}'.format(v))
            continue
        if len(texts) == 0:
            cnt_fail += 1
            logger.info('Null response for {}'.format(v))
        cnt  += 1
        rv = {'query': v, 'qid': k, 'passages': texts}
        fout.write(json.dumps(rv) + '\n')
        if cnt % 10 ==0:
            logger.info('cnt: {}\tcnt_fail: {}'.format(cnt, cnt_fail))
