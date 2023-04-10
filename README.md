Convert Wikipedia Mathematical Formulas to LaTeX
This Python script converts mathematical formulas found on a Wikipedia page to LaTeX format using regular expressions. It replaces certain tags related to mathematical formulas and markdown tags with their corresponding LaTeX commands or tags.

Requirements
Python 3.x
re module (built-in)
Usage
Clone the repository.
Navigate to the project folder and place the text file containing the Wikipedia page content in the same directory as the Python script.
Run the main.py file using the following command:
python main.py
The converted LaTeX output will be saved in a new file named output.txt.
Details
The script uses the following regular expressions to identify and replace various tags:

patterns = [
    r'<(\/)?(math|sub|sup)>',
    r'<math>\([^<]*\)<\/math>',
    r'<math display="block">\([^<]*\)<\/math>',
    r'\[\[\(.*\)\]\]',
    r"'''.*?'''",
    r"'''(.*?)'''",
    r"''(.*?)''"
]
It then uses the following dictionary to replace each tag with its corresponding LaTeX command or tag:

replacements = {
    '<math>': '$',
    '</math>': '$',
    '<sub>': '_',
    '</sub>': '',
    '<sup>': '^',
    '</sup>': '',
    "'''": '\\textbf{',
    "'''": '}',
    "''": '\\textit{',
    "''": '}',
}
Example
To see an example of how the script works, the main.py file has been pre-configured to convert the mathematical formulas found on the Riemann hypothesis Wikipedia page.
