from flask import Flask, request, jsonify, render_template
from sql_metadata import Parser
import re

app = Flask(__name__)

def extract_tables(sql):
    parser = Parser(sql)
    return list(set(parser.tables))

def extract_columns(sql):
    sql = re.sub(r"'[^']*'", '', sql)
    columns = re.findall(r'\b(?:[A-Za-z0-9_]+\.)?[A-Za-z0-9_]+\b', sql)
    sql_keywords = {
        'SELECT', 'FROM', 'WHERE', 'GROUP', 'ORDER', 'BY', 'AS', 'AND', 'OR', 'CASE', 'WHEN', 'THEN', 'ELSE', 'END', 'SUM',
        'DISTINCT', 'NOT', 'LEFT', 'OUTER', 'JOIN', 'ON', 'ASC', 'IN', 'IS', 'NULL', 'DESC', 'INNER', 'RIGHT', 'WITH', 'FULL', ''
    }
    columns = {col for col in columns if col.upper() not in sql_keywords and not col.isdigit()}
    return list(columns)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    sql = request.json.get('sql', '')
    tables = extract_tables(sql)
    columns = extract_columns(sql)
    return jsonify({'tables': tables, 'columns': columns})

if __name__ == '__main__':
    app.run(debug=True)