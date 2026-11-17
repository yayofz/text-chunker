from utils import chunk_text, word_freq, top_words

class Document():
    def __init__(self, title, text):
        self.title = title
        self.text = text
    def __repr__(self):
        return f"Document(title={self.title!r}, words={self.word_count()})"
    def word_count(self):
        words = self.text.split()
        return len(words)
    def search(self, query):
        stripped_query = query.strip()
        if stripped_query:
            search_query = []
            sentences = self.text.split(".")
            for sentence in sentences:
                if sentence and stripped_query.lower() in sentence.lower():
                    search_query.append(sentence.strip())
            return search_query
        raise ValueError("Запрос пустой")
    def chunk_text(self, size=50, overlap=10):
        return chunk_text(self.text, size, overlap)

with open("notes.txt", 'r', encoding="utf-8") as f:
    text = f.read()

my_document = Document(title="notes.txt", text=text)
STOP_WORDS = {"и", "в", "на", "для", "с", "это", "что", "как", "а", "не", "по", "из", "его", "них", "свою", "именно", "потом"}

chunked_document = my_document.chunk_text(size=50, overlap=10)
print(len(chunked_document))
print(len(chunked_document[-1].split()))


for number, chunk in enumerate(chunked_document, start=1):
    print(number,top_words(chunk, 3, STOP_WORDS))