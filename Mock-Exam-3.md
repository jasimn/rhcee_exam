Q1.Locate the appropriate documentation directory for bzip2 and copy that directory and its contents to /home/bob/.

answer:

Find the documentation directory for bzip2 with below command:


sudo find / -name bzip2 -type d

Copy the directory with its content /usr/share/doc/bzip2 to /home/bob/ as below:


cp -r /usr/share/doc/bzip2/ /home/bob/

Q2.Using the proper commands, search the LICENSE file located in the bzip2 subdirectory of /home/bob/ which you created in the previous task, and copy only the lines beginning with numbers to the file /home/bob/numbers.txt.

answer:

Find the file LICENSE under /home/bob/ as below:


find /home/bob -name LICENSE -type f

Copy the line beginning with numbers to the file /home/bob/numbers.txt with below command:


grep '^[0-9]' /home/bob/bzip2/LICENSE

Q3.Set the sticky bit on the /home/bob/bzip2 directory. Leave all other permissions in place.

answer:

Run the below command to add sticky bit to directory /home/bob/bzip2:


chmod +t /home/bob/bzip2

Q4.Write a script named documenter.sh and save it in the /home/bob/ directory. For every subdirectory in /usr/share/doc/, the script should echo $dir has documentation. where $dir is the name of a subdirectory in /usr/share/doc/. The script should direct this output to the file /home/bob/documentation.txt and each entry should be on a separate line. Make your script executable and run it.

answer:

Using some editor like vi, create a script /home/bob/documenter.sh as below:


#!/bin/bash

for dir in $(ls /usr/share/doc/)

do

    echo $dir has documentation. >> /home/bob/documentation.txt

done

Make the script executable and run with below command:


chmod u+x documenter.sh
./documenter.sh

Q5.Write a script named home.sh and save it in the /home/bob/ directory. The script should create a tar archive named homedir.tar containing the full contents of /home/bob/ and all subdirectories. Use absolute paths. The script should create homedir.tar in the /opt/ directory. Make your script executable and run it.

answer:

Using an editor such as vi create a script named home.sh at /home/bob/ containing the following:


#!/bin/bash

tar cf /opt/homedir.tar /home/bob


Make the script executable and run it with below commands:


chmod u+x home.sh
sudo ./home.sh

Q6.Write a script named conditional.sh and save it in the /home/bob/ directory. The script should check if the file /opt/nojoy exists. If it exists, the script should copy the file to /home/bob/nojoy. Otherwise, the script should echo File not found. and direct that output to the file /home/bob/nojoy overwriting any contents that are in the file. Make your script executable and run it.

answer:

Using an editor such as vi create a script named conditional.sh at /home/bob/ containing the following:


#!/bin/bash

if [ -f "/opt/nojoy" ]
then
    cp /opt/nojoy /home/bob/
else
    echo File not found. > /home/bob/nojoy
fi


Make the script executable and run it with below commands:


chmod u+x /home/bob/conditional.sh
./conditional.sh

Q7.Using yum, install TuneD, then start the TuneD service and enable it to run at boot time.

answer:

Install package TuneD by using yum with below command:


sudo yum install tuned -y


Start TuneD service and enable its service as below:


sudo systemctl start tuned

sudo systemctl enable --now tuned.service

Q8.Configure TuneD for dynamic tuning, and make sure this setting is picked up and used by TuneD.

answer:

Using an editor such as vi, edit /etc/tuned/tuned-main.conf and change dynamic_tuning = 0 to dymanic_tuning = 1 and save the file as below.


sudo vi /etc/tuned/tuned-main.conf


Restart the TuneD service with below command:


sudo systemctl restart tuned

Q9.What would you add to the GRUB command line if you needed to interrupt the boot process and gain access to the emergency shell?
For example, you might do this if you had lost the root password for the machine, and need to gain access to change it. Write the answer in the file /home/bob/interrupt.txt.

Note: This is for RHEL 8.

answer:

Using an editor such as vi, edit the file /home/bob/interrupt.txt and add the following:


rd.break

Q10.



