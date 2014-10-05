def sort_jobs_by_weight_minus_length(job1, job2):
    """This sorts the jobs by weight-lenght. For ties, pick the ones with higher weight first"""
    comp = (job1[0]-job1[1]) - (job2[0]-job2[1])
    if (comp > 0):
        return 1
    elif (comp < 0):
        return -1
    elif (job1[0] > job2[0]):
        return 1
    elif (job1[0] < job2[0]):
        return -1
    else:
        return 0
def sort_jobs_by_weight_divided_by_length(job1, job2):
    """This sorts the jobs by weight/length. For ties, break arbitraryly""" 
    comp = (job1[0]/job1[1]) - (job2[0]/job2[1])
    if (comp > 0):
        return 1
    elif (comp < 0):
        return -1
    else:
        return 0
a = []
with open("jobs.txt","r") as f:
    n = int(f.readline().strip())
    for line in f.readlines():
        a.append([float(m) for m in line.split()])
#n = a[0][0]
#print n
#print a

#a.sort(cmp=sort_jobs_by_weight_minus_length, reverse=True)
a.sort(cmp=sort_jobs_by_weight_divided_by_length, reverse=True)
#print a

weight_sum = 0
time = 0
for job in a:
    time = time + job[1]
    weight_sum += job[0] * time
print "weight_sum = %d" % weight_sum
print "total process time = %d" % time
f.close()
