import os
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from src.model import get_sentence_transformer
from src.utils import load_config
from termcolor import colored

cfg = load_config()


def load_dir_data():
    loader = DirectoryLoader(
        cfg.DATA_PATH,
        glob="*.pdf",
        loader_cls=PyPDFLoader,
        show_progress=True,
        use_multithreading=True,
    )
    document_data = loader.load()

    return document_data


def split_doc_to_chunks(document_data):
    # Split the Document into chunks for embedding and vector storage.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=cfg.CHUNK_SIZE, chunk_overlap=cfg.CHUNK_OVERLAP
    )
    all_splits = text_splitter.split_documents(document_data)
    return all_splits


def save_data_to_faiss_vector_db(all_splits):
    embeddings = get_sentence_transformer()
    vectorstore = FAISS.from_documents(all_splits, embeddings)
    vectorstore.save_local(cfg.DB_FAISS_PATH)

    return "Database build completed ..."


def load_data():
    document_data = load_dir_data()
    all_splits = split_doc_to_chunks(document_data)
    return save_data_to_faiss_vector_db(all_splits)


def init_vector_db():
    files = [file for file in os.listdir(cfg.DB_FAISS_PATH) if file != 'readme.md']

    if not files:
        print(
            colored(f"{cfg.DB_FAISS_PATH} is empty. Build vector DB on first run", 'red')
        )
        resp = load_data()
        print(resp)
    else:
        print(
            colored(f"{cfg.DB_FAISS_PATH} is not empty. No need to build vector DB on first run",'green')
        )
