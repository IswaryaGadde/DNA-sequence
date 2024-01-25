def find_longest_sequance(dna_sequence):
    #Iswarya (02-10-2023): Declaring variables 
    max_sequance_length = 0 
    current_sequance_length = 1  
    max_sequance_start = 0 
    current_sequance_start = 0 

    for i in range(1, len(dna_sequence)):
        #Iswarya (02-10-2023): Comparing letters in the string 
        if dna_sequence[i] == dna_sequence[i - 1]:
            current_sequance_length += 1
        else:
            if current_sequance_length > max_sequance_length:
                max_sequance_length = current_sequance_length
                max_sequance_start = current_sequance_start
            current_sequance_start = i
            current_sequance_length = 1

    #Iswarya (02-10-2023): Compare lengths to find the longest DNA sequnce 
    if current_sequance_length > max_sequance_length:
        max_sequance_length = current_sequance_length
        max_sequance_start = current_sequance_start

    max_sequance_end = max_sequance_start + max_sequance_length - 1
    return max_sequance_length, max_sequance_start, max_sequance_end

#Iswarya (02-10-2023): Input DNA sequence 
input_sequence = input("Enter a DNA sequence: ")

#Iswarya (02-10-2023): Method to find the longest sequance
length, start, end = find_longest_sequance(input_sequence)

#Iswarya (02-10-2023): Printing the results 
print("Length of the longest sequance:", length)
print("Start position of the longest sequance:", start + 1)  # Iswarya (02-10-2023): Adding 1 to start position from 1-based index 
print("End position of the longest sequance:", end + 1)  # Iswarya (02-10-2023): Adding 1 to end position to make it 1-based index 
