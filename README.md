Certainly, here's a revised `README.md` file for your "simple-semantic-search" project:

---

# Simple Semantic Search

## Overview
This repository contains a project focused on implementing semantic search on PDF documents. It uses the Universal Sentence Encoder model to embed textual data and then performs nearest neighbor search to find the most relevant passages in response to a query.

## How to Use
1. Clone the repository to your local machine.
2. Install the necessary Python packages using:
```bash
pip install -r requirements.txt
```
3. Run the `main.py` script to execute the code.

## Project Structure
- **main.py**: This is the main script where the primary functionality of the app is located.
- **utils/helper_functions.py**: Contains helper functions required by the main script.
- **data/questions.txt**: Contains sample questions to query the semantic search.

## Dependencies
All necessary dependencies are listed in the `requirements.txt` file. The core packages include:
- `numpy`
- `openai`
- `requests`
- `fitz`
- `fastapi`
- `scikit-learn`
- `tensorflow_hub`
- `reportlab`

... and others.

## License
[MIT License](LICENSE)

---

Make sure to adjust any other specific details or add sections as per the needs of your project. If you have a license (e.g., MIT), you can include a link to it as done above; otherwise, you can remove the License section.
