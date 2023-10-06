from typing import List
from collections import deque 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        nodes = {}
        order = []

        for node_id in range(numCourses):
            nodes[node_id] = {'in': 0, 'out': set()}
        
        for node_id, pre_id in prerequisites:
            nodes[node_id]['in'] += 1
            nodes[pre_id]['out'].add(node_id)
        
        for node_id in nodes.keys():
            if nodes[node_id]['in'] == 0:
                q.append(node_id)
        
        while q:
            node_id = q.pop()
            for pre_id in nodes[node_id]['out']:
                nodes[pre_id]['in'] -= 1
                if nodes[pre_id]['in'] == 0:
                    q.append(pre_id)
            order.append(node_id)
            
        for node_id in nodes.keys():
            if nodes[node_id]['in']:
                return False
        
        return True