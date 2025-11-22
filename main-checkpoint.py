import tkinter as tk
from tkinter_interface import RPS_GUI

if __name__ == '__main__':
    # Initialize Tkinter
    root = tk.Tk()
    
    # Create the GUI instance
    app = RPS_GUI(root)
    
    # Start the Tkinter event loop
    root.mainloop()