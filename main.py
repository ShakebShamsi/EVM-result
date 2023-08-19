# Initialize vote counters
votes_A = 0
votes_B = 0
votes_C = 0

# Total number of votes
total_votes = 21

# Take votes as input from users
for i in range(total_votes):
    vote = input(f"Voter {i + 1}. \n 1.Candidate A \n 2.Candidate B \n 3.Candidate C \n Cast your vote (1, 2, or 3): ").upper()
    
    if vote == '1':
        votes_A += 1
    elif vote == '2':
        votes_B += 1
    elif vote == '3':
        votes_C += 1
    else:
        print("\n Invalid vote. Please vote for Candidate A, Candidate B, or Candidate C. \n ")

# Check if the election should be canceled
if votes_C >=6:
    print(f" \n Election canceled due to  Candidate C got {votes_C} Votes.")
    print(f" \n Candidate A got {votes_A} votes\n Candidate B got {votes_B} votes\n Candidate C got {votes_C} votes \n")
else:
    # Determine the winner
    if votes_A == votes_B:
        print(f" \n Election tied between Candidate A and Candidate B. ")
        print(f" \n Candidate A got {votes_A} votes\n Candidate B got {votes_B} votes\n Candidate C got {votes_C} votes \n ")
    elif votes_A > votes_B:
        winner = 'A'
        marginA = votes_A - votes_B
        print(f" \n Candidate A wins by {marginA} votes.")
        print(f" \n Candidate A got {votes_A} votes\n Candidate B got {votes_B} votes\n Candidate C got {votes_C} votes \n")
    else:
        winner = 'B'
        marginB = votes_B - votes_A
        print(f" \n Candidate B wins by {marginB} votes.") 
        print(f" \n Candidate A got {votes_B} votes \n Candidate B got {votes_A} votes \n Candidate C got {votes_C} votes \n")
