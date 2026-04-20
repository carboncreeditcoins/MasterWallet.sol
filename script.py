import http.client
import csv
import json
import datetime
import mimetypes

conn = http.client.HTTPSConnection("aprovadoapp.com")

Id = "6368996"
Nome =  "Informática"
NomeResumido = "Informática"
Cor = "#FF69B4"
IdConteudo = "8960432"


'''
Id = "6369044"
Nome =  "Legislação Especial"
NomeResumido = "Legislação Espe..."
Cor = "#EE0000"
IdConteudo = "8957622"


Id = "6369063"
Nome =  "Português"
NomeResumido = "Português"
Cor = "#0000FF"
IdConteudo = "8957637"

Id = "6369007"
Nome =  "Raciocínio Lógico"
NomeResumido = "Raciocínio Lógi..."
Cor = "#F4A460"
IdConteudo = "8960431"

Id = "6370590"
Nome =  "Redação"
NomeResumido = "Redação"
Cor = "#F4A460"
IdConteudo = "8960429"

'''

with open('concurso1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if(row[1] == Nome):
            print(1)
            print(row[0] + " = " + row[2])

            t = row[2]
            h,m= t.split(':')

            duracao = str(int(datetime.timedelta(hours=int(h),minutes=int(m)).total_seconds()))+"000"
            print(duracao)

            dataInicio= row[0]
            d,m,a= dataInicio.split('/')
            dataNumero = str(datetime.datetime(int(a),int(m),int(d)).timestamp())
            print(dataNumero)

            print('\n')
            
            payload = '''{
                "Id": 0,
                "Materia": {
                    "Id": '''+ Id +''',
                    "Nome": "'''+ Nome +'''",
                    "NomeResumido": "''' + NomeResumido + '''",
                    "Cor": "'''+ Cor +'''"
                },
                "Tipo": "manual",
                "Conteudo": {
                    "Id": '''+ IdConteudo +''',
                    "Nome": "Retroativo",
                    "Cor": "",
                    "NomeResumido": "Retroativo"
                },
                "NovoConteudoNome": "",
                "DataInicio": "'''+ dataInicio + '''" ,
                "HoraInicio": "00:01",
                "Anotacoes": "",
                "Duracao": '''+ duracao +''',
                "DataNumero": '''+ dataNumero +''',
                "PossuiFacebook": false,
                "CompartilharFacebook": false,
                "PaginaAnterior": null
            }'''

            payload = payload.encode('utf-8')

            headers = {
            'Cookie': '__utmc=73562946; __utmz=73562946.1592410949.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); aprovado=A682FAFBD6FDCB66DC25E692A1A7DC85E7AA0420DF645B4FD788AA37A72B01F1E56090FBE344FF657A8A6645CD33DA07B8EE2BCFDE2F192E7A069DC243DB61BC0DCFE835F3C302F80F23363DDE0CAAA81A5253CD1B2A73E6E07FD89159523D44627B5B8E7027058A51380CFBE955E4B8EE9F9ECDB8F00D1CA43603A1BE0ABF61; _ga=GA1.2.1666451281.1592410949; _gid=GA1.2.90168544.1592415384; __utma=73562946.1666451281.1592410949.1592418645.1592452198.9; __utmt=1; __utmb=73562946.81.9.1592453318670',
            'Content-Type': 'application/json',
            'Accept-Encoding':  'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Accept': '*/*'
            }

            
            conn.request("POST", "/service/Atividade/Novo", payload, headers)
            res = conn.getresponse()
            data = res.read()
            print(data.decode("utf-8"))
            