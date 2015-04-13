#!/usr/bin/env python

## http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)

########## Running the Mapper and Reducer ######################

# Test your code (cat data | map | sort | reduce)

# # very basic test
# hduser@ubuntu:~$ echo "foo foo quux labs foo bar quux" | /home/hduser/mapper.py
# foo     1
# foo     1
# quux    1
# labs    1
# foo     1
# bar     1
# quux    1

# hduser@ubuntu:~$ echo "foo foo quux labs foo bar quux" | /home/hduser/mapper.py | sort -k1,1 | /home/hduser/reducer.py
# bar     1
# foo     3
# labs    1
# quux    2