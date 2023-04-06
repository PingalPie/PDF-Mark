#!/bin/env python

import click
from pdf import *

funcs = functions()

@click.command()
@click.option('--option', help="Which manipulation you want to do")
@click.option('-i', default=False, is_flag=True)
@click.option('--input-file', 'input_file', default="None")
@click.option('--output-file', 'output_file', default="None")
@click.option('--pages', default="ALL")
@click.option('--start-page', 'start_page', default=1)
@click.option('--end-page', 'end_page', default=1)
@click.option('--stamp-file', 'stamp_file', default="None")
@click.option('--watermark-file', 'watermark_file', default="None")
def main(option, i, input_file, output_file, pages, start_page, end_page, stamp_file, watermark_file):
    if option not in funcs.__all__:
        print("Choose correct option from '", end="")
        for f in funcs.__all__:
            print(f, end=", ")
        print("'")
        exit(1)

    if i:
        output_file = input('Output File: ')
        if option == 'split_pdf':
            input_file = input('Input File: ')
            start_page = input('Start Page (default: 1): ')
            end_page = input('End Page: (default: 1) ')
            try:
                start_page = int(start_page)
                end_page = int(end_page)
            except Exception as e:
                start_page = end_page = 1
            print(funcs.split_pdf(input_file, output_file, start_page, end_page))
        elif option == 'merge_pdfs':
            pdfs = input('Pdfs to be merged (space seperated): ').split(' ')
            print(funcs.merge_pdfs(pdfs, output_pdf))

        elif option == 'reduce_pdf_size':
            input_file = input('Input File: ')
            print(funcs.reduce_pdf_size(input_file, output_file))
        elif option == 'stamp':
            input_file = input('Main File: ')
            stamp_file = input('Stamp File (pdf): ')
            pages = input('Pages on which stamp to be applied (default: ALL): ')
            pages = pages.split(',')
            print(funcs.stamp(stamp_file, input_file, output_file, pages))

        elif option == 'watermark':
            input_file = input('Main File: ')
            watermark_file = input('Watermark File (pdf): ')
            pages = input('Pages on which Watermark to be applied (default: ALL): ')
            pages = pages.split(',')
            print(funcs.watermark(watermark_file, input_file, output_file, pages))

        elif option == 'convert_images_to_pdf':
            images = input('Name of images (space seperated values):').split(' ')
            print(funcs.convert_images_to_pdf(images, output_file))

        exit()

    if option == 'split_pdf':
        print(funcs.split_pdf(input_file, output_file, start_page, end_page))
    elif option == 'reduce_pdf_size':
        print(funcs.redice_pdf_size(input_file, output_file))

    elif option == 'stamp':
        pass
    elif option == 'watermark':
        pass
    elif option == 'merge_pdfs':
        pass
    elif option == 'convert_images_to_pdf':
        pass




if __name__=='__main__':
    main()
