#/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import heapq

def can_make_longer_sticks(sticks, cut_times, rank, target):
    # max_heapを構築
    sticks = [(-x, x) for x in sticks]
    heapq.heapify(sticks)

    # rank番目がtargetより長ければOK
    if len(sticks) >= rank and sorted(sticks)[rank-1][1] >= target:
        return True

    for i in range(cut_times):
        # 最長の棒がtarget以下の長さならこれ以上切れない
        y = sticks[0][1]
        if y <= target:
            break
        # 最長の棒から長さtargetの棒を切り出す
        heapq.heapreplace(sticks, (-(y-target), y-target))
        heapq.heappush(sticks, (-target, target))
        # 一回切るたびに判定
        if len(sticks) >= rank and sorted(sticks)[rank-1][1] >= target:
            return True

    return False

def binary_search(min_max, judge_func):
    (a, b) = min_max
    # 小数点以下第2位まで求める
    while round(a,2) != round(b,2):
        mid = (a+b)/2.0
        if judge_func(mid):
            (a, b) = (mid, b)
        else:
            (a, b) = (a, mid)
        print >>sys.stderr, (a, b)
    return round(a,2)

def get_answer(sticks, cut_times, rank):
    # 二分探索
    return binary_search((0, 1e9), lambda x: can_make_longer_sticks(sticks, cut_times, rank, x))

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
