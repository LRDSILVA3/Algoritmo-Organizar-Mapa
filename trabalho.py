from PIL import Image, ImageFilter
import os

# pasta onde se envontra as imagens que deseja trabalhar
pathName = 'C:\\Users\Lucas\Desktop\Projetos\Abrir e converter imagens'

for folderName, subfolders, filenames in os.walk(pathName):
	print('O diretório corrente é  ' + folderName)
	
	cont_name = 0
	
	# percorre todos os arquivos da pasta indicada
	for filename in filenames:
		if 'alumin' in filename.lower():
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			arq = Image.open( filename )			
			# Aplicando os filtros necessários
			arq.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '1.jpg'
			arq.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = arq.split()
