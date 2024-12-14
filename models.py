class Candidate:
    """
    Candidate model representing a candidate in the election.

    Attributes:
        name (str):The name of the candidate
        votes (int): The number votes towards the candidate
    """
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError('Candidate name cannot be empty')
        self.name = name
        self.votes = 0

    def add_vote(self) -> None:
        """Adds a vote to the candidate."""
        self.votes += 1