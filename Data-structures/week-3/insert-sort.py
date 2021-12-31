'''
Two friends Reema and Rita decide to play cards. But Reema doesn't know to play the cards. So Rita decides to teach her how to play cards. Rita distributes 13 cards to each other which are in unsorted order and teaches her how to make set with the cards without considering the symbols. 
Rita first takes two cards and checks which card has the lesser number and the card with the least number is put first and larger at second.  
She takes third card and checks it with second card. If the third card number is less than the second card she inserts the third card at the second position and checks newly inserted second card with the first card. If the newly inserted second card number is less than the first card, she inserts the second card at the first place and this goes on till all the cards get sorted. 
Rita finally learns how to order the cards. 
  
Write a program to perform insertion sort on an array of n elements. 
  
Input Format: 
Input consists of n+1 integers. The first integer corresponds to n, the number of elements in the array. The next n integers correspond to the elements in the array. 
  
Output Format: 
Refer sample output for formatting specs
'''

# Program:
def insertion_sort(arr):
    for i in range(1,len(arr)):
        t = arr[i]
        j = i - 1
        
        while j >= 0 and t < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = t
    return arr

n = int(input('Enter length of the array: '))
p = list(map(int,input("enter elemnets: ").split()[:n]))
print("Sorted array: ",insertion_sort(p))

'''
Output:
Enter length of the array: 5
enter elemnets: 6 4 3 2 5
Sorted array:  [2, 3, 4, 5, 6]
'''
