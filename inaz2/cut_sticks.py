#/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def get_answer(sticks, cut_times, rank):
    # 長さの降順にソート
    sticks.sort(reverse=True)

    for i in range(cut_times):
        # 自分の棒が取れてしまえば、あとの棒は無限小でよいとみなせるので無視できる
        # 自分の棒が確保でき、かつ、これ以上分割しても長い棒が得られないなら終了
        if len(sticks) >= rank and sticks[0]/2.0 <= sticks[rank-1]:
            break
        # 一番長い棒を等分割
        sticks[0:1] = [sticks[0]/2.0] * 2
        sticks.sort(reverse=True)
        logging.debug(sticks)

    return sticks[rank-1]

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print >>sys.stderr, """Usage: python %s STICKS CUT_TIMES RANK

STICKS is comma-separated values such as '1,2,3'.
CUT_TIMES and RANK are positive integers.""" % sys.argv[0]
        sys.exit(1)
    sticks = map(float, sys.argv[1].split(','))
    cut_times = int(sys.argv[2])
    rank = int(sys.argv[3])
    print get_answer(sticks, cut_times, rank)
