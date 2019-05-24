#! /usr/bin/env python

import fileinput

old_key = None
max_value = 0

for line in fileinput.input():

	data = line.strip().split('\t')

	if(len(data) != 2):
		continue

	current_key, current_value = data


	if old_key and old_key != current_key:
		print("{0}\t{1}".format(old_key,max_value))
		old_key = current_key
		max_value = 0

	if old_key is None:
		old_key = current_key
		
	if float(current_value) > float(max_value):
			max_value = current_value

if old_key == current_key:
	print("{0}\t{1}".format(old_key,max_value))