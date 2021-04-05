
import math

def rabinKarp(text, patt, q):
    M = len(patt)
    N = len(text)
    hash_patt = 0
    hash_text = 0
    h=0
    
    for i in range(M):
        hash_patt += ord(patt[i])*(q**i)
        hash_text += ord(text[i])*(q**i)
       
    for i in range(0,N-M+1,1):
 
        if hash_patt==hash_text:
 
            for j in range(0,M,1):
                if text[i+j] != patt[j]:
                    break
                   
            if j==M-1:
                print("Pattern found at index "+str(i))
        
        if i<N-M:
            hash_text -= ord(text[i])
            hash_text = (hash_text//q) + (ord(text[i+M])*(q**(M-1)))    
                
    
text = "algorithmisfun"
patt = "fun"
mod = 101
rabinKarp(text, patt, mod)