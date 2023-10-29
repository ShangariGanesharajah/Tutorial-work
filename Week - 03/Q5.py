response = input('Do you like Python? (yes/no): ').lower()
if response in ['yes', 'y', 'yeah', 'sure', 'absolutely']:
    print("You are on the right course.")
elif response in ['no', 'n', 'nope', 'not really']:
    print("You might change your mind.")
else:
    print("I did not understand your response.")