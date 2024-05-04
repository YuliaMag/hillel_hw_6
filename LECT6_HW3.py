# print(max(open("test.txt", "r"), key=len))
# ========================================= #
# dic_t = {}
# with open("test.txt", "r") as f:
#     for ln in f:
#         dic_t[len(ln)] = ln
# print(dic_t[sorted(dic_t)[-1]])
# ========================================= #


max_ln = " "
len_max_ln = 0
with open("test.txt", "r") as f:
    for ln in f:
        if len(ln) >= len_max_ln:
            len_max_ln = len(ln)
            max_ln = ln
    print(max_ln)


