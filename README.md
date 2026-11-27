# Countries, Regions, Languages, and Borders
This program retrieves country data from the REST Countries API and allows users to search for countries based on their official languages. For each matching country, the program displays its name, region, bordering countries, and official languages.

## API

This project uses the [REST Countries](https://api.restcountries.com/countries/v5) API.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-intro-final-project.git
   cd python-intro-final-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # macOS/Linux
   # .venv\Scripts\activate       # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python main.py --language
```

User runs program including a language argument. 
Describe what happens when the program runs — what prompt(s) appear and what the user can do.

## CLI Interactions

Describe each interaction your CLI supports.

- **Filter by language** —  Enter a language as a command-line argument to display all countries where that language is an official language.
- **Language validation** — The program uses argparse to validate the language against the available languages returned by the API. If an unsupported language is entered, the program displays an error and the available choices.
- **Country information** — For each matching country, the program displays: Country name, Geographic region, Bordering countries, Official languages