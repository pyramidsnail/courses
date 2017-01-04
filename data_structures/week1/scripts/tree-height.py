# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.max_depth_n = None
                self.depth_n = [None]*self.n
                # self.nodes = {}
                # for i, num in enumerate(self.parent):
                #         if not num in self.nodes:
                #                 self.nodes[num] = [i]
                #         else:
                #                 self.nodes[num].append(i)

                # self.height = 1

        def max_depth(self):
                if self.max_depth_n==None:
                        for idx, parent in enumerate(self.parent):
                                depth = self.get_depth(idx)
                                if depth > self.max_depth_n:
                                        self.max_depth_n = depth
                return self.max_depth_n
        def get_depth(self, idx):
                if not self.depth_n[idx] == None:
                        return self.depth_n[idx]
                else:
                        parent_n = self.parent[idx]
                        if parent_n == -1:
                                self.depth_n[idx] = 1
                        else:
                                self.depth_n[idx] = self.get_depth(parent_n)+1
                        return self.depth_n[idx]
                                
                

        # def compute_height(self, father):
        #         if not father in self.nodes:
        #                 return self.height
        #         else:
        #                 self.height = self.height+1
        #                 for child in self.nodes[father]:
        #                         return self.compute_height(child)
                
        #         # Replace this code with a faster implementation
        #         # maxHeight = 0
        #         # for vertex in range(self.n):
        #         #         height = 0
        #         #         i = vertex
        #         #         while i != -1:
        #         #                 height += 1
        #         #                 i = self.parent[i]
        #         #         maxHeight = max(maxHeight, height);
        #         # return maxHeight;

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.max_depth())

threading.Thread(target=main).start()
