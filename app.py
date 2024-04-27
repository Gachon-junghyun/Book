from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import PyPDF2
#from konlpy.tag import Okt



app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    session['name'] = request.form['name']
    if 'pdfs' not in session:
        session['pdfs'] = []
    return redirect(url_for('user_dashboard'))

@app.route('/dashboard')
def user_dashboard():
    if 'name' in session:
        name = session['name']
        pdfs = session.get('pdfs', [])
        return render_template('dashboard.html', name=name, pdfs=pdfs)
    return redirect(url_for('home'))

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['pdfs'].append({'name': filename, 'progress': '0%'})
            session.modified = True
            flash('File uploaded successfully.')
        return redirect(url_for('user_dashboard'))
    return redirect(url_for("home"))

@app.route('/pdf_reader/<pdf_name>')
def play_pdf(pdf_name):
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_name)
    text = extract_text_from_pdf(pdf_path)
    #analyzed_text = analyze_text(text)

    return render_template('pdf_reader.html', pdf_name=pdf_name, text=text)


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extractText() if page.extractText() else ''
    return text


"""
def analyze_text(text):
    okt = Okt()
    morphs = okt.morphs(text)
    return ' '.join(morphs)
"""
if __name__ == '__main__':
    app.run(debug=True)
