# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

import tkinter as tk
import number_entry as nent
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()
    root.geometry("400x300")

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Area Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Radius:"
    lbl_radius = tk.Label(frm_main, text="Radius (cm):")

    # Create a integer entry box where the user will enter a radius value.
    ent_radius = nent.FloatEntry(frm_main, 1, 100000, width=10)

    # Create a label that displays "Area Circle:"
    lbl_area = tk.Label(frm_main, text="Area Circle:")

    # Create labels that will display the area of the circle.
    lbl_result = tk.Label(frm_main, width=10)

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_radius.grid(row=0, column=1, padx=3, pady=3)
    lbl_area.grid(row=0, column=2, padx=(30, 3), pady=3)
    lbl_result.grid(row=0, column=4, padx=3, pady=3)
    btn_clear.grid(row=1, column=0, padx=3, pady=3, columnspan=5, sticky="w")

    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the radius from the user
            radius = ent_radius.get()

            # Compute the area of a circle.
            area = float(math.pi * radius ** 2)

            # Display the area of a circle.
            lbl_result.config(text=f"{area:.2f}")

        except ValueError:
            # When the user deletes all the digits in the radius
            # entry box, clear the result of the area of a circle.
            lbl_result.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_radius.delete(0, tk.END)
        lbl_result.config(text="")
        ent_radius.focus()

    # Bind the calculate function to the radius entry box
    # so that the calculate function will be called when
    # the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the radius entry box.
    ent_radius.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
