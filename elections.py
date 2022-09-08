DONALD_TRUMP = "DONALD TRUMP"
JOE_BIDEN = "JOE BIDEN"
def count_votes_by_states (votes: list, search_state: str)-> tuple:
    votes_for_candidate1 = 0
    votes_for_candidate2 = 0
    for vote in votes:
        id, candidate, state, city = vote
        if (candidate.upper() == DONALD_TRUMP and state.upper() == search_state.upper()):
            votes_for_candidate1+=1
        if (candidate.upper() == JOE_BIDEN and state.upper() == search_state.upper()):
            votes_for_candidate2+=1
    
    return (
        {DONALD_TRUMP: votes_for_candidate1},
         {JOE_BIDEN: votes_for_candidate2}
    )

def count_total_votes_by_state(votes:list, states:tuple)->dict:
    total_votes_by_state = {}

    for state in states:
        total_votes_by_state[state] = count_votes_by_states(votes, state)
    
    return total_votes_by_state
        



    




votes = [
    ("WI1451", "Donald Trump", "Wisconsin", "Milwaukee"),
    ("VA4829", "Joe Biden", "Virginia", "Fairfax"),
    ("VA4820", "Joe Biden", "Virginia", "Fairfax"),
    ("VA4821", "Joe Biden", "Virginia", "Fairfax"),
    ("WI1451", "Donald Trump", "Virginia", "Fairfax")]

states = (
    "Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Delaware",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"IllinoisIndiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Maryland",
"Massachusetts",
"Michigan",
"Minnesota",
"Mississippi",
"Missouri",
"MontanaNebraska",
"Nevada",
"New Hampshire",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"PennsylvaniaRhode Island",
"South Carolina",
"South Dakota",
"Tennessee",
"Texas",
"Utah",
"Vermont",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin",
"Wyoming"
)









print(count_total_votes_by_state(votes, states))
print(count_votes_by_states(votes, 'Virginia'))