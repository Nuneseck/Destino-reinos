import random

options = {
    "A": ["A1", "A2", "A3"],
    "B": ["B1", "B2", "B3"],
    "C": ["C1", "C2", "C3"]
}

# Display the available options
print("Options:")
print("A - Option A")
print("B - Option B")
print("C - Option C")

# Prompt the user for their choice
choice = input("Choose an option (A, B, or C): ")

# Check if the chosen option is valid
if choice in options:
    sub_options = options[choice]
    
    # Prompt the user for the number of times to generate sub-options
    num_times = int(input("Enter the number of times to generate the sub-option: "))
    
    # Generate and display the sub-options
    for _ in range(num_times):
        random_sub_option = random.choice(sub_options)
        print("Random sub-option:", random_sub_option)
else:
    print("Invalid option. Please choose A, B, or C.")
