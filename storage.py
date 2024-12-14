import json
from models import Candidate# Imports class
from controllers import ElectionController

def save_data(controller) -> None:
    """
    Saves the current vote count to a file.
    The file will have the format: {'candidate_name': votes}
    """

    with open('vote_data.json', 'w') as file:
        data = {candidate.name: candidate.votes for candidate in controller.candidates}
        json.dump(data, file)

def load_data(controller: ElectionController) -> None:
    """
    Loads the vote count from a JSON file.
    Expects the file format: {'candidate_name': votes}
    If the file is missing or corrupted no further changes will be made
    """
    try:
        with open('vote_data.json', 'r') as file:
            data = json.load(file)
            controller.candidates.clear()  # Clears any existing candidates before loading
            for name, votes in data.items():
                candidate = Candidate(name)  # Creates a new Candidate instance
                candidate.votes = votes
                controller.candidates.append(candidate)
    except FileNotFoundError:
        print('No previous data found')
        pass
    except json.JSONDecodeError:
        print('Error: Corrupted data file')
        pass