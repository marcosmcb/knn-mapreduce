#!/usr/bin/python
import sys


neighbours = list()
data = list()

# Sets the number of the K nearest neighbours
K = int( sys.argv[ 1 ] )
idx = 0

#Initializes the neighbours and data lists
for x in range( K ):
    neighbours.append( -1 )
    data.append( None )

# Method used to get the Highest value of our neighbours list
def getMaxElement( neighbours=[] ):
    max_el = posi = -1
    for x in range( K ):     
        if neighbours[ x ] > max_el:    
            max_el = neighbours[ x ]
            posi = x    

    return (max_el, posi)

# Read line by line from the streaming
for line in sys.stdin:
    # Process each line
    content = line.strip().split("\t")
	
	# As we have a 'key' value pair object, if the size is different from 2, we skip it
    if len( content ) != 2:
        # Something has gone wrong. Skip this line.
        continue
	
	# Gets the actual object
    fields = content[0]    
	
	# Gets the distance value
    distance = float( content[1] )
	
	# Selects the K Nearest Neighbours
    if idx < K:
        neighbours[ idx ] =  distance 
        data[ idx ] = fields
        idx += 1
    else:
        max_el , posi = getMaxElement( neighbours )
        if max_el > distance:
            neighbours[ posi ] = distance
            data[ posi ] = fields


# Prints the list of the K Nearest Neighbours
print "Set of the " + str(K) + " neighbours: \n"
for x in range( K ):
    print data[ x ]
    print neighbours[x]
    print "\n"
