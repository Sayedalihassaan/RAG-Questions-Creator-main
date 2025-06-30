from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI , GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from dotenv import load_dotenv
from fpdf import FPDF
from PyPDF2 import PdfReader
import os



load_dotenv()
 
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def get_pdf_text(pdf_docs) :
    text = ""
    if not isinstance(pdf_docs , list) :
        pdf_docs = [pdf_docs]

    for i in pdf_docs :
        if i is not None :
            docs_pdf = PdfReader(i)
            for j in docs_pdf.pages :
                text += j.extract_text()

    return text




def get_text_chunks(text):
   
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=20000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text=text)
    return chunks



embedding_model = None
def get_vector_store(text_chunks):
    
    global embedding_model
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )
    vectore_store = FAISS.from_texts(text_chunks, embedding_model)
    vectore_store.save_local(folder_path="faiss-index")


# Define the function to take user query and return results
def user_query(question, num_questions, difficulty_level, question_types, include_answers):
    embedding_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001",
                                                   google_api_key=GOOGLE_API_KEY)
    
    # Load FAISS index from local storage
    new_db = FAISS.load_local(folder_path="faiss-index",
                              embeddings=embedding_model,
                              allow_dangerous_deserialization=True) #  index.pkl
    
    # Perform similarity search to get relevant documents
    docs = new_db.similarity_search(query=question, k=10)
    
    # Prepare the input for the chain
    chain_input = {
        "input_documents": docs,
        "input": question,
        "num_questions": num_questions,
        "difficulty_level": difficulty_level,
        "question_types": question_types,
        "include_answers": include_answers
    }
    
    exam_prompt = """
                    You are a knowledgeable and professional AI assistant that specializes in generating high-quality exam questions.

                    Your role is to:

                    1. Generate clear, accurate, and well-structured exam questions based on the provided context and requirements.
                    2. Ensure that questions are relevant to the given subject, topic, and difficulty level.
                    3. Vary the question types if requested (e.g., multiple choice, true/false, short answer, essay).
                    4. Provide correct answers or model answers if specified.
                    5. Follow academic standards and avoid overly simplistic or overly complex wording unless specified.
                    6. If context is not enough to generate meaningful questions, acknowledge the limitation and ask for more detail.

                    Remember:
                    - Do not make up unrelated information.
                    - Stick closely to the topic and subject area.
                    - Maintain clarity and educational value in all questions.
                    - Avoid repetition unless explicitly instructed.
                    - Ensure consistency with the question format and style.
                    - Do not put words in " " or ' '
                    - If the question type is multiple choice:
                    * "Place the choices **each on a new line** starting with a), b), c), d)"
                    * "Do not inline choices"
                    * "Keep formatting clean and professional"

                    Context:
                    {context}

                    Instructions:
                    - Number of Questions: {num_questions}
                    - Difficulty Level: {difficulty_level}
                    - Question Type(s): {question_types}
                    - Include Answers: {include_answers}

                    Now, generate the questions based on the above.
                    
                    """

    
    exam_prompt_template = PromptTemplate(
        input_variables=["context", "num_questions", "difficulty_level", "question_types", "include_answers"],
        template=exam_prompt
    )

    
    model = ChatGoogleGenerativeAI(api_key=GOOGLE_API_KEY, model="gemini-2.0-flash")

   
    chain = load_qa_chain(llm=model, prompt=exam_prompt_template)

    
    response = chain(chain_input, return_only_outputs=True)
    
    response = response["output_text"] + " ? "
    return response




def save_text_to_pdf(text, filename):
    try:
        # Ensure filename ends with .pdf
        if not filename.lower().endswith('.pdf'):
            filename += '.pdf'

        # Ensure the directory exists
        dir_name = os.path.dirname(filename)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name)

        pdf = FPDF()
        pdf.add_page()

        font_path = "fonts/DejaVuSans.ttf"
        if os.path.exists(font_path):
            pdf.add_font("DejaVu", "", font_path, uni=True)
            pdf.set_font("DejaVu", size=14)
        else:
            pdf.set_font("Arial", size=12)

        # Handle encoding issues
        for line in text.split('\n'):
            # Encode text to handle special characters
            pdf.multi_cell(0, 10, txt=line.encode('latin-1', 'replace').decode('latin-1'))

        absolute_path = os.path.abspath(filename)
        pdf.output(absolute_path)
        return absolute_path
    except Exception as e:
        print(f"Error saving PDF: {e}")
        return None