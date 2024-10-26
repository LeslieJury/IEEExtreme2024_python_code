import numpy as np



def swap_digits(digit_array, swap_times):
    
    count = 0 # count for how many times we swap
    sorted_digit_array = np.sort(digit_array)[::-1]  # Get the sorted array. use i to locate the biggest, 2nd, 3rd, and etc. value in the array

    # all_max_indices = np.where(digit_array == max_value)[0]  # [0] extracts indices as a 1D array
        
    # Issue: What is the best way to "swap"?
    # We can use the sorted array to locate the position of the max value in the original array
        
    # for i, ori_value in enumerate(digit_array):
    #     for j, sor_value in enumerate(sorted_digit_array): # Get the value in the descending order
    
    for i in range(len(digit_array)):
        if count == swap_times:
            break
        elif digit_array[i] == sorted_digit_array[i]: #  if the value is already in the correct position
            continue
        else:
            #digit_array[i] != sorted_digit_array[i]: # if the value is not in the correct position -- I think  this is not necessary
            
            # Get the indices where the current maximum value appears
            indices = np.where(digit_array == sorted_digit_array[i])[0]
            # Get the rightmost index if there are multiple occurrences
            j = indices[-1]
            
            # Only swap if the indices are different
            if i != j:
                # For NumPy arrays, we need to use a different swap method
                temp = digit_array[i].copy()
                digit_array[i] = digit_array[j]
                digit_array[j] = temp
                count += 1
            
    return digit_array


def main():
    # Get input setups
    value_and_swap = list(input().split(" "))
    value = value_and_swap[0] # str
    swap = int(value_and_swap[1]) # swap is the value to be swapped

    digit_array = np.array(list(map(int, value))) # Convert to an array of integers   
    
    #  Swap the value in the array
    result = swap_digits(digit_array, swap)

    # Print the result
    for i in result:
        print(i, end="")
            
if  __name__ == "__main__":
    main()





            
            
                

        
            
    
 
