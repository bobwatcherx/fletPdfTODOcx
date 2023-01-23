from flet import *
from pdf2docx import Converter

import os
def main(page:Page):
	name_file = TextField(label="Rename File")
	def my_func_process(e:FilePickerResultEvent):
		path = os.getcwd()

		# GET YOU FILE ON PICKET
		for x in e.files:
			print("YOU PATH",x.path)
			pdf_file = x.path
			docx_file = path + f"/results/{name_file.value}.docx"

			try:
				res = Converter(pdf_file)
				res.convert(docx_file)
				res.close()
			except:
				# IF FAILED THE MESSAGE
				print("YOU CONVERT IS FAILED !!!!")
			else:
				# IF SUCESS CONVERT
				print("successs YES CONVERT !!!!----")
				page.snack_bar = SnackBar(
					Text("SUCCESS CONVERT ",size=30),
					bgcolor="green"

					)
				page.snack_bar.open = True
		page.update()

	filepicker = FilePicker(on_result=my_func_process)
	page.overlay.append(filepicker)
	page.add(
		Column([
		Text("CONVERT PDF TO DOCX",size=30),
		name_file,

		ElevatedButton("convert Now",
		bgcolor="blue",color="white",
		on_click=lambda _:filepicker.pick_files()
		)


			])

		)

flet.app(target=main,assets_dir="results")
