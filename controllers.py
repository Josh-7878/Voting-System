from models import Candidate


class ElectionController:
    """
    Controller to manage election operations.

    Attributes:
        candidates (list[Candidate]): List of candidates in the election.
    """

    def __init__(self):
        """
        Initializes with an empty list of candidates.
        """
        self.candidates = []

    def add_candidate(self, name: str):
        """
        Adds a new candidate to the election.

        Args:
            name(str): The name of the candidate to add.

        Raises:
            ValueError: If the name is empty or the candidate already exists.
        """
        if not name.strip():
            raise ValueError("Candidate name cannot be empty.")
        if name in self.get_candidate_names():
            raise ValueError(f"Candidate '{name}' already exists.")
        self.candidates.append(Candidate(name))

    def vote_for_candidate(self, candidate_name: str) -> bool:
        """
        Records the vote of a specific candidate.

        Args:
            candidate_name (str): The name of the candidate to vote for.

        Returns:
            bool: True if the vote was successfully recorded, False if it wasn't.
        """
        for candidate in self.candidates:
            if candidate.name == candidate_name:
                candidate.add_vote()
                return True
        return False

    def get_results(self) -> str:
        """
        Returns a string with the voting results.

        Returns:
            str: The results as "Candidate: X votes" for all candidates.
        """

        if not self.candidates:
            return "No candidates available."
        return "\n".join(f"{c.name}: {c.votes} votes" for c in self.candidates)

    def get_candidate_names(self) -> list[str]:
        """
        Returns a list of candidate names.

        Returns:
            list[str]: A list of candidate names.
        """
        return [c.name for c in self.candidates]

    def reset_votes(self)-> None:
        """
        Resets the votes for all candidates.
        """
        for candidate in self.candidates:
            candidate.votes = 0