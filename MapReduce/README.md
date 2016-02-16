Map Reduce with Python and Java
===============================

## Introduction

for these sample projects , 

-data I worked is available in ***Inputs*** folder.

-sample code is availabel in ***Dev*** folder.

## Python Module

-For ***python*** we need not have anything `Jar` file in Java version.using following commands over unix we can make them executable.

	> chmod +x jobname_mapper.py 
	> chmod +x jobname_reducer.py 
-for testing and debugging for ***python*** code have been done as follows:

	> cat join1_File*.txt | ./jobname_mapper.py | sort | ./jobname_reducer.py

- for running of ***python*** code following ***hadoop*** commands have been used:
	hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
   		-input /user/cloudera/input \
   		-output /user/cloudera/output_new_3 \
   		-mapper /home/cloudera/jobname_mapper.py \
   		-reducer /home/cloudera/jobname_reducer.py \
   		-numReduceTasks 1
    **Note**:`Backward slash at end of line takes command to next line.`
	      Number of reducer tasks can be configured as `-numReduceTasks 1`


## Joins

**Joins example 1**

***Problem Statement***: `Acheiving inner join using two input files`

***Dev folder***
	-join1_mapper.py 
	-join1_reducer.py

***Inputs folder***
	-join1_FileA
	-join1_FileB	

**Joins example 2**

***Problem Statement***: `Acheiving inner join using multiple input files`

Two different sets of input files have been given one set files have TV channel code and TV Show name. By merging two sets of data we need to achive Total viewrs count per show.

***Dev folder***
	-join2_mapper.py 
	-join2_reducer.py

***Inputs folder***
	-join2_genchanA
	-join2_genchanB
	-join2_genchanC
	-join2_gennumA
	-join2_gennumB
	-join2_gennumC

***Output folder***
	-Total_viewer_count.txt	