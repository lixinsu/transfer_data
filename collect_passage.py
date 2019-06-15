#!/usr/bin/env python
# coding: utf-8

import os
import sys
import json

from tqdm import tqdm
from loguru import logger

from bsearch import bing_search


filename = sys.argv[1]
logger.add(filename+'.log')

qid_query_mapping = json.load(open(filename))
cnt = 0
cnt_fail = 0
# 输出文件为jsonl格式，支持中断恢复
outfile = filename.replace('json','jsonl')
done_qid = set([])
if os.path.exists(outfile):
    for line in open(outfile):
        done_qid.add(json.loads(line)['qid'])

with open(outfile, 'a+') as fout:
    for qid, query in qid_query_mapping.items():
        query = query.replace('\"', '').replace('\n', '').replace("\'", '')
        if qid in done_qid:
            continue
        try:
            texts = bing_search(query)
        except KeyboardInterrupt:
            raise
        except :
            logger.error('parsing error: {}'.format(query))
            cnt_fail += 1
            continue
        if len(texts) == 0:
            cnt_fail += 1
            logger.warning('Null response for: {}'.format(query))
            continue
        done_qid.add(qid)
        cnt += 1
        rv = {'query': query, 'qid': qid, 'passages': texts}
        fout.write(json.dumps(rv) + '\n')
        if cnt % 10 ==0:
            logger.info('cnt: {}\tcnt_fail: {}'.format(cnt, cnt_fail))
