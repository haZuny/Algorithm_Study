n, m = map(int, input().split())

ls = sorted(list(map(int, input().split())))

searched = set()

def bt(seq, selected_idx):
    global m
    if len(seq) == m:
        s = ' '.join(list(map(str, seq)))
        if s not in searched: print(s);searched.add(s);
        return
    for i, v in enumerate(ls):
        if i not in selected_idx: bt(seq+[v], selected_idx.union(set([i])))

bt([], set())
