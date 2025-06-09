# type-returner

A simple Python utility that returns a list of every object in the global namespace and the type Python interprets it as. The output is displayed in a clean, readable table format using the `rich` library.

## Overview

This script is a handy tool for introspection and debugging. It scans the `globals()` scope, identifies every object, and neatly presents its name and its Python type (`<class '...'`). This can be useful for understanding the state of a program at a certain point or for educational purposes to see how Python classifies different data structures.

## Features

*   Scans the global namespace for all existing objects.
*   Identifies the type of each object.
*   Presents the results in a clear, color-coded table in the console.

## Installation

To get a local copy up and running, follow these simple steps.

1.  **Clone the repository**
    ```sh
    git clone https://github.com/JupiterMack/type-returner-1.git
    ```

2.  **Navigate to the project directory**
    ```sh
    cd type-returner-1
    ```

3.  **(Recommended) Create and activate a virtual environment**
    *   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```

4.  **Install the required dependencies**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use the application, simply execute the main Python script from your terminal. The script will automatically inspect the environment and print the results.

```sh
python type_returner.py
```
*(Assuming the main script is named `type_returner.py`)*

### Example Output

The script will print a table to your console, similar to the one below. The actual output in your terminal will be color-coded for better readability.

| Object Name          | Type                      |
| -------------------- | ------------------------- |
| my_string            | `<class 'str'>`           |
| an_integer           | `<class 'int'>`           |
| a_float              | `<class 'float'>`         |
| a_list_of_items      | `<class 'list'>`          |
| a_dictionary         | `<class 'dict'>`          |
| my_custom_function   | `<class 'function'>`      |
| MyClass              | `<class 'type'>`          |
| ...                  | ...                       |

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

You can also open an issue directly here: [https://github.com/JupiterMack/type-returner-1/issues](https://github.com/JupiterMack/type-returner-1/issues)