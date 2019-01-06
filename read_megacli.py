# Monitoramento de RAID e envio de email para servidores
# Modelo da placa: Supermicro SMC2108

# Importação das bibliotecas:
# re (para utilizar expressão regulares na consulta de palavras)
# smtplib para envio de e-mails

import re
import smtplib


# Criação de uma função para comparação de uma comparacao_string
# Retorna TRUE caso existe alguma string que foi passada com parâmetro
def comparacao_string(comparacao,string):
	re.compile(comparacao)
	if (re.search(comparacao,string)):
		return True
	else:
		return False

# Função que envia e-mail
def envia_email(assunto,texto_email):
	smtp = smtplib.SMTP_SSL('mail.xtpo.com.br',465) #servidor smtp
	smtp.login('user@xtpo.com.br','password') #usuário e senha do e-mail
	smtp.ehlo_or_helo_if_needed()
	from_email = 'From: user@xpto.com.br\n' #remetente do email
	to_email = 'To: rotinas@xpto.com.br\n' #destinatario do email
	subject_email = 'Subject: '+assunto+'\n' #assunto
	body_email = texto_email+'\n' #corpo do email
	msg = from_email+to_email+subject_email+body_email
	msg = msg.encode('ascii','ignore').decode('utf-8')
	smtp.sendmail('user@xpto.com.br',['rotinas@xpto.com.br'],msg)
	smtp.quit()


# Lê novamente o arquivo MegaSAS.log e armazena cada linha em um array para que possa ser analisado
file_date = open('MegaSAS.log','r')
text_array = []
for line in file_date:
	text_array.append(line)

# Armazena uma variável data para poder verificar se o comando executado pelo arquivo bat está funcionando diáriamente.
# Esta variável é utilizada no assunto do e-mail
date_line = text_array[0]

file_date.close()

#Verifica se dentro do arquivo existe a palavra Optimal, se sim, o RAID está funcionando corretamente, caso contrário está com erro.
file = open('MegaSAS.log','r')
message = file.read()
state = comparacao_string('Optimal',message)
if state:
	state_message = 'MegaRaid OK'
else:
	state_message = 'MegaRaid Error'

envia_email(state_message+' - '+date_line,message)

file.close()
