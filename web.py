from flask import Flask, redirect, url_for, request, render_template
from pdf import functions
import json
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
    return render_template('index.html',
                        title='hello',
                        options=options)
    
@app.route('/manipulations')
def manuplations():
    option = request.args.get('option')
    return redirect(url_for(option))    

@app.route('/split_pdf', methods=['GET', 'POST'])
def split_pdf():
    if request.method == 'POST':
        file = request.form['file']
        out_file = f'splitted_{request.form["file"]}'
        start_page = int(request.form['start_page'])
        end_page = int(request.form['end_page'])

        result = funcs.split_pdf(file, out_file, start_page, end_page)

        os.rename(out_file, f'static/pdfs/{out_file}')

        if result == 'Success':
            return render_template('split_pdf.html', out_file=f'/static/pdfs/{out_file}')
        return render_template('split_pdf.html', error=result)
    return render_template('split_pdf.html')

@app.route('/reduce_pdf_size', methods=['GET', 'POST'])
def reduce_pdf_size():
    if request.method == 'POST':
        file = request.form['file']
        out_file = f'reduced_size_{file}'
        
        result = funcs.reduce_pdf_size(file, out_file)
        os.rename(out_file, f'static/pdfs/{out_file}')

        if result == 'Success':
            return render_template('reduce_pdf_size.html', out_file=f'/static/pdfs/{out_file}')
        return render_template('reduce_pdf_size.html', error=result)
    return render_template('reduce_pdf_size.html')

@app.route('/merge_pdfs', methods=['GET', 'POST'])
def merge_pdfs():
    if request.method == 'POST':
        file1 = request.form['file1']
        file2 = request.form['file2']

        out_file = file1.split('.')[0] + file2

        result = funcs.merge_pdfs([file1, file2], out_file)
        os.rename(out_file, f'static/pdfs/{out_file}')

        if result == 'Success':
            return render_template('merge_pdfs.html', out_file=f'/static/pdfs/{out_file}')
        return render_template('merge_pdfs.html', error=result)
    return render_template('merge_pdfs.html')


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)