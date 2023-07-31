import re
import urllib
import fitz
from tempfile import NamedTemporaryFile
from sklearn.neighbors import NearestNeighbors
import tensorflow_hub as hub
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import openai

class SemanticSearch:
    def __init__(self):
        self.model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
        self.knn = NearestNeighbors(n_neighbors=5, algorithm='auto', metric='cosine')

    def fit(self, data):
        self.data = data
        self.embeddings = self.model(data).numpy()
        self.knn.fit(self.embeddings)

    def __call__(self, query):
        query_embedding = self.model([query]).numpy()
        distances, indices = self.knn.kneighbors(query_embedding)
        return [(self.data[i], d) for i, d in zip(indices[0], distances[0])]

def download_pdf(url, output_path):
    urllib.request.urlretrieve(url, output_path)

def preprocess(text):
    text = text.replace('\n', ' ')
    text = re.sub('\s+', ' ', text)
    return text

def pdf_to_text(path, start_page=1, end_page=None):
    doc = fitz.open(path)
    total_pages = doc.page_count

    if end_page is None:
        end_page = total_pages

    text_list = []

    for i in range(start_page - 1, end_page):
        text = doc.load_page(i).get_text("text")
        text = preprocess(text)
        text_list.append(text)

    doc.close()
    return text_list

def text_to_chunks(texts, word_length=150, start_page=1):
    text_toks = [t.split(' ') for t in texts]
    chunks = []

    for idx, words in enumerate(text_toks):
        for i in range(0, len(words), word_length):
            chunk = words[i: i + word_length]
            if (
                (i + word_length) > len(words)
                and (len(chunk) < word_length)
                and (len(text_toks) != (idx + 1))
            ):
                text_toks[idx + 1] = chunk + text_toks[idx + 1]
                continue
            chunk = ' '.join(chunk).strip()
            chunk = f'[Page no. {idx+start_page}]' + ' ' + '"' + chunk + '"'
            chunks.append(chunk)
    return chunks

def get_answer_from_prompt(question, search_results, openAI_key):
    search_results_text = "\n".join(search_results)


    prompt = (
    "Compose a concise reply to the following question using the provided search results. "
    "Cite with [Page no.]. If the results mention identical subjects, provide separate answers. "
    "Rely only on the search results.\n\nQuestion: "
    f"{question}\nSearch Results:\n{search_results_text}"
    )


    openai.api_key = openAI_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
    )

    answer = response.choices[0].text.strip()
    return answer

def create_summary_pdf(question, answer, pdf_name="summary.pdf"):
    doc = SimpleDocTemplate(pdf_name, pagesize=letter)
    styles = getSampleStyleSheet()
    Story = [Spacer(1, 2 * 72)]

    question_title = f"Question: {question}"
    answer_title = "Answer:"

    question_style = styles["Heading1"]
    answer_style = styles["Heading2"]

    question_paragraph = Paragraph(question_title, question_style)
    answer_paragraph = Paragraph(answer_title, answer_style)
    answer_text = Paragraph(answer, styles["BodyText"])

    Story.append(question_paragraph)
    Story.append(Spacer(1, 12))
    Story.append(answer_paragraph)
    Story.append(Spacer(1, 12))
    Story.append(answer_text)
    Story.append(Spacer(1, 12))

    doc.build(Story)

def clean_filename(filename):
    return re.sub('[?/:*"><|]', '', filename)
