#!/usr/bin/python

import sys
import math

# Target is the sample which we want to classify
target = list()

length = len( sys.argv )

# Attributes is the number of attributes that a "valid" object should have, An Integer must be passed before the last argument in the command line 
attributes = int( sys.argv[ length - 2 ] )

# Separator is the token which is going to be used to split each line of our dataset
separator = sys.argv[ length - 1 ]

print length
print attributes
print separator

# This function checks the type of a variable passed as an argument, It returns True when the variable can be converted into a float, otherwise, it returns False
def isnumeric( arg ):
    try:
        arg = float( arg )
    except ValueError:
        return False
    else:
        return True

# This function receives each object of our dataset as an argument and,
# gets only the attributes which can be converted into a numeric value, either int or float.
# Then, It returns an array of "valid fields"
def getValidAttrList( data=[] ):
    fields = list()
    for idx in range( len(data) - 1 ):
        if isnumeric( data[idx] ):
            fields.append( float( data[idx] ) )
    return fields

# This functions receives a token which is used as the separator argument for the split function.
# If the token happens to be a space, a tab or some other space represented by 0, we use the split function with no arguments 
def getSeparator( sep ):
	if sep=="" or sep=="0":
		return False
	return True		
	
# We populate the target list with the sample passed as an argument to our program
for i in range( 1, length - 2, 1 ):
    target.append( float( sys.argv[ i ] ) )

# Read line by line of our dataset
for line in sys.stdin:
	
	# Splits each line and populate an array called data
	if getSeparator( separator ):    
		data = line.strip().split( separator )
	else:
		data = line.strip().split( )
	
	# if the length of the object is different from the number of attributes passed as an argument, we skip this obj
	if (len(data) != attributes):
		continue

	#Sets distance as 0
	distance = 0
	
	#Gets the array of valid attributes
    	attrs = getValidAttrList( data )
        
	#if the array has length 0 is because we got a line with no numeric attributes
        if len(attrs)==0:continue;        
	
	#Computes the euclidean distance
        for idx in range( 0, len( attrs ), 1 ):
            distance += pow( ( target[idx] - float(attrs[idx])) , 2 )

        distance = math.sqrt(distance)

	#Sends the results, along with the object, to the Hadoop streaming
        print "{0}\t{1}".format( data, distance )
