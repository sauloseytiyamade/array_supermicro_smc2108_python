@echo off
REM Acessa a linha de comando do Megacli para gerar um log do status do Array
cd C:\SWTOOLS\DEVICEDRIVERS\MegeCli\te8msm01sr17\for windows\
REM Envia para o arquivo MegaSAS.log a data
date /T > MegaSAS.log
REM Envia para o arquivo MegaSAS.log o status do array
MegaCli64.exe -CfgDsply -aALL >> MegaSAS.log
REM Executa um ping
ping -n 10 192.168.X.X
REM Executa o script python para verificar o status do array
python read_megacli.py
