import argparse
import os
import sqlite3
from flask import Flask, jsonify, render_template, request, send_from_directory

DB_PATH = os.path.join(os.path.dirname(__file__), 'notes.db')
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with open(os.path.join(os.path.dirname(__file__), 'schema.sql'), 'r', encoding='utf-8') as f:
        schema = f.read()
    conn = get_db_connection()
    with conn:
        conn.executescript(schema)
    conn.close()

if not os.path.exists(DB_PATH):
    init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.get('/api/notes')
def api_list_notes():
    conn = get_db_connection()
    notes = conn.execute('SELECT id, text, created_at FROM notes ORDER BY id DESC').fetchall()
    conn.close()
    return jsonify([dict(n) for n in notes])

@app.post('/api/notes')
def api_create_note():
    data = request.get_json(silent=True) or {}
    text = (data.get('text') or '').strip()
    if not text:
        return jsonify({'error': 'Text is required.'}), 400
    conn = get_db_connection()
    with conn:
        cur = conn.execute('INSERT INTO notes (text) VALUES (?)', (text,))
        note_id = cur.lastrowid
        row = conn.execute('SELECT id, text, created_at FROM notes WHERE id = ?', (note_id,)).fetchone()
    conn.close()
    return jsonify(dict(row)), 201

@app.delete('/api/notes/<int:note_id>')
def api_delete_note(note_id):
    conn = get_db_connection()
    with conn:
        conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.close()
    return jsonify({'ok': True})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--initdb', action='store_true', help='Initialize the SQLite database and exit.')
    args = parser.parse_args()

    if args.initdb:
        init_db()
        print('Database initialized at', DB_PATH)
    else:
        app.run(debug=True)
