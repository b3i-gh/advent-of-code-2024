from collections import defaultdict
import networkx as nx

def main(input):
    ans1 = ans2 = 0

    g = defaultdict(set)
    for l in input.strip().split("\n"):
        a,b = l.split("-") 
        g[a].add(b)
        g[b].add(a)

    # part 1
    for a in g.keys():
        ag = a.startswith("t")
        for b in g.keys():
            if b not in g[a]:
                continue
            bg = b.startswith("t")
            if a<= b:
                continue
            cs = g[a] & g[b]
            for c in cs:
                if c > a and c > b:
                    if ag or bg or c.startswith("t"):
                        ans1 += 1

    # part 2
    g = nx.Graph()
    for l in input.strip().split("\n"):
        a,b = l.split("-") 
        g.add_edge(a,b)
        g.add_edge(b,a)

    maxc = ()

    for c in nx.find_cliques(g):
        if len(c) > len(maxc):
            maxc = c
            ans2 = ",".join(sorted(maxc))
    return ans1, ans2