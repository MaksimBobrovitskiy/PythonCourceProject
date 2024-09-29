def partitionString(self, s):
    cur_set = set()
    ans = 0
    for i in s:
        if i in cur_set:
            cur_set = set()
            ans += 1
        cur_set.add(i)

    return ans + 1