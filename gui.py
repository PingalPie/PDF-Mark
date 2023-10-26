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

import tkinter as tk
from pdf import functions
from tkinter import filedialog as fd
from tkinter import simpledialog as sd

class window(tk.Tk):
	def __init__(self):
		super().__init__()
		self.geometry('462x300')
		self.title('Pdf Manipulator')
		self.funcs = functions()

		# MENU BAR
		self.menu = tk.Menu(self)
		self.config(menu=self.menu)

		home = tk.Menu(self.menu, tearoff=0)
		self.menu.add_cascade(label="Home", menu=home)
		home.add_command(label="HomePage", command=lambda: (self.frame.pack_forget(), self.window()))
		home.add_command(label="About", command=lambda: (self.frame.pack_forget(), self.about()))
		home.add_command(label="Help", command=lambda: (self.frame.pack_forget(), self.help()))


	def about(self):
		self.frame = tk.Frame(self)
		title = tk.Label(self.frame, text="ABOUT PAGE", font="sans-serif 30")

		copyright = tk.Label(
			self.frame,
			text="""This is a tool which can be used to do many operations on pdf files.
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
""")
		info = tk.Label(self.frame, text="This software is made by PingalPie (https://github.com/PingalPie)")

		title.pack()
		copyright.pack()
		info.pack()
		self.frame.pack()

	def help(self):
		self.frame = tk.Frame(self)
		title = tk.Label(self.frame, text="Feedback page", font="sans-serif 30")
		content = tk.Label(self.frame, text="If you encountered any error please report it to https://github.com/pingalpie/pdf-manipulator")

		title.pack()
		content.pack()
		self.frame.pack()

	def window(self):
		"""

		"""
		self.frame = tk.Frame(self)
		labelf = tk.Label(self.frame, text='Options: ')
		option = tk.StringVar()
		option.set("Choose one option")
		options_all = self.funcs.__all__
		options = []

		def select_answers():
			if option.get()!= "Choose one option":
				return self.options(option.get())
			return

		for i in options_all:
			options.append(i.replace('_', ' '))

		option_menu = tk.OptionMenu(self.frame, option, *options)

		submit = tk.Button(self.frame, text="Submit", command=select_answers)

		labelf.grid(column=1, row=1)
		option_menu.grid(column=2, row=1)
		submit.grid(column=1, row=2)
		self.frame.pack()

	def options(self, selected_option: str):
		"""

		"""
		self.frame1.pack_forget()
		selected_option = selected_option.replace(' ', '_')
		match selected_option:
			case 'split_pdf':
				# Creating required labels and frames
				title = tk.Label(self, text='Split Pdf', font='monospace 20')
				title.pack()
				self.frame = tk.Frame(self)

				# Creating variables for entryboxes
				input_path = tk.StringVar()
				input_path.set('')
				output_path = tk.StringVar()
				output_path.set('')
				start_page = tk.StringVar()
				start_page.set('')
				end_page = tk.StringVar()
				end_page.set('')

				# Actual function which will do the task
				def split_pdfs(input_path, output_path, start_page, end_page):
					result = self.funcs.split_pdf(str(input_path), str(output_path), int(start_page), int(end_page))
					self.frame.pack_forget()
					self.frame2 = tk.Frame(self)
					label12 = tk.Label(frame2, text=result)
					label12.pack()
					back_to_home = tk.Button(frame2, text='Back to HomePage', command=lambda: (title.pack_forget(), frame2.pack_forget(), self.window()))
					back_to_home.pack()
					self.frame2.pack()

				# Creating entry boxes
				input_path_box = tk.Entry(frame, textvariable=input_path)
				output_path_box = tk.Entry(frame, textvariable=output_path)
				start_page_box = tk.Entry(frame, textvariable=start_page)
				end_page_box = tk.Entry(frame, textvariable=end_page)

				# Creating Labels for entry boxes
				input_path_label = tk.Label(frame, text='Input Path: ')
				output_path_label = tk.Label(frame, text='Output Path: ')
				start_page_label = tk.Label(frame, text='Start Page: ')
				end_page_label = tk.Label(frame, text='End Page: ')

				# Creating required buttons
				input_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (input_path.set(self.funcs.select_file_pdf()), input_path_box.update()))
				output_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (output_path.set(self.funcs.select_output_file_pdf()), output_path_box.update()))
				submit_button = tk.Button(frame, text='Submit', command=lambda: split_pdfs(input_path=input_path.get(), output_path=output_path.get(), start_page=start_page.get(), end_page=end_page.get()))

				back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

				# Packing everything
				input_path_label.grid(column=1, row=1)
				output_path_label.grid(column=1, row=2)
				start_page_label.grid(column=1, row=3)
				end_page_label.grid(column=1, row=4)

				input_path_icon_file.grid(column=3, row=1, padx=3, pady=2)
				output_path_icon_file.grid(column=3, row=2, padx=3, pady=2)

				input_path_box.grid(column=2, row=1)
				output_path_box.grid(column=2, row=2)
				start_page_box.grid(column=2, row=3, pady=2)
				end_page_box.grid(column=2, row=4, pady=3)

				submit_button.grid(column=1, row=5)

				back_to_homepage.grid(column=3, row=5, pady=10)

				self.frame.pack()

			case 'reduce_pdf_size':
				# Creating required labels and frames
				title = tk.Label(self, text="Reduce file size of a pdf", font='Sans-Serif 20')
				title.pack()
				self.frame = tk.Frame(self)

				# Creating variables for entryboxes
				input_path = tk.StringVar()
				input_path.set('')
				output_path = tk.StringVar()
				output_path.set('')

				# Actual function which will do the task
				def reduce_file_size(file, out_file):
					result = self.funcs.reduce_pdf_size(file, out_file)
					self.frame.pack_forget()
					self.frame2 = tk.Frame(self)
					label12 = tk.Label(frame2, text=result, font='sans-serif 15')
					label12.pack()
					back_to_home = tk.Button(frame2, text='Back to HomePage', command=lambda: (title.pack_forget(), frame2.pack_forget(), self.window()))
					back_to_home.pack()
					frame2.pack()

				# Creating entry boxes
				input_path_box = tk.Entry(frame, textvariable=input_path)
				output_path_box = tk.Entry(frame, textvariable=output_path)

				# Creating Labels for entry boxes
				input_path_label = tk.Label(frame, text='Input Path: ')
				output_path_label = tk.Label(frame, text='Output Path: ')

				# Creating required buttons
				input_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (input_path.set(self.funcs.select_file_pdf()), input_path_box.update()))
				output_path_icon_file = tk.Button(frame, text="Open File", command=lambda: (output_path.set(self.funcs.select_output_file_pdf()), output_path_box.update()))
				submit_button = tk.Button(frame, text='Submit', command=lambda: reduce_file_size(input_path.get(), output_path.get()))
				back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

				# Packing everything
				input_path_label.grid(column=1, row=1)
				output_path_label.grid(column=1, row=2)

				input_path_icon_file.grid(column=3, row=1, padx=3, pady=2)
				output_path_icon_file.grid(column=3, row=2, padx=3, pady=2)

				input_path_box.grid(column=2, row=1)
				output_path_box.grid(column=2, row=2)

				submit_button.grid(column=1, row=5)

				back_to_homepage.grid(column=3, row=5, pady=10)

				self.frame.pack()

			case 'merge_pdfs':
				# Creating required labels and frames
				title = tk.Label(self, text="Merge Pdfs", font='Sans-Serif 20')
				instructions = tk.Label(self, text='Have values in the entry box of list of files comma seperated', relief=tk.SUNKEN, anchor='s')
				self.frame = tk.Frame(self)

				# Creating variables for entryboxes
				files = tk.StringVar()
				files.set('')
				output_path = tk.StringVar()
				output_path.set('')

				# Actual function which will do the task
				def merge_pdfs(output_file):
					list_of_files = files.get().split(',')
					result = self.funcs.merge_pdfs(list_of_files, output_file)
					self.frame.pack_forget()
					self.frame2 = tk.Frame(self)
					label12 = tk.Label(frame2, text=result, font='sans-serif 15')
					label12.pack()
					back_to_home = tk.Button(frame2, text='Back to HomePage', command=lambda: (instructions.pack_forget(), title.pack_forget(), frame2.pack_forget(), self.window()))
					back_to_home.pack()
					self.frame2.pack()

				# Creating entry boxes
				files_box = tk.Entry(frame, textvariable=files)
				output_path_box = tk.Entry(frame, textvariable=output_path)

				# Creating Labels for entry boxes
				files_label = tk.Label(frame, text='Files: ')
				output_path_label = tk.Label(frame, text='Output Path: ')

				# Creating required buttons
				submit_button = tk.Button(frame, text='Submit', command=lambda: (merge_pdfs(output_path.get())))
				back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (instructions.pack_forget(), title.pack_forget(), frame.pack_forget(), self.window()))
				if files.get() == '':
					files_open_file = tk.Button(frame, text="Open File", command=lambda: (files.set(self.funcs.select_file_pdf()),files_box.update()))
				files_open_file = tk.Button(frame, text="Open File", command=lambda: (files.set(files.get()+','+self.funcs.select_file_pdf()),files_box.update()))
				output_open_file = tk.Button(frame, text="Open File", command=lambda: (output_path.set(output_path.get()+','+self.funcs.select_output_file_pdf()), output_path_box.update()))

				# Packing everything
				files_label.grid(column=1, row=1)
				output_path_label.grid(column=1, row=3)

				files_box.grid(column=2, row=1)
				output_path_box.grid(column=2, row=3)

				files_open_file.grid(column=3, row=1, padx=3, pady=2)
				# file2_.grid(column=3, row=2, padx=3, pady=2)
				output_open_file.grid(column=3, row=3, padx=3, pady=2)

				submit_button.grid(column=1, row=4)
				back_to_homepage.grid(column=3, row=5, pady=10)

				title.pack()
				instructions.pack(side='bottom', fill=tk.X)

				self.frame.pack()

			case 'convert_images_to_pdf':

				# Creating required labels and frames
				title = tk.Label(self, text='convert_images_to_pdf', font='Sans-Serif 20')
				list_of_files_instructions = tk.Label(self, text='Have values in the entry box of list of files comma seperated', relief=tk.SUNKEN, anchor='s')
				self.frame = tk.Frame(self)

				# Creating variables for entryboxes
				list_of_file = tk.StringVar()
				list_of_file.set('')
				output_path = tk.StringVar()
				output_path.set('')

				# Actual function which will do the task
				def convert_images_to_pdf(list_of_images: list, output_pdf: str):
					list_of_files_instructions.pack_forget()
					self.frame.pack_forget()
					result = self.funcs.convert_images_to_pdf(list_of_images, output_pdf)
					lab = tk.Label(self, text=result)
					go_to_homepage = tk.Button(self, text='Back to homepage', command=lambda: (lab.pack_forget(), title.pack_forget(), self.window()))
					lab.pack()
					go_to_homepage.pack()

				# Creating Labels for entry boxes
				list_of_file_label = tk.Label(frame, text='List of files: ')
				output_path_label = tk.Label(frame, text='Output filename: ')

				# Creating entry boxes
				list_of_file_entry = tk.Entry(frame, textvariable=list_of_file)
				output_path_entry = tk.Entry(frame, textvariable=output_path)

				# Creating required buttons
				if list_of_file.get() == '':
					list_of_files_open_file = tk.Button(frame, text="Open File", command=lambda: (list_of_file.set(self.funcs.select_file_image()),list_of_file_entry.update()))
				list_of_files_open_file = tk.Button(frame, text="Open File", command=lambda: (list_of_file.set(list_of_file.get()+','+self.funcs.select_file_image()),list_of_file_entry.update()))
				output_path_open_file = tk.Button(frame, text="Open File", command=lambda: (output_path.set(self.funcs.select_output_file_pdf()), output_path_box.update()))
				submit_button = tk.Button(frame, text='Submit', command=lambda: (convert_images_to_pdf(list_of_file.get().split(',') ,output_path.get())))
				back_to_homepage = tk.Button(frame, text='Back to homepage', command=lambda: (frame.pack_forget(), self.window()))

				# Packing everything
				list_of_file_label.grid(column=1, row=1)
				output_path_label.grid(column=1, row=2)

				list_of_file_entry.grid(column=2, row=1)
				output_path_entry.grid(column=2, row=2)

				list_of_files_open_file.grid(column=3, row=1, padx=3, pady=3)
				output_path_open_file.grid(column=3, row=2, padx=3)

				submit_button.grid(column=1, row=3)
				back_to_homepage.grid(column=3, row=5)

				title.pack()

				self.frame.pack()

				list_of_files_instructions.pack(side='bottom', fill=tk.X)

			case 'watermark':
				# Changing geometry
				self.geometry('650x300')
				# Creating frame and title
				title = tk.Label(self, text="Watermark", font='sans-serif 20')
				indicies_instructions = tk.Label(self, text="Page numbers should be written in comma seperated values, default: all")
				self.frame = tk.Frame(self)

				# Creating variables
				content_pdf = tk.StringVar()
				watermark_file = tk.StringVar()
				output_pdf = tk.StringVar()
				page_indicies = tk.StringVar()
				page_indicies.set('ALL')
				watermark_file.set('')
				content_pdf.set('')

				# Function which works on pressing submit button
				def watermark():
					self.frame.pack_forget()
					indicies_instructions.pack_forget()
					result = self.funcs.watermark(watermark_file.get(), content_pdf.get(), output_pdf.get(), page_indicies.get().split(','))
					print(result)
					lab = tk.Label(self, text=result)
					go_to_homepage = tk.Button(self, text='Back to homepage', command=lambda: (lab.pack_forget(), title.pack_forget(), go_to_homepage.pack_forget(), self.window()))

					lab.pack()
					go_to_homepage.pack()

				# Making Entry boxes
				output_pdf_entry = tk.Entry(frame, textvariable=output_pdf)
				content_pdf_entry = tk.Entry(frame, textvariable=content_pdf)
				watermark_entry = tk.Entry(frame, textvariable=watermark_file)
				page_indices_entry = tk.Entry(frame, textvariable=page_indicies)

				# Making Labels
				output_pdf_label = tk.Label(frame, text="Output file:")
				content_pdf_label = tk.Label(frame, text='Main pdf:')
				watermark_label = tk.Label(frame, text="Watermark file:")
				page_indicies_label = tk.Label(frame, text="Page numbers on which watermark to be applied: ")

				# Making buttons
				output_pdf_open = tk.Button(frame, text='Open File', command=lambda: (output_pdf.set(self.funcs.select_file_pdf()), ))
				content_pdf_open = tk.Button(frame, text='Open File', command=lambda: (output_pdf.set(self.funcs.select_file_pdf()), ))

				watermark_open = tk.Button(frame, text="Open File", command=lambda: (watermark_file.set(self.funcs.select_output_file_image()), watermark_entry.update()))
				submit = tk.Button(frame, text="Submit", command=lambda: (frame.pack_forget(), watermark()))
				back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

				# Packing Everything
				content_pdf_label.grid(column=1, row=1)
				watermark_label.grid(column=1, row=2)
				output_pdf_label.grid(column=1, row=3)
				page_indicies_label.grid(column=1, row=4)

				content_pdf_entry.grid(column=2, row=1)
				watermark_entry.grid(column=2, row=2)
				output_pdf_entry.grid(column=2, row=3)
				page_indices_entry.grid(column=2, row=4)

				content_pdf_open.grid(column=3, row=1, padx=3, pady=1)
				watermark_open.grid(column=3, row=2, padx=3, pady=1)
				output_pdf_open.grid(column=3, row=3, padx=3, pady=1)

				submit.grid(column=1, row=5)
				back_to_homepage.grid(column=3, row=5)


				title.pack()
				indicies_instructions.pack(side='bottom', fill=tk.X)

				self.frame.pack()

			case "unlock_pdf":
				self.frame = tk.Frame(self)
				title = tk.Label(self, text="Unlock PDF", font="sans-serif 20")

				# Variables
				input_pdf = tk.StringVar()
				output_pdf = tk.StringVar()
				password = tk.StringVar()
				input_pdf.set('')
				output_pdf.set('')
				password.set('')

				# Function which works on pressing submit button
				def unlock():
					self.frame.pack_forget()
					result = self.funcs.unlock(input_pdf.get(), output_pdf.get(), password.get())
					lab = tk.Label(self, text=result)
					go_to_homepage = tk.Button(self, text='Back to homepage', command=lambda: (lab.pack_forget(), title.pack_forget(), go_to_homepage.pack_forget(), self.window()))

					lab.pack()
					go_to_homepage.pack()


				# Entry Boxes
				input_pdf_entry = tk.Entry(frame, textvariable=input_pdf)
				output_pdf_entry = tk.Entry(frame, textvariable=output_pdf)
				password_entry = tk.Entry(frame, textvariable=password)

				# Labels
				input_pdf_label = tk.Label(frame, text="Input file:")
				output_pdf_label = tk.Label(frame, text="Output file:")
				password_label = tk.Label(frame, text="Password:")

				# Buttons
				input_pdf_open = tk.Button(frame, text='Open File', command=lambda: (input_pdf.set(self.funcs.select_file_pdf()), ))

				submit = tk.Button(frame, text="Submit", command=lambda: (frame.pack_forget(), unlock()))
				back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

				# Packing Everything
				input_pdf_label.grid(column=1, row=1)
				output_pdf_label.grid(column=1, row=2)
				password_label.grid(column=1, row=3)

				input_pdf_entry.grid(column=2, row=1)
				output_pdf_entry.grid(column=2, row=2)
				password_entry.grid(column=2, row=3)

				input_pdf_open.grid(column=3, row=1, padx=3, pady=1)

				submit.grid(column=1, row=5)
				back_to_homepage.grid(column=3, row=5)


				title.pack()
				self.frame.pack()


			case "lock_pdf":
				self.frame = tk.Frame(self)
				title = tk.Label(self, text="Lock PDF", font="sans-serif 20")

				# Variables
				input_pdf = tk.StringVar()
				output_pdf = tk.StringVar()
				password = tk.StringVar()
				input_pdf.set('')
				output_pdf.set('')
				password.set('')

				# Function which works on pressing submit button
				def lock():
					self.frame.pack_forget()
					result = self.funcs.lock(input_pdf.get(), output_pdf.get(), password.get())
					lab = tk.Label(self, text=result)
					go_to_homepage = tk.Button(self, text='Back to homepage', command=lambda: (lab.pack_forget(), title.pack_forget(), go_to_homepage.pack_forget(), self.window()))

					lab.pack()
					go_to_homepage.pack()


				# Entry Boxes
				input_pdf_entry = tk.Entry(frame, textvariable=input_pdf)
				output_pdf_entry = tk.Entry(frame, textvariable=output_pdf)
				password_entry = tk.Entry(frame, textvariable=password)

				# Labels
				input_pdf_label = tk.Label(frame, text="Input file:")
				output_pdf_label = tk.Label(frame, text="Output file:")
				password_label = tk.Label(frame, text="Password:")

				# Buttons
				input_pdf_open = tk.Button(frame, text='Open File', command=lambda: (input_pdf.set(self.funcs.select_file_pdf()), ))

				submit = tk.Button(frame, text="Submit", command=lambda: (frame.pack_forget(), lock()))
				back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

				# Packing Everything
				input_pdf_label.grid(column=1, row=1)
				output_pdf_label.grid(column=1, row=2)
				password_label.grid(column=1, row=3)

				input_pdf_entry.grid(column=2, row=1)
				output_pdf_entry.grid(column=2, row=2)
				password_entry.grid(column=2, row=3)

				input_pdf_open.grid(column=3, row=1, padx=3, pady=1)

				submit.grid(column=1, row=5)
				back_to_homepage.grid(column=3, row=5)

				title.pack()

				self.frame.pack()


			case "stamp":
				# Changing geometry
				self.geometry('650x300')
				# Creating frame and title
				title = tk.Label(self, text="Stamp", font='sans-serif 20')
				indicies_instructions = tk.Label(self, text="Page numbers should be written in comma seperated values, default: all")
				self.frame = tk.Frame(self)

				# Creating variables
				content_pdf = tk.StringVar()
				stamp_file = tk.StringVar()
				output_pdf = tk.StringVar()
				page_indicies = tk.StringVar()
				page_indicies.set('ALL')
				stamp_file.set('')
				content_pdf.set('')

				# Function which works on pressing submit button
				def stamp():
					self.frame.pack_forget()
					indicies_instructions.pack_forget()
					result = self.funcs.stamp(stamp_file.get(), content_pdf.get(), output_pdf.get(), page_indicies.get().split(','))
					lab = tk.Label(self, text=result)
					go_to_homepage = tk.Button(self, text='Back to homepage', command=lambda: (lab.pack_forget(), title.pack_forget(), go_to_homepage.pack_forget(), self.window()))

					lab.pack()
					go_to_homepage.pack()

				# Making Entry boxes
				output_pdf_entry = tk.Entry(frame, textvariable=output_pdf)
				content_pdf_entry = tk.Entry(frame, textvariable=content_pdf)
				stamp_entry = tk.Entry(frame, textvariable=stamp_file)
				page_indices_entry = tk.Entry(frame, textvariable=page_indicies)

				# Making Labels
				output_pdf_label = tk.Label(frame, text="Output file:")
				content_pdf_label = tk.Label(frame, text='Main pdf:')
				stamp_label = tk.Label(frame, text="Stamp file:")
				page_indicies_label = tk.Label(frame, text="Page numbers on which stamp to be applied: ")

				# Making buttons
				output_pdf_open = tk.Button(frame, text='Open File', command=lambda: (output_pdf.set(self.funcs.select_file_pdf()), ))
				content_pdf_open = tk.Button(frame, text='Open File', command=lambda: (output_pdf.set(self.funcs.select_file_pdf()), ))

				stamp_open = tk.Button(frame, text="Open File", command=lambda: (stamp_file.set(self.funcs.select_output_file_image()), watermark_entry.update()))
				submit = tk.Button(frame, text="Submit", command=lambda: (frame.pack_forget(), stamp()))
				back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

				# Packing Everything
				content_pdf_label.grid(column=1, row=1)
				stamp_label.grid(column=1, row=2)
				output_pdf_label.grid(column=1, row=3)
				page_indicies_label.grid(column=1, row=4)

				content_pdf_entry.grid(column=2, row=1)
				stamp_entry.grid(column=2, row=2)
				output_pdf_entry.grid(column=2, row=3)
				page_indices_entry.grid(column=2, row=4)

				content_pdf_open.grid(column=3, row=1, padx=3, pady=1)
				stamp_open.grid(column=3, row=2, padx=3, pady=1)
				output_pdf_open.grid(column=3, row=3, padx=3, pady=1)

				submit.grid(column=1, row=5)
				back_to_homepage.grid(column=3, row=5)


				title.pack()
				indicies_instructions.pack(side='bottom', fill=tk.X)
				self.frame.pack()


			case _:
				title = tk.Label(self, text='Choose correct option.')
				self.frame = tk.Frame(self)

				back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

				back_to_homepage.pack()
				self.frame.pack()
				title.pack()


if __name__=='__main__':
	gui = window()
	gui.window()
	gui.mainloop()
