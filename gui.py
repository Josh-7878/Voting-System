import tkinter as tk
from tkinter import messagebox
from controllers import ElectionController
from storage import save_data #Imports the save_data function

"""
GUI model for the Voting Systems
"""

class MainApplication(tk.Tk):
    """
    Main GUI application for the Voting Systems.
    """
    def __init__(self, controller: ElectionController):
        super().__init__()
        self.controller = controller

        self.title('Voting System')
        self.geometry('300x400')

        tk.Label(self, text="Vote for a Candidate", font=("Arial", 16)).pack(pady=10)

        for candidate_name in controller.get_candidate_names():
            button = tk.Button(self, text=candidate_name,
                               command=lambda c=candidate_name: self.vote(c))
            button.pack(pady=5)

        results_button = tk.Button(self, text="Show Results", command=self.show_results)
        results_button.pack(pady=10)

        #Reveals the winner and total votes
        winner_button = tk.Button(self, text="Show Winner", command=self.show_winner)
        winner_button.pack(pady=5)

        # Added a reset button
        reset_button = tk.Button(self, text="Reset Votes", command=self.reset_votes)
        reset_button.pack(pady=10)



    def vote(self, candidate_name: str)-> None: #Confirms the users vote
        try:
            self.controller.vote_for_candidate(candidate_name)
            messagebox.showinfo("Vote", f"Voted for {candidate_name}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def show_results(self) -> None: #Displays the voting result
        results = self.controller.get_results()
        messagebox.showinfo("Results", results)

    def show_winner(self) -> None:
        """
        Displays the winner of the election.
        """
        try:
            winner_message = self.controller.get_winner()
            messagebox.showinfo("Winner", winner_message)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def reset_votes(self) -> None:
        """
        Resets the votes and updates the UI accordingly.
        """
        self.controller.reset_votes()
        save_data(self.controller)
        messagebox.showinfo("Reset", "The votes have been reset.")
        #Updates UI elements if necessary