# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return node
        nodeCopy = UndirectedGraphNode(node.label)
        dic = {node: nodeCopy}
        queue = [node]
        while queue:
            n = queue.pop(0)
            for neighbor in n.neighbors:
                if neighbor not in dic:
                    neighborCopy = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = neighborCopy
                    dic[n].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[n].neighbors.append(dic[neighbor])
        return nodeCopy
            
        
