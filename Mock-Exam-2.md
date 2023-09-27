Q1. One of the files in the directory /opt/assets/ contains text, and the others are empty. Locate the file that contains text, and write its full file path in the file /home/bob/magicfile.txt.

answer:

grep -r [A-Z,a-z] /opt/assets/ > /home/bob/magicfile.txt

           or

Q2. Find /opt/assets/ -type f -exec grep -l . {} \; > /home/bob/magicfile.txt
 
Create a soft link to the file you found in the previous question. The soft link should be located at /home/bob/magiclink.

answer:

ln -s /opt/assets/asset150 /home/bob/magiclink

 Q3. Write a shell script named exit_test.sh and save it in the directory /home/bob/. The script should echo Exiting with code 150. and set the exit code to 150.
Make your script executable.

answer:
  
opne editor like vim or nano and add these lines


#!/bin/bash
echo "Exiting with code 150."
exit 150
you open editor like nano or vim 
add these lines

save these changes and run this script 

Q4.Write a shell script named file_check.sh and save it in the directory /home/bob/. The script should check if the file /opt/assets/asset75 exists.
If the file exists, the script should echo File exists. Making a copy. It should then create the directory /home/bob/backups/ and copy the file /opt/assets/asset75 to the directory /home/bob/backups/. If the file is not found, the script should echo File not found.. Also make your script executable and run it.

answer:

opne editor like vim or nano and add these lines



#!/bin/bash
if [ -f "/opt/assets/asset75" ]
then
        echo "File exists. Making a copy."
        mkdir /home/bob/backups/
        cp /opt/assets/asset75 /home/bob/backups/
else
        echo "File not found."
fi
 
save these changes and run this script


Q5.Write a shell script named read_log.sh and save it in the directory /home/bob/.
The script should list the contents of /opt/assets3/ and for every entry, it should echo Read file $file. where $file is the name of a file from the list of files in /opt/assets3/. Each time this echo statement runs, it should append the output to a file located at /home/bob/read_log.txt.

answer:

open editor like vim or nano and add these lines below



#!/bin/bash
for file in $(ls /opt/assets3/)
do
        echo "Read file $file." >> /home/bob/read_log.txt
done
 

 save these changes and run the script

Q6.Change the default boot target for this system to graphical.target.

answer:
 
sudo systemctl set-default graphical.target

Q7.Create a level 0 RAID at /dev/md0 using the devices at /dev/vdb , /dev/vdc and /dev/vdd. Create an XFS filesystem on the resulting RAID device.
Further create a mount point at /raid and mount the filesystem you have just created.

answer:


to create a raid device use these command ;

sudo  mdadm --create /dev/md0 --level=0 --raid-devices=3 /dev/vdb /dev/vdc /dev/vdd


  






