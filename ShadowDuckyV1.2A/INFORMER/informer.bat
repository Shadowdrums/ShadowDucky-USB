@ECHO OFF
cd %TEMP%
powershell.exe echo 'Hello'
powershell -command sleep 1
powershell -command echo 'Computer And User Name:' > D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command whoami >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command echo 'IP-Address:' >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command ipconfig >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command echo 'ARP:' >>D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command arp -a >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command echo 'OS Name' >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command (get-wmiobject win32_operatingsystem).name >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command echo 'CS OS Nmae:' >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command (get-wmiobject win32_operatingsystem).csname >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command echo 'OS Architecture' >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command (get-wmiobject win32_operatingsystem).osarchitecture >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command echo 'Thank You For Using ShadowDucky Informer' >> D:\Intel-Report\Intel-Report.txt
powershell -command sleep 1
powershell -command exit