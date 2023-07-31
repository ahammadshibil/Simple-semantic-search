from utils.helper_functions import (download_pdf, preprocess, pdf_to_text, text_to_chunks,
                                    get_answer_from_prompt, create_summary_pdf, clean_filename, SemanticSearch)
import openai

openAI_key = "YOUR_OPENAI_KEY"

if __name__ == "__main__":
    pdf_url = "https://www.example.com/sample.pdf"

    tmp_pdf = NamedTemporaryFile(delete=False)
    tmp_pdf.close()

    download_pdf(pdf_url, tmp_pdf.name)
    texts = pdf_to_text(tmp_pdf.name)
    chunks = text_to_chunks(texts)

    semantic_search = SemanticSearch()
    semantic_search.fit(chunks)

    # Open and read the questions.txt file
    with open('data/questions.txt', 'r') as file:
        questions = file.readlines()

    # Loop through each question
    for i, question in enumerate(questions):
        question = question.strip()  # Remove trailing and leading spaces
        print(f"Processing question: {question}")
        search_results = semantic_search(question)
        answer = get_answer_from_prompt(question, [r[0] for r in search_results], openAI_key)
        print(f"Answer: {answer}")
   
        create_summary_pdf(question, answer, pdf_name=f"summary_{i}.pdf")
