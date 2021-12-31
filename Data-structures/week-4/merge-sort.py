'''
We have discussed sorting algorithm in the class. Implement the same algorithm using any of the languages like C/Python. Given a group of unordered elements. Design an algorithm/pseudocode based on divide and conquer to make the elements in to sorted list. Write all your observations. Eloborate the testcases.
Note: Use the Logic discussed in the class
Algorithm as below
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
Test case-1
Enter number of Elements 
12
Apply the process of merge sort and sort the following list of elements:

Mar, May, Nov, Aug, Apr, Jan, Dec, Jul, Feb, Jun, Oct, Sep
Test case-2
Enter number of Elements 
6
Enter array of elements
12,45,10,33,55,50
Sorted array is 
10,12,33,45,50,55
'''
# Program:
def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]


	i = 0
	j = 0
	k = l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1


def mergeSort(arr, l, r):
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


arr2 = [12,45,10,33,55,50]
n2 = len(arr2)
mergeSort(arr2, 0, n2-1)
print("Sorted array: ",arr2)

'''
Output:

Sorted array: [10, 12, 33, 45, 50, 55]
'''
