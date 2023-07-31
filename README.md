
# Semantic Search in PDFs

This project leverages semantic search to query PDF documents and provide concise answers. Using Google's Universal Sentence Encoder, we embed chunks of text from PDFs and then perform searches to find the most relevant passages. The results are then processed by OpenAI to deliver coherent and concise answers.

## Features:
- PDF text extraction and preprocessing.
- Text embedding using the Universal Sentence Encoder.
- Nearest neighbor search for semantic similarity.
- Concise answer generation using OpenAI.

## Table of Contents:
1. [Setup and Installation](#setup-and-installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [License](#license)

## Setup and Installation

### Prerequisites:
- Python 3.7 or newer.
- An OpenAI API key.

### Steps:

1. Clone the repository:
```
git clone https://github.com/yourusername/semantic-search-pdf.git
```
2. Navigate to the directory:
```
cd semantic-search-pdf
```
3. Install the required libraries:
```
pip install -r requirements.txt
```

## Usage

1. Ensure you have a file named `questions.txt` in the `data` directory. Each line should be a separate question you want to ask.
2. Run the `main.py` script:
```
python src/main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

Note: 
- You should replace `https://github.com/yourusername/semantic-search-pdf.git` with the actual URL of your GitHub repository.
- If you decide to include a `requirements.txt` file (which is a good practice), it should list all the Python libraries and their respective versions required for your project. 
- The license link is just a placeholder; you can replace it with the actual link to the license you're using for your project. If you don't have one yet, the provided link takes you to the MIT license, which is a popular open-source license.
