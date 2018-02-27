#!/usr/bin/env python
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START import_libraries]
import random
from array import *
from collections import Counter
# [END import_libraries]

class Cont():
	"""docstring for Cont"""
	#this method is to generate an array of random numbers between a specifiable range and length  
	def generateArray(self,upp,loww,lengths):
		#it gives the option of setting the range of numbers and how many random numbers it should print
		rest=[random.randrange(upp,loww) for x in range(lengths)]
		return rest

	#this method is to get the number of occurrences of a specified element in an array.  	
	def oneElement(self, arrray, no):
		#its taking the element and checking it in the array 
		array_num = array('i', arrray)
		#this is to count how many times the  element occurs in the array
		return ("Number of occurrences of the number "+ str(no) + " in the said array: "+str(array_num.count(no)))

	#this method is to get the number of occurence of all the elements in an array  
	def uniqueElement(self,arrray):
		#create an empty list
		unique_list = []
		#for every element in the array add it to the unique list without repetition
		unique = [x for x in arrray if x not in unique_list and unique_list.append(x)]
		return (unique_list)


	#this method computes the mean of any given array.  
	def means(self, arrray):
		#the mean is the sum of the array divided by its length
		avg = sum(arrray)/len(arrray)
		return("The mean is " +str(avg))

	#this method computes the median of any given array.  
	def medians(self,arrray):
		# Input: list of numbers; Output: the "middle" number of an ordered list of #s
		sorted_x = sorted(arrray)
		length_n = len(arrray)
		middle = length_n // 2 # Integer division
		# Even numbered amount in list:
		if length_n % 2 == 0:
		 	median_even = (sorted_x[middle - 1] + sorted_x[middle]) / 2
		 	return(median_even) # Remember index 0 as 1st element.
		else:
			return(sorted_x[middle]) # Return middle number
	
	#this method computes the mode of any given array. 
	def modes(self,arrray):
		return (Counter(arrray).most_common(1))
	
	
