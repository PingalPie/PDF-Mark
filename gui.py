import tkinter as tk
from pdf import *
from tkinter import filedialog as fd
from tkinter import simpledialog as sd

class window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('462x336')
        self.title('Pdf Manipulator')
        self.funcs = functions()

    def window(self):
        """
        
        """
        self.frame1 = tk.Frame(self)
        labelf = tk.Label(self.frame1, text='Options: ')
        option = tk.StringVar()
        option.set("Choose one option")
        options = []

        def select_answers():
            if option.get() == "Choose one option":
                return
            self.options(option.get())
            return

        for function in dir(functions):
            if not function.startswith('__') and not function=='select_file_pdf' and not function=='select_file_image' and not function=='select_output_file_pdf':
                options.append(function)

        option_menu = tk.OptionMenu(self.frame1, option, *options)
            
        submit = tk.Button(self.frame1, text="Submit", command=select_answers)

        labelf.grid(column=1, row=1)
        option_menu.grid(column=2, row=1)
        submit.grid(column=1, row=2)
        self.frame1.pack()

    def options(self, selected_option):
        """
        
        """
        self.frame1.pack_forget()
        match selected_option:
            case 'split_pdf':
                # Creating required labels and frames
                title = tk.Label(self, text='Split Pdf', font='monospace 20')
                title.pack()
                frame = tk.Frame(self)
                
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
                    frame.pack_forget()
                    frame2 = tk.Frame(self)
                    label12 = tk.Label(frame2, text=result)
                    label12.pack()
                    back_to_home = tk.Button(frame2, text='Back to HomePage', command=lambda: (title.pack_forget(), frame2.pack_forget(), self.window()))
                    back_to_home.pack()
                    frame2.pack()

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

                frame.pack()
            
            case 'reduce_pdf_size':
                # Creating required labels and frames
                title = tk.Label(self, text="Reduce file size of a pdf", font='Sans-Serif 20')
                title.pack()
                frame = tk.Frame(self)

                # Creating variables for entryboxes
                input_path = tk.StringVar()
                input_path.set('')
                output_path = tk.StringVar()
                output_path.set('')

                # Actual function which will do the task
                def reduce_file_size(file, out_file):
                    result = self.funcs.reduce_pdf_size(file, out_file)
                    frame.pack_forget()
                    frame2 = tk.Frame(self)
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

                frame.pack()
            
            case 'merge_pdfs':
                # Creating required labels and frames
                title = tk.Label(self, text="Merge Pdfs", font='Sans-Serif 20')
                instructions = tk.Label(self, text='Have values in the entry box of list of files comma seperated', relief=tk.SUNKEN, anchor='s')
                frame = tk.Frame(self)

                # Creating variables for entryboxes
                files = tk.StringVar()
                files.set('')
                output_path = tk.StringVar()
                output_path.set('')

                # Actual function which will do the task
                def merge_pdfs(output_file):
                    list_of_files = files.get().split(',')
                    result = self.funcs.merge_pdfs(list_of_files, output_file)
                    frame.pack_forget()
                    frame2 = tk.Frame(self)
                    label12 = tk.Label(frame2, text=result, font='sans-serif 15')
                    label12.pack()
                    back_to_home = tk.Button(frame2, text='Back to HomePage', command=lambda: (instructions.pack_forget(), title.pack_forget(), frame2.pack_forget(), self.window()))
                    back_to_home.pack()
                    frame2.pack()

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
                frame.pack()

            case 'convert_images_to_pdf':

                # Creating required labels and frames
                title = tk.Label(self, text='convert_images_to_pdf', font='Sans-Serif 20')
                list_of_files_instructions = tk.Label(self, text='Have values in the entry box of list of files comma seperated', relief=tk.SUNKEN, anchor='s')
                frame = tk.Frame(self)

                # Creating variables for entryboxes
                list_of_file = tk.StringVar()
                list_of_file.set('')
                output_path = tk.StringVar()
                output_path.set('')

                # Actual function which will do the task
                def convert_images_to_pdf(list_of_images: list, output_pdf: str):
                    list_of_files_instructions.pack_forget()
                    frame.pack_forget()
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

                frame.pack()

                list_of_files_instructions.pack(side='bottom', fill=tk.X)

            case _:
                title = tk.Label(self, text='Choose correct option.')
                frame = tk.Frame(self)
                
                back_to_homepage = tk.Button(frame, text='Back to HomePage', command=lambda: (title.pack_forget(), frame.pack_forget(), self.window()))

                back_to_homepage.pack()
                frame.pack()
                title.pack()


if __name__=='__main__':
    gui = window()
    gui.window()
    gui.mainloop()