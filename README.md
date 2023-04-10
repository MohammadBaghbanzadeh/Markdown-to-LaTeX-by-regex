# Converting Wikipedia Math Text to LaTeX

This project is a Python script that extracts mathematical formulas from a Wikipedia page and converts them into LaTeX format using regular expressions.

## Usage

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Open the `wiki.txt` file and replace its content with the desired Wikipedia article's text (make sure it contains mathematical formulas).
4. Run the script using `python convert.py`.
5. The output will be saved in the `output.txt` file.
6. Visit [LaTeX Equation Editor](https://www.latex4technics.com/) or any other LaTeX editor of your choice to generate images from the LaTeX equations in the output file.

## How it works

The script uses regular expressions to extract mathematical formulas and highlight text from the input text. The following tags are replaced with their corresponding LaTeX commands:

- `<math>` and `</math>` tags are replaced with `$` signs.
- `<sub>` and `</sub>` tags are replaced with `_`.
- `<sup>` and `</sup>` tags are replaced with `^`.
- `'''` tags are replaced with `\textbf{}`.
- `''` tags are replaced with `\textit{}`.
- Text inside `[[...]]` tags is highlighted using `\textbf{}`.

## References

The script was tested on the following Wikipedia page:

- [Riemann hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
