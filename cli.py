import argparse
from pdf import functions
import sys

funcs = functions()

option = sys.argv

parser = argparse.ArgumentParser()

if len(option)<2:
    print('Enter correct information')
    print(f"Usage: {option[0]} ['split', 'reduce_size', 'merge_pdfs', 'convert_images'] (option related to the option selected) ")
    exit(1)

match option[1]:
    case 'split_pdf':
        parser.add_argument('Option', help='Manipulator option to use on the given pdf')
        parser.add_argument('input_file', help='Input path of the file')
        parser.add_argument('output_file', help='Path to the file where to save the splitted pdf')
        parser.add_argument('start_page', help='Starting page for the input pdf', type=int)
        parser.add_argument('end_page', help='Ending page for the output pdf', type=int)
    
    case 'reduce_size':
        parser.add_argument('Option', help='Manipulator option to use on the given pdf')
        parser.add_argument('input_file', help='Input path of the file')
        parser.add_argument('output_file', help='Path to the file where to save the splitted pdf')
    
    case 'merge_pdfs':
        parser.add_argument('Option', help='Manipulator option to use on the given pdf')
        parser.add_argument('output_file', help='Path to the file where to save the splitted pdf')
        parser.add_argument('list_of_files', nargs='+', help='All the filenames that needed to be combined')
    
    case 'convert_images':
        parser.add_argument('Option', help='Manipulator option to use on the given pdf')
        parser.add_argument('output_file', help='Path to the file where to save the combined pdf')
        parser.add_argument('list_of_files', nargs='+', help='All the filenames that needed to be combined')
        
    case _:
        print(option)
        print('Error')
        exit(1)

args = parser.parse_args()

match args.Option:
    case 'split_pdf':
        result = funcs.split_pdf(args.input_file, args.output_file, args.start_page, args.end_page)
        print(result)
    
    case 'reduce_size':
        print(funcs.reduce_pdf_size(args.input_file, args.output_file))

    case 'merge_pdfs':
        print(funcs.merge_pdfs(output_file=args.output_file, list_of_files=args.list_of_files))
    
    case 'convert_images':
        print(funcs.convert_images_to_pdf(output_path=args.output_file, list_of_images=args.list_of_files))