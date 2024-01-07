def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
    
  return subsets

def decode(message_file):
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract words and corresponding numbers
    word_number_pairs = [line.split() for line in lines]
    # Convert numbers to integers and sort it
    numbers = [int(pair[0]) for pair in word_number_pairs]
    numbers.sort()
    # Convert numbers to Pyramid with help of create_staircase function
    pyramid = create_staircase(numbers)
    #Getting last number of the Pyramid row
    last_numbers = []
    for row in pyramid:
        last_numbers.append(row[len(row)-1])
    # Extract words based on the pyramid structure
    res = []
    for num in last_numbers:
        for word in word_number_pairs:
            if str(num) == word[0]:
                res.append(word[1])

    # Return the decoded message as a string
    decoded_message = ' '.join(res)
    return decoded_message

# Example usage
message_file = './coding_qual_input.txt'  # Replace with the actual file path
decoded_message = decode(message_file)
print(decoded_message)