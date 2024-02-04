#!/bin/env python
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

import click
from pdf import *

funcs = functions()

@click.group()
def cli():
	pass

@cli.command("split_pdf")
@click.option("-i", "--input-file", prompt_required=True, prompt=True, multiple=False)
@click.option("-o", "--output-file", prompt_required=True, prompt=True, multiple=False)
@click.option("-s", "--start-page", default=1, prompt=True, multiple=False)
@click.option("-e", "--end-page", default=1, prompt=True, multiple=False)
def split_pdf(input_file, output_file, start_page, end_page):
	result = funcs.split_pdf(input_file, output_file, int(start_page), int(end_page))
	click.echo(result)

@cli.command("merge_pdfs")
@click.option("-o", '--output-file', prompt_required=True, prompt=True, multiple=False)
@click.option("-i", "--input-files", multiple=True)
def merge_pdfs(output_file, input_files):
	result = funcs.merge_pdfs(input_files, output_file)
	click.echo(result)

@cli.command("reduce_pdf_size")
@click.option('-i', '--input-file', prompt=True, multiple=False)
@click.option('-o', '--output-file', prompt=True, multiple=False)
def reduce_pdf_size(input_file, output_file):
	result = funcs.compress(file=input_file, reduced_file_name=output_file)
	click.echo(result)

@cli.command("stamp")
@click.option('-i', '--input-file', prompt=True, multiple=False)
@click.option('-o', '--output-file', prompt=True, multiple=False)
@click.option('-s', '--stamp-pdf', prompt=True, multiple=False)
def stamp(input_file, stamp_pdf, output_file):
	result = funcs.stamp(stamp=stamp_pdf, input_file=input_file, output_file=output_file)
	click.echo(result)

@cli.command("watermark")
@click.option('-i', '--input-file', prompt=True, multiple=False)
@click.option('-o', '--output-file', prompt=True, multiple=False)
@click.option('-w', '--watermark-pdf', prompt=True, multiple=False)
def watermark(input_file, watermark_pdf, output_file):
	result = funcs.watermark(watermark=watermark_pdf, input_file=input_file, output_file=output_file)
	click.echo(result)

@cli.command("images_to_pdf")
@click.option("-o", '--output-file', prompt_required=True, prompt=True, multiple=False)
@click.option("-i", "--input-files", multiple=True)
def images_to_pdf(output_file, input_files):
	result = funcs.convert_images_to_pdf(list_of_images=input_file, output_path=output_file)
	click.echo(result)

@cli.command("lock")
@click.option('-i', '--input-file', prompt=True, multiple=False)
@click.option('-o', '--output-file', prompt=True, multiple=False)
@click.option("-p", "--password", prompt=True, hide_input=True, confirmation_prompt=True)
def lock(input_file, output_file, password):
	result = funcs.lock(input_file=input_file, output_file=output_file, password=password)
	click.echo(result)

@cli.command("unlock")
@click.option('-i', '--input-file', prompt=True, multiple=False)
@click.option('-o', '--output-file', prompt=True, multiple=False)
@click.option("-p", "--password", prompt=True, hide_input=True, confirmation_prompt=False)
def unlock(input_file, output_file, password):
	result = funcs.unlock(input_file=input_file, output_file=output_file, password=password)
	click.echo(result)



if __name__=='__main__':
    cli()
