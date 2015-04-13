def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                # for i in m:
                #     print i
                # print "################", s1[x - 1], x, y
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    print x_longest, x_longest - longest
    return s1[x_longest - longest: x_longest]

str1 = "help"
str2 = "el"
print longest_common_substring(str1,str2)