class VotingSystem:
    def __init__(self):
        self.votes = {}

    def add_vote(self, vote_for):
        if vote_for in self.votes:
            self.votes[vote_for] += 1
        else: 
            self.votes[vote_for] = 1

    def show_results(self):
        for candidate in sorted(self.votes):
            print(candidate, self.votes[candidate]) 

voting = VotingSystem()
voting.add_vote("Alice")
voting.add_vote("Bob")
voting.add_vote("Alice")
voting.show_results()