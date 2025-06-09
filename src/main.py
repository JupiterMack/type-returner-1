# src/main.py

"""
Type Returner: A Python utility to display all objects in the global namespace
and their corresponding Python types in a clean, readable table.
"""

# Import necessary components from the rich library for creating a styled table.
# 'Console' is used for printing rich content to the terminal.
# 'Table' is used to create the table structure.
from rich.console import Console
from rich.table import Table

# --- Example Objects ---
# Define a few objects of different types to demonstrate the script's functionality.
# These will be present in the global namespace when the script runs and will be
# included in the final output table.

# Basic data types
an_integer = 42
a_float = 3.14159
a_string = "Hello, Type Returner!"
a_boolean = True
a_none_type = None
a_complex_number = 1 + 2j

# Data structures
a_list = [1, 2, "three", 4.0]
a_tuple = (1, 2, "three", 4.0)
a_dictionary = {"key": "value", "number": 123}
a_set = {1, 2, 3, 3, 2, 1}
a_frozen_set = frozenset(a_set)

# A simple function
def example_function():
    """An example function to be listed in the global namespace."""
    pass

# A simple class
class ExampleClass:
    """An example class to be listed in the global namespace."""
    def __init__(self):
        self.value = 10

# An instance of the class
an_instance = ExampleClass()


def display_global_types():
    """
    Scans the global namespace, identifies the type of each object,
    and displays the results in a formatted table using the 'rich' library.
    """
    # Create a Console object for rich, colorful output to the terminal.
    console = Console()

    # Create a Table object to format the output.
    # We set a title and style the header for better readability.
    table = Table(
        title="Objects and Types in the Global Namespace",
        show_header=True,
        header_style="bold magenta"
    )

    # Define the columns for the table with specific styles.
    table.add_column("Object Name", style="cyan", no_wrap=True)
    table.add_column("Python Type", style="green")

    # Get a copy of the global namespace dictionary to iterate over.
    # We use .copy() as a good practice to avoid iterating over a dictionary
    # that might change during the loop.
    # We sort the items by name for a consistent and readable output.
    global_scope_items = sorted(globals().copy().items())

    # Iterate through each name and object in the global scope.
    for name, obj in global_scope_items:
        # Add the object's name and its type (converted to a string) as a new row.
        # The str(type(obj)) format gives the familiar <class '...'> representation.
        table.add_row(name, str(type(obj)))

    # Print the completed table to the console.
    console.print(table)


if __name__ == "__main__":
    # This is the main entry point of the script.
    # When the script is executed directly (e.g., `python src/main.py`),
    # this block will run. It calls the function to display the types of all
    # objects currently in the global namespace.
    display_global_types()