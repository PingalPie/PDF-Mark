import pypdf
import os
from tkinter import filedialog as fd

class functions:
    def select_file(self):
        filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
        )
        file = fd.askopenfilename(
            title='Path of the pdf',
            initialdir='.',
            filetypes=filetypes)
        
        return file

    def split_pdf(self, input_file, output_file, start_page, end_page):
        """
        Split pages of a PDF file and save the result to a new file.

        Args:
            input_path (str): The path of the input PDF file.
            output_path (str): The path of the output PDF file.
            start_page (int): The first page to be included in the output file.
            end_page (int): The last page to be included in the output file.
        """
        try:
            if not isinstance(input_file, str):
                raise TypeError
            if not isinstance(output_file, str):
                raise TypeError
            if not isinstance(start_page, int):
                raise TypeError
            if not isinstance(end_page, int):
                raise TypeError
            
            if not os.path.exists(input_file):
                raise FileNotFoundError

            with open(input_file, "rb") as input_file:
                pdf_reader = pypdf.PdfReader(input_file)
                pdf_writer = pypdf.PdfWriter()

                for page_num in range(start_page - 1, end_page):
                    pdf_writer.add_page(pdf_reader.pages[page_num])

                with open(output_file, "wb") as output_file:
                    pdf_writer.write(output_file)
            return "Success"
        except Exception as e:
            return e

    def reduce_pdf_size(self, file, reduced_file_name):
        """"
        Reduce the size of the file

        Args:
            file (str): The path of the input file
            reduced_file_name (str): The path of the output file
        """
        
        try:
            if not isinstance(file, str):
                raise TypeError
            if not isinstance(reduced_file_name, str):
                raise TypeError
            
            if not os.path.exists(file):
                raise FileNotFoundError


            pdf_reader = pypdf.PdfReader(file)
            pdf_writer = pypdf.PdfWriter()

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

            pdf_writer.add_metadata(pdf_reader.metadata)

            with open(reduced_file_name, "wb") as f:
                pdf_writer.write(f)
            
            return "Success"
        except Exception as e:
            return e

    def merge_pdfs(self, list_of_files, output_file):
        """
        Append pdfs given in the argument list_of_files to provided output_file

        Args:
            list_of_files (list): The list of files
            output_file (str): The path of the output file 
        """
        try:
            pdf_writer = pypdf.PdfWriter()
            if not isinstance(list_of_files, list):
                raise TypeError
            
            for pdf in list_of_files:
                pdf_writer.append(pdf)
            
            pdf_writer.write(output_file)
            pdf_writer.close()

            return "Success"
        except Exception as e:
            return e
        
if __name__=='__main__':
    func =functions()
    print(func.split_pdf('sql1-10.pdf', 'sql1-2.pdf', 1, 2))