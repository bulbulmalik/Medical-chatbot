from setuptools import setup, find_packages
setup(
    name="medical-chatbot",
    version="0.1.0",
    author="BULBUL MALIK",
    packages=find_packages(),
    install_requires=[
        "langchain==0.3.26",
        "flask==3.1.1",
        "sentence-transformers==3.4.1",
        "pypdf==5.6.1",
        "python-dotenv==1.1.0",
        "langchain-pinecone==0.2.8",
        "langchain-groq==0.3.8",
        "gunicorn==23.0.0",
        "langchain-openai==0.3.24",
        "langchain-community==0.3.26",
    ],
)