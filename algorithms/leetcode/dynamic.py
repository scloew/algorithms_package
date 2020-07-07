def totalFruit(self, tree: list[int]) -> int:
    """solution for https://leetcode.com/problems/fruit-into-baskets/"""
    if len(tree) == 1:
        return 0 if not tree[0] == 0 else 1
    fruit_counts, max_ = {}, 0
    f1, f2 = None, None
    f1_index, f2_index = None, None
    for i, v in enumerate(tree):
        #don't like the essentially copy pasted code
        #here and if else in final elif
        if f1 is None and not v == f2:
            f1 = v
            f1_index = i
        elif f2 is None and not v == f1:
            f2 = v
            f2_index = 2
        elif v not in (f1, f2):
            max_ = max(max_, fruit_counts.get(f1, 0) + fruit_counts.get(f2, 0))
            f_temp = tree[i - 1]
            fruit_counts[f_temp] = 0
            if f1 == f_temp:
                fruit_counts[f2] = 0
                fruit_counts[f1] = i - 1 - f2_index
                f2 = v
            else:
                fruit_counts[f1] = 0
                fruit_counts[f2] = i - 1 - f1_index
                f1 = v
        fruit_counts[v] = fruit_counts.get(v, 0) + 1
        if v == f1:
            f1_index = i
        else:
            f2_index = i
    return max(max_, fruit_counts.get(f1, 0) + fruit_counts.get(f2, 0))