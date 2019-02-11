import os, sys
from PyPDF2 import PdfFileReader, PdfFileWriter
from archer import db
from archer.models import Document, Partition

class CropPdf(object):
	def __init__(self, filename, filepath):
		target = os.path.join(filepath,filename[:-4])
		if not os.path.isdir(target):
			os.mkdir(target)
		print (target)	
		os.system('pdf-crop-margins -v -s -u ' + '"'+filepath+filename+'"'+' -o '+'"'+target
				+"/"+"%s(MARGINLESS).pdf" %filename[:-4]+'"')
		
		crop = 'python3 archer/pdf_crop.py -m '
		if filepath[-8:]=="death_1/":
			newdoc = Document.query.filter_by(docname = filename).first()

			os.system(crop+'"'+"0.955 0.9627 0.09 0.6985"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(ONE).pdf" %filename[:-4]+'"')
			part1 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
						url = "death_1/%s/%s(ONE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.735 0.09 0.6"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(TWO).pdf" %filename[:-4]+'"')
			part2 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 2, count = 0, flag = False, 
						url = "death_1/%s/%s(TWO).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.635 0.09 0.55"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(THREE).pdf" %filename[:-4]+'"')
			part3 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1/%s/%s(THREE).pdf" %(filename[:-4],filename[:-4]))
			
			os.system(crop+'"'+"0.955 0.585 0.09 0.49"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FOUR).pdf" %filename[:-4]+'"')
			part4 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1/%s/%s(FOUR).pdf" %(filename[:-4],filename[:-4]))
			
			os.system(crop+'"'+"0.955 0.53 0.09 0.419"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FIVE).pdf" %filename[:-4]+'"')
			part5 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 3, count = 0, flag = False, 
						url = "death_1/%s/%s(FIVE).pdf" %(filename[:-4],filename[:-4]))
			
			os.system(crop+'"'+"0.955 0.46 0.09 0.33"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SIX).pdf" %filename[:-4]+'"')
			part6 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 2, count = 0, flag = False, 
						url = "death_1/%s/%s(SIX).pdf" %(filename[:-4],filename[:-4]))
			
			os.system(crop+'"'+"0.955 0.38 0.09 0.263"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SEVEN).pdf" %filename[:-4]+'"')
			part7 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_1/%s/%s(SEVEN).pdf" %(filename[:-4],filename[:-4]))
			
			os.system(crop+'"'+"0.955 0.33 0.09 0.0713"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(EIGHT).pdf" %filename[:-4]+'"')
			part8 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 5, count = 0, flag = False, 
						url = "death_1/%s/%s(EIGHT).pdf" %(filename[:-4],filename[:-4]))

			db.session.add(part1)
			db.session.add(part2)
			db.session.add(part3)
			db.session.add(part4)
			db.session.add(part5)
			db.session.add(part6)
			db.session.add(part7)
			db.session.add(part8)
			db.session.commit()

		elif filepath[-8:]=="death_2/":
			newdoc = Document.query.filter_by(docname = filename).first()

			os.system(crop+'"'+"0.955 0.98 0.09 0.77"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(ONE).pdf" %filename[:-4]+'"')
			part1 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 3, count = 0, flag = False, 
						url = "death_2/%s/%s(ONE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.81 0.09 0.73"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(TWO).pdf" %filename[:-4]+'"')
			part2 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 2, count = 0, flag = False, 
						url = "death_2/%s/%s(TWO).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.765 0.09 0.71"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(THREE).pdf" %filename[:-4]+'"')
			part3 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_2/%s/%s(THREE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.744 0.09 0.61"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FOUR).pdf" %filename[:-4]+'"')
			part4 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 4, count = 0, flag = False, 
						url = "death_2/%s/%s(FOUR).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.635 0.09 0.56"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(FIVE).pdf" %filename[:-4]+'"')
			part5 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_2/%s/%s(FIVE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.58 0.09 0.477"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SIX).pdf" %filename[:-4]+'"')
			part6 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_2/%s/%s(SIX).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.5 0.09 0.435"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(SEVEN).pdf" %filename[:-4]+'"')
			part7 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 3, count = 0, flag = False, 
						url = "death_2/%s/%s(SEVEN).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.45 0.09 0.345"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(EIGHT).pdf" %filename[:-4]+'"')
			part8 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 3, count = 0, flag = False, 
						url = "death_2/%s/%s(EIGHT).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.368 0.09 0.3"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(NINE).pdf" %filename[:-4]+'"')
			part9 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_2/%s/%s(NINE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.32 0.09 0.19"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(TEN).pdf" %filename[:-4]+'"')
			part10 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 4, count = 0, flag = False, 
						url = "death_2/%s/%s(TEN).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.955 0.23 0.09 0.05"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(ELEVEN).pdf" %filename[:-4]+'"')
			part11 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 1, count = 0, flag = False, 
						url = "death_2/%s/%s(ELEVEN).pdf" %(filename[:-4],filename[:-4]))

			db.session.add(part1)
			db.session.add(part2)
			db.session.add(part3)
			db.session.add(part4)
			db.session.add(part5)
			db.session.add(part6)
			db.session.add(part7)
			db.session.add(part8)
			db.session.add(part9)
			db.session.add(part10)
			db.session.add(part11)
			db.session.commit()

		elif filepath[-8:]=="death_3/":
			newdoc = Document.query.filter_by(docname = filename).first()

			os.system(crop+'"'+"0.458 0.83 0 0.64"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftONE).pdf" %filename[:-4]+'"')
			part1 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_3/%s/%s(LeftONE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.458 0.685 0 0.48"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftTWO).pdf" %filename[:-4]+'"')
			part2 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_3/%s/%s(LeftTWO).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.458 0.533 0 0.325"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftTHREE).pdf" %filename[:-4]+'"')
			part3 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_3/%s/%s(LeftTHREE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.458 0.385 0 0.175"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftFOUR).pdf" %filename[:-4]+'"')
			part4 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_3/%s/%s(LeftFOUR).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"0.458 0.235 0 0.01"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(LeftFIVE).pdf" %filename[:-4]+'"')
			part5 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 6, count = 0, flag = False, 
					url = "death_3/%s/%s(LeftFIVE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"1 0.835 0.4 0.635"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightONE).pdf" %filename[:-4]+'"')
			part6 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_3/%s/%s(RightONE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"1 0.685 0.4 0.48"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightTWO).pdf" %filename[:-4]+'"')
			part7 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_3/%s/%s(RightTWO).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"1 0.535 0.4 0.325"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightTHREE).pdf" %filename[:-4]+'"')
			part8 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_3/%s/%s(RightTHREE).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"1 0.38 0.4 0.17"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightFOUR).pdf" %filename[:-4]+'"')
			part9 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_3/%s/%s(RightFOUR).pdf" %(filename[:-4],filename[:-4]))

			os.system(crop+'"'+"1 0.235 0.4 0"
						+'"'+' -i '+'"'+target+"/"+"%s(MARGINLESS).pdf" %filename[:-4]
						+'"'+' -o '+'"'+target+"/"+"%s(RightFIVE).pdf" %filename[:-4]+'"')
			part10 = Partition(doc_id = newdoc.id, editor1 = 0, editor2 = 0, column = 7, count = 0, flag = False, 
					url = "death_3/%s/%s(RightFIVE).pdf" %(filename[:-4],filename[:-4]))


			db.session.add(part1)
			db.session.add(part2)
			db.session.add(part3)
			db.session.add(part4)
			db.session.add(part5)
			db.session.add(part6)
			db.session.add(part7)
			db.session.add(part8)
			db.session.add(part9)
			db.session.add(part10)
			db.session.commit()