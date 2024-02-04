"""
    This is a tool which can be used to do many operations on pdf files.
    Copyright (C) 2023  PingalPie

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from flask import Flask, redirect, url_for, request, render_template
from pdf import functions
import os

app = Flask(__name__)
funcs = functions()

options = funcs.__all__

@app.route('/')
def index():
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

@app.route('/compress', methods=['GET', 'POST'])
def compress():
    if request.method == 'POST':
        file = request.files['file']
        out_file = f'static/pdfs/reduced_size_{file.filename}'

        file.save(f'static/pdfs/{file.filename}')

        result = funcs.compress(f'static/pdfs/{file.filename}', out_file)

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

@app.route('/stamp')
def stamp():
     if request.method == 'POST':
          mainFile = request.files['mainFile']
          stampFile = request.files['stamp_file']

          l = mainFile.split('.')
          l.pop()
          out_file = ''.join(l) + '_stamped.pdf'

          del l
          result = funcs.stamp(stamp=stampFile, input_file=mainFile, output_file=out_file)
          os.rename(out_file, f'static/pdfs/{out_file}')
          # TODO: add feature for pages to stamp

          if result == 'Success':
                return render_template('stamp.html', out_file=f'static/pdfs/{out_file}')
          return render_template('stamp.html', error=result)
     return render_template('stamp.html', title="stamp pdf")

@app.route('/watermark')
def watermark():
     if request.method == 'POST':
          mainFile = request.files['mainFile']
          watermark = request.files['watermark']

          l = mainFile.split('.')
          l.pop()
          out_file = ''.join(l) + '_watermark.pdf'

          del l
          result = funcs.watermark(watermark=stampFile, input_file=mainFile, output_file=out_file)
          os.rename(out_file, f'static/pdfs/{out_file}')
          # TODO: add feature for selecting pages to watermark

          if result == 'Success':
                return render_template('watermark.html', out_file=f'static/pdfs/{out_file}')
          return render_template('watermark.html', error=result)
     return render_template('watermark.html', title="watermark pdf")

@app.route('/lock')
def lock():
     return render_template('lock.html')

@app.route('/unlock')
def unlock():
     return render_template('unlock.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
