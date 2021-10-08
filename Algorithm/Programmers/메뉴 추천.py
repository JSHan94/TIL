from itertools import combinations
import collections

def solution(orders, course):
    res = []
    
    for course_size in course:
        order_combination = []
        for order in orders:
            order_combination += combinations(sorted(order), course_size)
        most_ordered = collections.Counter(order_combination).most_common()
        #print(course_size, order_combination)
        
        res += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]
    return [''.join(v) for v in sorted(res)]
