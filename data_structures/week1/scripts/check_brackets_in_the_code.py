import sys, os, re

line = sys.stdin.readline().strip()
stack = []
index_track = []
flag = 0
for i,c in enumerate(line):
    if c in ["(","[","{"]:
        stack.append(c)
        index_track.append(i)
    elif c in [")","]","}"]:
        match = stack.pop()
        if (c==")" and match!="(") or (c=="]" and match!="[") \
           or (c=="}" and match!="{"):
            print i+1
            flag = 1
            break

    else:
        pass

if flag==0:
    if len(stack)==0:
        print "Success"
    else:
        print index_track[len(stack)-1]+1
    
    
            
        
