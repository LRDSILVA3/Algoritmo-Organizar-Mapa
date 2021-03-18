from PIL import Image, ImageFilter
import os

# pasta onde se envontra as imagens que deseja trabalhar
pathName = 'c:\\teste'

for folderName, subfolders, filenames in os.walk(pathName):
	print('O diretório corrente é  ' + folderName)
	
	cont_name = 0
	
	# percorre todos os arquivos da pasta indicada
	for filename in filenames:
		if 'ponto' in filename.lower():
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			pontos = Image.open( filename )			
			# Aplicando os filtros necessários
			pontos.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '3'
			pontos.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = pontos.split()

		if 'ctc.wmf' in filename.lower():
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			ctc = Image.open( filename )			
			# Aplicando os filtros necessários
			ctc.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '5'
			ctc.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = ctc.split()

		if 'materia organica.wmf' in filename.lower():
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			m_org = Image.open( filename )			
			# Aplicando os filtros necessários
			m_org.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '6'
			m_org.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = m_org.split()


		if ('contri' in filename.lower())and('organica' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			cm_org = Image.open( filename )			
			# Aplicando os filtros necessários
			cm_org.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '7'
			cm_org.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = cm_org.split()


		if ('fosfor' in filename.lower())and('mehli' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			fosf_meh = Image.open( filename )			
			# Aplicando os filtros necessários
			fosf_meh.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '8'
			fosf_meh.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = fosf_meh.split()


		if ('capac' in filename.lower())and('fosforo' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			cap_fosforo = Image.open( filename )			
			# Aplicando os filtros necessários
			cap_fosforo.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '9'
			cap_fosforo.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = cap_fosforo.split()

		if ('eficien' in filename.lower())and('fosforo' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			efici_fosfo = Image.open( filename )			
			# Aplicando os filtros necessários
			efici_fosfo.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '10'
			efici_fosfo.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = efici_fosfo.split()

		if 'bases' in filename.lower():
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			saturacao = Image.open( filename )			
			# Aplicando os filtros necessários
			saturacao.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '11'
			saturacao.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = saturacao.split()

		if ('calcio' in filename.lower())and('ctc' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			cal_ctc = Image.open( filename )			
			# Aplicando os filtros necessários
			cal_ctc.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '12'
			cal_ctc.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = cal_ctc.split()



		if ('magnesio' in filename.lower())and('ctc' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			mag_ctc = Image.open( filename )			
			# Aplicando os filtros necessários
			mag_ctc.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '13'
			mag_ctc.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = mag_ctc.split()

		if ('potassio' in filename.lower())and('ctc' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			pot_ctc = Image.open( filename )			
			# Aplicando os filtros necessários
			pot_ctc.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '14'
			pot_ctc.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = pot_ctc.split()


		if ('ph' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			ph_cacl = Image.open( filename )			
			# Aplicando os filtros necessários
			ph_cacl.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '15'
			ph_cacl.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = ph_cacl.split()


		if ('h' in filename.lower())and('al' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			h_al = Image.open( filename )			
			# Aplicando os filtros necessários
			h_al.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '16'
			h_al.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = h_al.split()



		if ('aluminio' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			aluminio = Image.open( filename )			
			# Aplicando os filtros necessários
			aluminio.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '17'
			aluminio.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = aluminio.split()


		if ('enxofre' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			enxofre = Image.open( filename )			
			# Aplicando os filtros necessários
			enxofre.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '18'
			enxofre.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = enxofre.split()


		if ('recom' in filename.lower())and('calci' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			recom_calci = Image.open( filename )			
			# Aplicando os filtros necessários
			recom_calci.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '19'
			recom_calci.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = recom_calci.split()



		if ('recom' in filename.lower())and('dolo' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			recom_dolo = Image.open( filename )			
			# Aplicando os filtros necessários
			recom_dolo.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '20'
			recom_dolo.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = recom_dolo.split()

		if ('recom' in filename.lower())and('p2o5' in filename.lower())and('ate cff' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			recom_pocff = Image.open( filename )			
			# Aplicando os filtros necessários
			recom_pocff.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '21'
			recom_pocff.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = recom_pocff.split()



		if ('recom' in filename.lower())and('p2o5' in filename.lower())and('ate 150 cff' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			recom_pocff150 = Image.open( filename )			
			# Aplicando os filtros necessários
			recom_pocff150.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '22'
			recom_pocff150.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = recom_pocff150.split()


		if ('recom' in filename.lower())and('p2o5' in filename.lower())and('culturas' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			recom_poculturas = Image.open( filename )			
			# Aplicando os filtros necessários
			recom_poculturas.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '23'
			recom_poculturas.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = recom_poculturas.split()


		if ('recom' in filename.lower())and('k2o' in filename.lower())and('soja' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			ko_soja = Image.open( filename )			
			# Aplicando os filtros necessários
			ko_soja.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '24'
			ko_soja.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = ko_soja.split()



		if ('recom' in filename.lower())and('k2o' in filename.lower())and('milho' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			ko_milho = Image.open( filename )			
			# Aplicando os filtros necessários
			ko_milho.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '25'
			ko_milho.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = ko_milho.split()


		if ('recom' in filename.lower())and('k2o' in filename.lower())and('trigo' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			ko_trigo= Image.open( filename )			
			# Aplicando os filtros necessários
			ko_trigo.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '26'
			ko_trigo.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = ko_trigo.split()



		if ('recom' in filename.lower())and('calcio' in filename.lower())and('culturas' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			cal_culturas = Image.open( filename )			
			# Aplicando os filtros necessários
			cal_culturas.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '27'
			cal_culturas.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = cal_culturas.split()

		if ('recom' in filename.lower())and('enxofre' in filename.lower())and('culturas' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			cal_enxofre = Image.open( filename )			
			# Aplicando os filtros necessários
			cal_enxofre.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '28'
			cal_enxofre.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = cal_enxofre.split()

		if ('recom' in filename.lower())and('n' in filename.lower())and('1a' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			recom_n1a = Image.open( filename )			
			# Aplicando os filtros necessários
			recom_n1a.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '29'
			recom_n1a.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = recom_n1a.split()


		if ('recom' in filename.lower())and('n' in filename.lower())and('2a' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			recom_n2a = Image.open( filename )			
			# Aplicando os filtros necessários
			recom_n2a.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '30'
			recom_n2a.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = recom_n2a.split()



		if ('recom' in filename.lower())and('n' in filename.lower())and('trigo' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			recom_trigo = Image.open( filename )			
			# Aplicando os filtros necessários
			recom_trigo.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '31'
			recom_trigo.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = recom_trigo.split()



		if ('manuten' in filename.lower()):
			# Abrindo o arquivo
			print('Abrindo o arquivo: ' + filename)
			manu = Image.open( filename )			
			# Aplicando os filtros necessários
			manu.filter(ImageFilter.SHARPEN)
	
			# Salvando as imagens usando um contador para renomea-las
			name_file = '32'
			manu.save(name_file, 'JPEG')
			

			# Separando as componentes das cores em RGB
			r,g,b = manu.split()




