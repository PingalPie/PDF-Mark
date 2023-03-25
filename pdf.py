import pypdf
import os
from pathlib import Path
from typing import Union, Literal, List
from PIL import Image
from tkinter import filedialog as fd

class incorrectNoPagesException:
	"Enter correct no. of pages"

class functions:
	def __init__(self):
		super().__init__()
		self.__all__ = ['split_pdf', 'merge_pdfs', 'reduce_pdf_size', 'stamp', 'watermark', 'convert_images_to_pdf']
	
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

	def split_pdf(self, input_file: Path, output_file: Path, start_page: int =1, end_page: int=1):
		"""
		Split pages of a PDF file and save the result to a new file.

		Args:
			input_path (Path): The path of the input PDF file.
			output_path (Path): The path of the output PDF file.
			start_page (int) (default: 1): The first page to be included in the output file.
			end_page (int) (default: 1): The last page to be included in the output file.
		"""
		try:
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

	def reduce_pdf_size(self, file: Path, reduced_file_name: Path):
		""""
		Reduce the size of the file

		Args:
			file (Path): The path of the input file
			reduced_file_name (Path): The path of the output file
		"""
		
		try:
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

	def merge_pdfs(self, list_of_files: list, output_file: Path):
		"""
		Append pdfs given in the argument list_of_files to provided output_file

		Args:
			list_of_files (list): The list of files
			output_file (Path): The path of the output file 
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

	def convert_images_to_pdf(self, list_of_images: list, output_path: Path):
		"""
		Convert the given image to a pdf

		Args:
			list_of_images (list): List of the images to be converted to pdf
			output_path (Path): Path of output file, where pdf will be stored
		"""
		try:
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

	def stamp_pdf(self, stamp: Path, input_file: Path, output_file: Path): # Not ready yet
			"""
		Stamp the pdf given in the input_file

		Args:
			stamp (Path): The path of the stamp image
			input_file (Path): The path of the file which needs to be stamped
			output_file (Path): The path of the file to which stamped file will be stored
		"""

		# try:
			
		#	 if not os.path.exists(stamp):
		#		 raise FileNotFoundError
		#	 if not os.path.exists(input_file):
		#		 raise FileNotFoundError

		#	 reader = pypdf.PdfReader(input_file)
		#	 writer = pypdf.PdfWriter()

		#	 page_indices = list(range(0, len(reader.pages)))
		#	 print(page_indices)

		#	 for index in page_indices:
		#		 content_of_page = reader.pages[index]
		#		 mediabox = content_of_page.mediabox
		#		 content_of_page.merge_page(stamp)
		#		 content_of_page.mediabox = mediabox
		#		 writer.add_page(content_of_page)

		#	 with open(output_file, 'wb') as f:
		#		 writer.write(f)

		# except Exception as e:
		#	 print(e)
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

	def watermark(self, watermark: Path, input_file: Path, output_file: Path, page_indices: Union[Literal["ALL"], List[int]] = "ALL"):
		"""
		Watermark the file in the argument input_file

		Args: 
			watermark (Path): Path of the image file that is going to be used as watermark.
			input_file (Path): Path of the input file that is going to have the watermark.
		    page_indices (list): list of pages on which watermark is to be applied.
			output_file (Path): Path of the pdf where the pdf will stored.  
		"""
		try:
			if not os.path.exists(watermark):
				raise FileNotFoundError
			if not os.path.exists(input_file):
				raise FileNotFoundError

			reader = pypdf.PdfReader(input_file)
			if page_indices == 'ALL':
				page_indices = range(len(reader.pages))
			
			writer = pypdf.PdfWriter()
			if watermark.split('.')[-1] == 'pdf':
				watermark_page = pypdf.PdfReader(watermark).pages[0]
			else:
				self.convert_images_to_pdf([watermark], watermark + '.pdf')
				watermark_page = pypdf.PdfReader(watermark+'.pdf').pages[0]
				
			for index in page_indices:
				content_page = reader.pages[index]
				content_page.merge_transformed_page(watermark_page, pypdf.Transformation(), over=False)
				writer.add_page(content_page)
				
			with open(output_file, "wb") as f:
				writer.write(f)
			return "Success"

		except Exception as e:
			return e

if __name__=='__main__':
	funcs = functions()
	print(funcs.watermark('twst.pdf', 'mamu.pdf', 'test2_watermark.pdf'))
