# Converting Wikipedia Math Tags to LaTeX

This is a Python program that converts various math tags and markdown tags from a given Wikipedia page to their respective LaTeX commands. The converted text can then be used in LaTeX documents.

## How to Use

1. Clone the repository to your local machine
2. Install the necessary packages (if any)
3. Open `wiki.txt` and replace the contents with the desired Wikipedia page's text
4. Run the Python script `MD_to_LaTeX.py`
5. The output will be saved as `output.txt` in the same directory

## Supported Tags

The following tags are supported and converted to their LaTeX equivalents:

- `<math>...</math>` (inline math)
- `<math display="block">...</math>` (display/blocked math)
- `<sub>...</sub>` (subscripts)
- `<sup>...</sup>` (superscripts)
- `'''...'''` (bold)
- `''...''` (italic)
- `[[...]]` (text highlighting)

## File Structure

- `math_converter.py`: the main Python script 
- `wiki.txt`: input file containing the text from the chosen Wikipedia page
- `output.txt`: output file containing the converted text in LaTeX format
- `regex_explanations.txt`: explanation of each regex used in the code

## Credits

This project was created by Mohammad Baghbanzadeh, 9812223158.

## Source

The text used for conversion is taken from the Wikipedia page on [Riemann Hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis).
