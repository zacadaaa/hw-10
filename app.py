from flask import Flask
from utils import *


app = Flask(__name__)


@app.route('/')
def index():
    """Главная страница"""
    candidates = get_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'
    return f"<pre> {result}</pre>"


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    """Поиск кандидата по pk"""
    candidate = get_by_pk(pk)
    result = '<br>'
    result += candidate['name'] + '<br>'
    result += candidate['position'] + '<br>'
    result += candidate['skills'] + '<br>'
    result += '<br>'
    return f"""
        <img src="{candidate['picture']}"
        <pre> {result}</pre>
    """


@app.route('/candidate/<skill>')
def get_candidate_by_skills(skill):
    """Поиск кандидата по навыку"""
    candidates = get_by_skill(skill.lower())
    result = '<br>'
    for candidate in candidates:
        result += candidate['name'] + '<br>'
        result += candidate['position'] + '<br>'
        result += candidate['skills'] + '<br>'
        result += '<br>'
    return f"<pre> {result}</pre>"


app.run(debug=True)
