#!/bin/bash


printf "Iris DataSet"
for i in 5 13 17 67 69 77
do

	time cat ../../data/iris.data | ./knn-mapper.py 2.3 3.4 7.8 5.4 5 , | ./knn-reducer.py ${i} > tests/output_iris_${i}.out
	
done
printf "\n\n\n\n\n"

printf "Puc Rio DataSet"
for i in 11 39 53 157 279 591
do

	time cat ../../data/dataset-har-PUC-Rio-ugulino.csv | ./knn-mapper.py 50 1.85 78 27.9 -4 88 -51 -28 22 -23 3 110 -87 -154 -109 -142 19 ';' | ./knn-reducer.py ${i} > tests/output_pucrio_${i}.out
	
done
printf "\n\n\n\n\n"

printf "Donation DataSet"
for i in 97 751 1809 2979
do

	time cat ../../data/donation/donation_all_blocks.csv | ./knn-mapper.py 38985 55678 0.42354645654 0 1 1 0 1 0 0 1 12 , | ./knn-reducer.py ${i} > tests/output_donation_${i}.out
	
done
printf "\n\n\n\n\n"

printf "Ethylene"
for i in 923 2543 3987
do

	time cat ../../data/data/ethylene_all.txt | ./knn-mapper.py 0.01 0.00 0.01 -59 -1.05 -35.2343 0.98754 -6.9843243 -29.34244 -12.545346 -4.56 59876.435 49875.5345 8876.34324 10011.423423 25768.345 22543.543453 5435.34543 7325.5234 6244.43234 19 0 | ./knn-reducer.py ${i} > tests/output_ethylene_${i}.out
	
done
printf "\n\n\n\n\n"


hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -input knn-input-ethylene -output knn-output-ethylene-3987 -mapper 'knn-mapper.py 0.01 0.00 0.01 -59 -1.05 -35.2343 0.98754 -6.9843243 -29.34244 -12.545346 -4.56 59876.435 49875.5345 8876.34324 10011.423423 25768.345 22543.543453 5435.34543 7325.5234 6244.43234 19 0' -reducer 'knn-reducer.py 3987' -file knn-mapper.py -file knn-reducer.py





