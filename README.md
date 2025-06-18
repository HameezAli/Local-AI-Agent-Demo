# Local-AI-Agent-Demo
1. Install ollama in your pc 
2. In cmd,
----------
ollama pull llama3.2

ollama pull mxbai-embed-large

3. Terminal codes in order, one-by-one
-------------------------
cd Local-AI-Agent-Demo

python -m venv venv

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

./venv/Scripts/activate

python .\main.py
