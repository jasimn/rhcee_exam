Q1. One of the files in the directory /opt/assets/ contains text, and the others are empty. Locate the file that contains text, and write its full file path in the file /home/bob/magicfile.txt.

answer:

grep -r [A-Z,a-z] /opt/assets/ > /home/bob/magicfile.txt

           or

Find /opt/assets/ -type f -exec grep -l . {} \; > /home/bob/magicfile.txt

 
Q2.Create a soft link to the file you found in the previous question. The soft link should be located at /home/bob/magiclink.

answer:

ln -s /opt/assets/asset150 /home/bob/magiclink

 Q3. Write a shell script named exit_test.sh and save it in the directory /home/bob/. The script should echo Exiting with code 150. and set the exit code to 150.
Make your script executable.

answer:
  
opne editor like vim or nano and add these lines


#!/bin/bash

echo "Exiting with code 150."

exit 150

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

sudo mkdir /raidsudo 

mkfs.xfs /dev/md0

sudo mount /dev/md0 /raid

Q8.Create an entry in /etc/fstab to automatically mount your RAID device /dev/md0 to the mount point /raid/ at boot time. In addition to the default options, include mount options to enable filesystem quota support for both users and groups on the XFS file system. Use 0 0 for the file system check and dump options.

answer:

open the vim editor and add this lines

/dev/md0   /raid/   xfs   defaults,usrquota,grpquota   0 0

after the saving the this lines save the changes 

run this the commmand 

sudo mount -a

Q9.Using the correct utility, create a single partition on /dev/vde that uses the entire available disk space. Set the partition type to the correct type for a vfat filesystem.


answer:

type this command

sudo fdisk /dev/vde

select  n for new

select p for primary, and use the entire disk space available.

Choose t for type for the partition.

Choose L. it is used to list all codes and choose b for W95 FAT32.

Choose w to write the changes and exit.

Q10.Format the partition /dev/vde1 with a 32-bit vfat filesystem. Create a mount point at /vfat/.
Add an entry in /etc/fstab to automatically mount the filesystem on /dev/vde at boot time.
Also mount the filesystem to the /vfat/ mount point you created.

answer:

sudo mkfs.vfat -F 32 /dev/vde1

Create a mount point at /vfat/ as below:


sudo mkdir /vfat/



Using an editor such as vi, edit /etc/fstab and add an entry as follow:


/dev/vde1 /vfat vfat defaults 0 0



Mount the filesystem to the /vfat/ as below:


sudo mount -a


Q11.Using yum, install the necessary packages for creating and managing Stratis layered storage.

answer:


sudo yum -y install stratisd stratis-cli


Q12.Imagine a hypothetical Stratis pool named web_storage, with a Stratis filesystem named web_storage1.
What line would you need to add to /etc/fstab to have this Stratis filesystem mounted to a hypothetical mount point /mnt/web_storage at boot time?

Write your answer in the file /home/bob/stratisboot.txt


answer:

/dev/stratis/web_storage/web_storage1 /mnt/web_storage xfs x-systemd.requires=stratisd.service 0 0

Q13.Using yum, install the necessary packages for creating and managing VDO devices on RHEL 8.

answer:


sudo yum -y install vdo


Q14.Imagine a hypothetical VDO device named compressed on a hypothetical device /dev/vdf with an XFS filesystem.
What line would you add to /etc/fstab to have this VDO device mounted to the mount point /mnt/compressed at boot time?

Write your answer in the file /home/bob/vdoboot.txt.


answer:

/dev/mapper/compressed /mnt/compressed xfs _netdev,x-systemd.device-timeout=0,x-systemd.requires=vdo.service 0 0

Q15.Using yum uninstall nginx and all of its dependencies.

anser






  






