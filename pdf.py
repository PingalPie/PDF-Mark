import pypdf
import os
from PIL import Image
from tkinter import filedialog as fd

class incorrectNoPagesException:
    "Enter correct no. of pages"

class functions:
    def select_file_pdf(self):
        filetypes = (
        ('PDF files', '*.pdf'),
        ('All files', '*.*')
        )
        file = fd.askopenfilename(
            title='Path of the pdf',
            initialdir='.',
            filetypes=filetypes)
        
        return file
    
    def select_output_file_pdf(self):
        filetypes = (
        ('PDF files', '*.pdf,*.PDF'),
        ('All files', '*.*')
        )
        file = fd.asksaveasfilename(
            title='Path of the output pdf',
            initialdir='.',
            filetypes=filetypes)
        
        return file
    
    def select_file_image(self):
        filetypes = (
        ('Image files', '*.jpg,*.png,*.bmp,*.jpeg'),
        ('All files', '*.*')
        )
        file = fd.askopenfilename(
            title='Path of the pdf',
            initialdir='.',
            filetypes=filetypes)
        
        return file

    def split_pdf(self, input_file: str, output_file: str, start_page: int , end_page: int):
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
                reader = pypdf.PdfReader(input_file)
                writer = pypdf.PdfWriter()

                if len(reader.pages)<start_page or len(reader.pages)<end_page:
                    raise incorrectNoPagesException
                for page_num in range(start_page - 1, end_page):
                    writer.add_page(reader.pages[page_num])

                with open(output_file, "wb") as output_file:
                    writer.write(output_file)
            return "Success"
        except Exception as e:
            return e

    def reduce_pdf_size(self, file: str, reduced_file_name: str):
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


            reader = pypdf.PdfReader(file)
            writer = pypdf.PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.add_metadata(reader.metadata)

            with open(reduced_file_name, "wb") as f:
                writer.write(f)
            
            return "Success"
        except Exception as e:
            return e

    def merge_pdfs(self, list_of_files: list, output_file: str):
        """
        Append pdfs given in the argument list_of_files to provided output_file

        Args:
            list_of_files (list): The list of files
            output_file (str): The path of the output file 
        """
        try:
            if not isinstance(list_of_files, list):
                raise TypeError
            
            writer = pypdf.PdfWriter()
            
            for pdf in list_of_files:
                writer.append(pdf)
            
            writer.write(output_file)
            writer.close()

            return "Success"
        except Exception as e:
            return e

    def convert_images_to_pdf(self, list_of_images: list, output_path: str):
        """
        Convert the given image to a pdf

        Args:
            list_of_images (list): List of the images to be converted to pdf
            output_path (str): Path of output file, where pdf will be stored
        """
        try:
            if not isinstance(list_of_images, list):
                raise TypeError
            if not isinstance(output_path, str):
                raise TypeError

            for image_path in list_of_images:
                if not os.path.exists(image_path):
                    raise FileNotFoundError

            image_obj_list = []

            for image in list_of_images:
                image_pil = Image.open(image)
                img = image_pil.convert('RGB')
                image_obj_list.append(img)

            img = image_obj_list[0]
            image_obj_list.pop(0)

            img.save(fr'{output_path}', format='pdf', save_all=True, append_images=image_obj_list)
            return "Success"

        except Exception as e:
            return e

    def stamp_pdf(self, stamp: str, input_file: str, output_file: str): # Not ready yet
            """
        Stamp the pdf given in the input_file

        Args:
            stamp (str): The path of the stamp image
            input_file (str): The path of the file which needs to be stamped
            output_file (str): The path of the file to which stamped file will be stored
        """

        # try:
        #     if not isinstance(stamp, str):
        #         raise TypeError
        #     if not isinstance(input_file, str):
        #         raise TypeError
        #     if not isinstance(output_file, str):
        #         raise TypeError
            
        #     if not os.path.exists(stamp):
        #         raise FileNotFoundError
        #     if not os.path.exists(input_file):
        #         raise FileNotFoundError

        #     reader = pypdf.PdfReader(input_file)
        #     writer = pypdf.PdfWriter()

        #     page_indices = list(range(0, len(reader.pages)))
        #     print(page_indices)

        #     for index in page_indices:
        #         content_of_page = reader.pages[index]
        #         mediabox = content_of_page.mediabox
        #         content_of_page.merge_page(stamp)
        #         content_of_page.mediabox = mediabox
        #         writer.add_page(content_of_page)

        #     with open(output_file, 'wb') as f:
        #         writer.write(f)

        # except Exception as e:
        #     print(e)
            if not isinstance(stamp, str):
                raise TypeError
            if not isinstance(input_file, str):
                raise TypeError
            if not isinstance(output_file, str):
                raise TypeError
            
            if not os.path.exists(stamp):
                raise FileNotFoundError
            if not os.path.exists(input_file):
                raise FileNotFoundError

            reader = pypdf.PdfReader(input_file)
            writer = pypdf.PdfWriter()

            page_indices = list(range(0, len(reader.pages)))
            print(page_indices)

            for index in page_indices:
                content_page = reader.pages[index]
                mediabox = content_page.mediabox
                # content_page.merge_page(stamp)
                content_page.mediabox = mediabox
                writer.add_page(content_page)
            with open(output_file, 'wb') as f:
                writer.write(f)

    def watermark(self, watermark: str, input_file: str, output_file: str): # Not ready yet
        """
        Watermark the file in the argument input_file

        Args: 
            watermark (str): Path of the image file that is going to be used as watermark.
            input_file (str): Path of the input file that is going to have the watermark.
            output_file (str): Path of the pdf where the pdf will stored.  
        """
        try:
            if not isinstance(watermark, str):
                raise TypeError
            if not isinstance(input_file, str):
                raise TypeError
            if not isinstance(output_file, str):
                raise TypeError
            
            if not os.path.exists(watermark):
                raise FileNotFoundError
            if not os.path.exists(input_file):
                raise FileNotFoundError
            
            self.convert_images_to_pdf([watermark], f'{watermark}.pdf')

            real_watermark = watermark

            reader = pypdf.PdfReader(input_file)
            page_indices = list(range(0, len(reader.pages)))

            writer = pypdf.PdfWriter()
            
            for index in page_indices:
                content_page = reader.pages[index]
                mediabox = content_page.mediabox

                watermark_reader = pypdf.PdfReader(f'{real_watermark}.pdf')
                watermark = watermark_reader.pages[0]

                watermark.merge_page(content_page)
                watermark.mediabox = mediabox
                writer.add_page(watermark)
                
            os.remove(f'{real_watermark}.pdf')

            with open(output_file, "wb") as f:
                writer.write(f)
            return "Success"

        except Exception as e:
            return e

if __name__=='__main__':
    funcs = functions()