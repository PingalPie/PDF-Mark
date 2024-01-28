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
		self.__all__ = ['split_pdf', 'merge_pdfs', 'compress', 'stamp', 'watermark', 'convert_images_to_pdf', 'lock', 'unlock']

	def select_file_pdf(self):
		filetypes = (
		('PDF files', '*.pdf,*.PDF'),
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

	def split_pdf(self, input_file: Path, output_file: Path, start_page: int=1, end_page: int=1):
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

	def compress(self, file: Path, reduced_file_name: Path):
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

	def stamp(self, stamp: Path, input_file: Path, output_file: Path, pages: Union[Literal["ALL"], List[int]] = "ALL"):
		"""
		Stamp the pdf given in the input_file

		Args:
			stamp (Path): The path of the stamp pdf.
			input_file (Path): The path of the file which needs to be stamped
			output_file (Path): The path of the file to which stamped file will be stored
			pages (list or string): Pages to be stamped.
		"""

		try:
			if not os.path.exists(stamp):
				raise FileNotFoundError
			if not os.path.exists(input_file):
				raise FileNotFoundError

			stamp_page = pypdf.PdfReader(stamp).pages[0]

			writer = pypdf.PdfWriter()

			reader = pypdf.PdfReader(input_file)
			if pages == ['ALL']:
				pages = list(range(0, len(reader.pages)))
			elif pages == 'ALL':
				pages = list(range(0, len(reader.pages)))

			for page in pages:
				content_page = reader.pages[page]
				mediabox = content_page.mediabox
				content_page.merge_page(stamp_page)
				content_page.mediabox = mediabox
				writer.add_page(content_page)

			with open(output_file, 'wb') as f:
				writer.write(f)
			return "Success"

		except Exception as e:
			return e

	def lock(self, input_file: Path, output_file: Path, password: str, algorithm="AES-256-R5"):
		"""
				Locks the pdf file given in the argument input_file
				Args:
					   input_file (Path): Path of the pdf file that is going to be locked
					   output_file (Path): Path of the pdf file where the locked pdf file will be stored
					password (str): Password to be applied on the pdf
					   algorithm (str) [default: aes-256-r5]: encryption algorithm to be applied
		"""
		try:
			if not os.path.exists(input_file):
				raise FileNotFoundError

			reader = pypdf.PdfReader(input_file)
			writer = pypdf.PdfWriter(output_file)

			for page in reader.pages:
				writer.add_page(page)

			writer.encrypt(password, algorithm=algorithm)

			with open(output_file, "wb") as f:
				writer.write(f)

			return "Success"

		except Exception as e:
			return e

	def unlock(self, input_file: Path, output_file: Path, password: str, algorithm="AES-256-R5"):
		"""
				Remove the encryption from encrypted pdf
				Args:
					  input_file (Path): File which has ecryption on it
					  output_file (Path): Where to save the decrypted file
					  password (str): password of the encryption
					  algorithm (str) [default: aes-256-r5]: encryption algorithm to be applied
		"""
		try:
			if not os.path.exists(input_file):
				raise FileNotFoundError

			reader = pypdf.PdfReader(input_file)
			writer = pypdf.PdfWriter(output_file)

			if reader.is_encrypted:
				reader.decrypt(password)

			for page in reader.pages:
				writer.add_page(page)

			with open(output_file, "wb") as f:
				writer.write(f)
			return "Success"

		except Exception as e:
			return e

	def watermark(self, watermark: Path, input_file: Path, output_file: Path, page_indicies: Union[Literal["ALL"], List[int]] = "ALL"):
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
			if page_indicies == ['ALL']:
				page_indicies = list(range(len(reader.pages)))
			elif page_indicies == 'ALL':
				page_indicies = list(range(len(reader.pages)))

			writer = pypdf.PdfWriter()
			if watermark.split('.')[-1] == 'pdf':
				watermark_page = pypdf.PdfReader(watermark).pages[0]
			else:
				self.convert_images_to_pdf([watermark], watermark + '.pdf')
				watermark_page = pypdf.PdfReader(watermark+'.pdf').pages[0]

			for index in page_indicies:
				content_page = reader.pages[index]
				content_page.merge_transformed_page(watermark_page, pypdf.Transformation(), over=False)
				writer.add_page(content_page)

			with open(output_file, "wb") as f:
				writer.write(f)
			return "Success"

		except Exception as e:
			return e

    def export_to_doc(self, input_file: Path, output_file: Path):
		"""
		exports the input pdf file to docx document file.

		Args:
			input_file (Path): Path of the input file that is going to have the watermark.
			output_file (Path): Path of the pdf where the pdf will stored.
		"""
		try:
			if not os.path.exists(input_file):
				raise FileNotFoundError
			
			reader = pypdf.PdfReader(input_file)

			with open(output_file, "w") as f:
				for page in reader.pages:
					f.write(page)

			return "Success"
		except Exception as e:
			return e

if __name__=='__main__':
	funcs = functions()
	funcs.export_to_doc('test.pdf', 'test.docx')
