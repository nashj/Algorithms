#!/usr/bin/env python

def levenshtein(s, t):
    # It works, but the runtime is terrible because the call tree expands rapidly 
    if (len(s) == 0): return len(t)
    if (len(t) == 0): return len(s)

    #print s, t
    return min(levenshtein(s[0:len(s)-1], t) + 1,
               levenshtein(s, t[0:len(t)-1]) + 1,
               levenshtein(s[0:len(s)-1], t[0:len(t)-1]) + (s[len(s)-1] != t[len(t)-1]) )

if __name__ == "__main__":
    assert(1==levenshtein("kitten", "sitten"))
    assert(1==levenshtein("sittin", "sitting"))
    assert(2==levenshtein("Hien", "Hidden"))
    assert(3==levenshtein("roof", "tooth"))
    print "Tests passed."


            
        
