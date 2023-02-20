from flask import Flask, redirect, url_for, request, render_template
from pdf import functions
import os

app = Flask(__name__)
funcs = functions()

options = []

@app.route('/')
def index():
    global options
    for function in dir(functions):
        if not function.startswith('__') and not function=='select_file':
            options.append(function)
    return render_template('index.html', title="Welcome to PDF Manipulator", options=options)
    
@app.route('/manipulations')
def manuplations():
    option = request.args.get('option')
    return redirect(url_for(option))    

@app.route('/split_pdf', methods=['GET', 'POST'])
def split_pdf():
    if request.method == 'POST':
        file = request.files['file']
        out_file = f'splitted_{file.filename}'
        start_page = int(request.form['start_page'])
        end_page = int(request.form['end_page'])

        file_path = f'static/pdfs/{file.filename}'
        out_file_path = f'static/pdfs/{out_file}'

        file.save(file_path)

        result = funcs.split_pdf(file_path, out_file_path, start_page, end_page)

        if result == 'Success':
            return render_template('split_pdf.html', title="Split PDF", out_file=f'/static/pdfs/{out_file}')
        print(result)
        return render_template('split_pdf.html', title="Split PDF", error=result)
    return render_template('split_pdf.html', title="Split PDF")

@app.route('/reduce_pdf_size', methods=['GET', 'POST'])
def reduce_pdf_size():
    if request.method == 'POST':
        file = request.files['file']
        out_file = f'static/pdfs/reduced_size_{file.filename}'
        
        file.save(f'static/pdfs/{file.filename}')

        result = funcs.reduce_pdf_size(f'static/pdfs/{file.filename}', out_file)

        if result == 'Success':
            return render_template('reduce_pdf_size.html', title="Reduce PDF size", out_file=out_file)
        return render_template('reduce_pdf_size.html', title="Reduce PDF size", error=result)
    return render_template('reduce_pdf_size.html', title="Reduce PDF size")

@app.route('/merge_pdfs', methods=['GET', 'POST'])
def merge_pdfs():
    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']

        file1.save(f'static/pdfs/{file1.filename}')
        file2.save(f'static/pdfs/{file2.filename}')

        out_file = file1.filename.split('.')[0] + file2.filename

        result = funcs.merge_pdfs([file1, file2], out_file)
        os.rename(out_file, f'static/pdfs/{out_file}')

        if result == 'Success':
            return render_template('merge_pdfs.html', out_file=f'/static/pdfs/{out_file}')
        return render_template('merge_pdfs.html', error=result)
    return render_template('merge_pdfs.html', title="Merge PDFS")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)