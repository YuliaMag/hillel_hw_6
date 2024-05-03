test_design_writers = [1, 3, 5]
tdw = set(test_design_writers)

test_scripters = [2, 3, 4, 6, 7, 8]
ts = set(test_scripters)

reviewers = [1, 2, 3, 9, 10]
rw = set(reviewers)

out_of_office_today = [2, 5, 6, 1]
oof = set(out_of_office_today)
# ================================== #

all_ = sorted(tdw.union(ts).union(rw).union(oof))
print("All the testers in the team: {}".format(all_))

write = sorted(ts.difference(rw).difference(tdw))
print("Testers who can only write scripts: {}".format(write))

working = sorted(ts.union(tdw).union(rw).difference(oof))
print("Testers who are at work today: {}".format(working))

today = sorted(ts.intersection(tdw).intersection(rw).difference(oof))
print("Testers who could write and review scripts, and are at work today: {}".format(today))
