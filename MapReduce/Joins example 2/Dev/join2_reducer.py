#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input
#
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------
prev_word = "  "                #initialize previous word  to blank string
line_cnt           = 0  #count input lines
running_total=0 # initialize counting variable
for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1
    #note: for simple debugging use print statements, ie:
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item
    #-----------------------------------------------------
    # Check if its a new word and not the first line
    #   (b/c for the first line the previous word is not applicable)
    #   if so then print out list of dates and counts
    #----------------------------------------------------
    if curr_word != prev_word:
    # -----------------------
#now write out the join result, but not for the first line input
    # -----------------------
        if line_cnt>1:
            if (value_in.isdigit()):
		running_total=0
                running_total +=int(value_in)
                prev_word=curr_word
            else:
                print curr_word,running_total
                running_total=0
        else:
            if (value_in.isdigit()):
                running_total +=int(value_in)
                prev_word=curr_word
            else:
                print curr_word,running_total
		running_total=0
    else:
        if (value_in.isdigit()):
            running_total +=int(value_in)
            prev_word=curr_word
        else:
            print curr_word,running_total
	    running_total=0

