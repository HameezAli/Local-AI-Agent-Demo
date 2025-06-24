# Local-AI-Agent-Demo
YT Video Link: https://youtu.be/E4l91XKQSgw?si=Epvy-aqYxjqm2d1H
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
