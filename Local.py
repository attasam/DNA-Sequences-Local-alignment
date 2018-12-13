import numpy as np
#import sys

s1 = input("Enter Sequence 1:")
s2 = input("Enter Sequence 2:")

match=int(input("Enter Match Score: "))
mmatch=int(input("Enter Mismatch Score: "))
indel = int(input("Enter Gap Score: "))
subst_matrix = {
'A': {'A': match,'C':mmatch,'G':mmatch,'T':mmatch}, 
'C': {'A':mmatch,'C': match,'G':mmatch,'T':mmatch}, 
'G': {'A':mmatch,'C':mmatch,'G': match,'T':mmatch},
'T': {'A':mmatch,'C':mmatch,'G':mmatch,'T': match},
}

s_matrix = np.ndarray(shape=(len(s1)+1,len(s2)+1), dtype=int)
s_matrix.fill(0)
bt_matrix = np.ndarray(shape=(len(s1)+1,len(s2)+1), dtype=int)
bt_matrix.fill(3)

for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i==0 and j==0:
                continue
            bs1 = s1[i-1] 
            bs2 = s2[j-1] 
            scores = [-999,-999,-999]
            if i==0 and j > 0:
                scores[0]=0
            if j==0 and i > 0:
                scores[2]=0
            if j > 0 and i > 0:
                if bs1==bs2:
                    scores[1]=max(s_matrix[i-1,j-1]+match,s_matrix[i-1,j]+indel,s_matrix[i,j-1]+indel)
                if bs1 != bs2 and (s_matrix[i-1,j-1]+mmatch) >= (s_matrix[i-1,j]+indel) and (s_matrix[i-1,j-1]+mmatch) >= (s_matrix[i,j-1]+indel):
                    if (s_matrix[i-1,j-1]+mmatch) >= 0:
                        scores[1]=s_matrix[i-1,j-1]+mmatch
                    else:
                        scores[1]=0
                elif bs1 != bs2 and (s_matrix[i-1,j]+indel) >= (s_matrix[i-1,j-1]+mmatch) and (s_matrix[i-1,j]+indel) >= (s_matrix[i,j-1]+indel):
                    if (s_matrix[i-1,j]+indel) >= 0:
                       scores[2]=s_matrix[i-1,j]+indel
                    else:
                        scores[2]=0
                    
                elif bs1 != bs2 and (s_matrix[i,j-1]+indel) >= (s_matrix[i-1,j-1]+mmatch) and (s_matrix[i,j-1]+indel) >= (s_matrix[i-1,j]+indel):
                    if (s_matrix[i,j-1]+indel) >= 0:
                      scores[0]=s_matrix[i,j-1]+indel
                    else:
                        scores[0]=0
                        
                    
                    
                    
            best = max(scores)
            s_matrix[i,j]=best
            for k in range(3):
                if scores[k] == best:
                    bt_matrix[i,j] = k
print("Dynamic programming matrix")
print(s_matrix)     
