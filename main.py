"""
This module initializes the election controller, loads data,
and starts the main application GUI.
"""

from controllers import ElectionController
from gui import MainApplication
from storage import load_data, save_data

def main()-> None:
    controller = ElectionController()
    # Initialize candidates here or loads from file
    controller.add_candidate('Johnny')
    controller.add_candidate('Daniel')
    controller.add_candidate('Ally')

    load_data(controller)  # Loads data if available

    app = MainApplication(controller) #Starts the GUI application
    app.protocol("WM_DELETE_WINDOW", lambda: on_close(app, controller))  # Handles window close event
    app.mainloop()

def on_close(app: MainApplication, controller: ElectionController)-> None:
    """
       Handles application shutdown and data saving.

       Saves the current vote data and closes the application.
    """
    save_data(controller)  # Saves data on close
    app.destroy()

if __name__ == '__main__':
    main()
