## Generate 1000000 pseudorandom numbers
num = 1000000
randarr = [0] * num
m = 2**32; a = 1664525; c = 1013904223;
randarr[0] = 1037892
for i in xrange(1,num) : randarr[i] = (a * randarr[i-1] + c) % m 

for n in (10,100,1000) :
        f = open("hw2_1_tc_%d.txt" % n, 'w')
        f.write("%d\n" % n)
        randidx = 0
        for i in xrange (1,n+1) :
            for j in xrange (i+1,n+1) :
                f.write("%d %d %d\n" % (i,j,randarr[randidx])); randidx += 1
        f.close()
