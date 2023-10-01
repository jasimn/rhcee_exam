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

Q10.Using the correct command or combination of commands, find all of the current open regular files in use by the sshd process, and save the list of complete file paths to /home/bob/sshdfiles.txt with one entry per line. This list should only include regular files, not directories, sockets, or any other type.

answer:

Run the following command to find all of the current open regular files in use by the sshd process and store the output to /home/bob/sshdfiles.txt.


sudo lsof | grep sshd |  grep -i reg | s

Q11.Use yum to install the necessary tools for managing lvm. Using the correct tools, perform the following tasks:


1: Create physical volumes on /dev/vdb and /dev/vdc.
2: Create a volume group named vg0 using the physical volumes on /dev/vdb and /dev/vdc.


3: Create a logical volume named developer_storage using all available space on vg0.




Install Package lvm


sudo yum install -y lvm2



Create physical volumes on /dev/vdb and /dev/vdc with below command:


sudo pvcreate /dev/vdb /dev/vdc



Create a volume group named vg0 using the physical volumes on /dev/vdb and /dev/vdc with below command:


sudo vgcreate vg0 /dev/vdb /dev/vdc



Create a logical volume named developer_storage using all available space on vg0 with below command:


sudo lvcreate -n developer_storage -

Q12.Using the correct tools, perform the following tasks:


1: Create an ext4 filesystem on the logical volume named developer_storage.


2: Create a mount point at /mnt/developer_storage/.


3: Edit /etc/fstab and add an entry to mount the logical volume named developer_storage at boot time.


4: Mount the logical volume named developer_storage to the mount point /mnt/developer_storage.


answer:


Create an ext4 filesystem on the logical volume named developer_storage with below command:


sudo mkfs.ext4 /dev/vg0/developer_storage


Create a mount point at /mnt/developer_storage/ with below command:


sudo mkdir /mnt/developer_storage/


Edit /etc/fstab and add an entry to mount the logical volume named developer_storage at boot time as below:


/dev/vg0/developer_storage /mnt/developer_storage ext4 defaults 0 0


Mount the logical volume named developer_storage to the mount point /mnt/developer_storage with below command:


sudo mount -a


Q13.Create a partition on /dev/vdd that uses all available space.


Run the command 

sudo fdisk /dev/vdd

and create a new partition by selecting n and using all available space.

The new partition should be /dev/vdd1.

Use the w option to write the changes.

Q14.Create an ext4 filesystem on the partition you have created on /dev/vdd. Take all necessary steps to enable user and group quotas on this file system, including installing the necessary software package(s).
Create a mount point at /mnt/shared/. Add an entry to /etc/fstab to mount this filesystem at boot time to this mount point, remembering to include the options for user and group quotas. Lastly, mount the file system you have created to the mount point at /mnt/shared/.



Install the quota package using yum with below command:


sudo yum -y install quota


Create an ext4 filesystem on the partition on /dev/vdd1.


sudo mkfs.ext4 /dev/vdd1


Using an editor such as vi, edit /etc/fstab and add an entry like this: 


/dev/vdd1 /mnt/shared ext4 defaults,usrquota,grpquota 0 0.


Create the mount directory /mnt/shared and mount with below commands:


sudo mkdir /mnt/shared/
sudo mount -a



Include the options for user and group quotas with below command:


sudo quotacheck --create-files --user --group /dev/vdd1
sudo quotaon /mnt/shared/


Q15.Using yum, install the necessary packages to create and manage Stratis layered storage. Make sure that the Stratis service is started and is enabled at boot time.
Next, create a Stratis layered storage solution on /dev/vde with the following parameters:


1: A pool named web_team.


2: A filesystem named web_fs.


Create a mount point at /mnt/web_storage/.


Edit /etc/fstab to add an entry that mounts your Stratis storage solution to /mnt/web_storage at boot time. Remember to include the options necessary for mounting a Stratis device at boot.


Lastly, mount your Stratis storage solution to /mnt/web_storage/.

answer:



Install the packages using yum command and start/enable the service as below:


sudo yum -y install stratisd stratis-cli
sudo systemctl enable --now stratisd.service


Create a pool named web_team with below command:


sudo stratis pool create web_team /dev/vde


Create a filesystem named web_fs with below command:


sudo stratis fs create web_team web_storage


Create a mount point at /mnt/web_storage with below command:


sudo mkdir /mnt/web_storage


Using an editor such as vi, edit /etc/fstab and add the following line:


/dev/stratis/web_team/web_storage /mnt/web_storage xfs x-systemd.requires=stratisd.service 0 0


Mount your Stratis storage solution to /mnt/web_storage/ with below command:


sudo mount -a


Q16.Using the correct commands, add the storage device at /dev/vdf to the web_team Stratis pool.




sudo stratis pool add-data web_team /dev/vdf


Q17.Use yum, reset the current module stream for php and then install version 7.4 of php.


answer:


Get a list of available PHP module streams:


sudo yum module list php



Enable php:7.4 module stream:


sudo yum module enable php:7.4 -y



Install php v7.4:


sudo yum install php -y


Q18.Create a repository file at /etc/yum.repos.d/kodekloud.repo and configure the repository with the following information:


answer:


1: short name: KodeKloud.


2: long name: KodeKloud YUM repository.


3: Base URL: https://download.docker.com/linux/centos/$releasever/$basearch/stable


4: gpgkey: https://download.docker.com/linux/centos/gpg


5: Enable the repository




Using an editor such as vi, edit the file /etc/yum.repos.d/kodekloud.repo and populate it with the following information:


[KodeKloud]
name=KodeKloud YUM repository
baseurl=https://download.docker.com/linux/centos/$releasever/$basearch/stable
gpgkey=https://download.docker.com/linux/centos/gpg
enabled=1


Q19.Edit the correct file to statically map repo.kodekloud.com to the IP address 1.2.3.4.

answer:


Using an editor such as vi, edit the file /etc/hosts and add an entry as below:


1.2.3.4 repo.kodekloud.com



Q20.Add a DNS resolver entry for the IP address 1.1.1.1

answer:


Using an editor such as vi, edit the file /etc/resolv.conf and add an entry:


nameserver 1.1.1.1


Q21.Using yum, install the chrony service, start it, and enable it at boot time.


answer:


Install chrony package using yum with below command:


sudo yum -y install chrony


Start and enable chrony service as below:


sudo systemctl start chronyd.service
sudo systemctl enable chronyd.servi


Q22.Using the contents of /etc/passwd, find which user accounts have a shell of /sbin/nologin, and save only the user name of each account, one per line, in the file /home/bob/nologin.txt



cat /etc/passwd | grep 'nologin' | cut -d : -f 1 > /home/bob/nologin.txt


Q23.Using the correct command, change the default shell of the user simon to a non-interactive shell by setting the default shell to /sbin/nologin.

answer:


Change the default shell of the user simon to a non-interactive shell by setting the default shell to /sbin/nologin as below:


sudo usermod --shell /sbin/nologin simo


Q24.Use the passwd utility to set the password for the user simon to expired.


answer:

Use the passwd utility to set the password for the user simon to expired using below command:


sudo passwd -e simon


Q25.Generate a ssh key pair for the user bob. Copy bob’s public key to /home/bob/public.txt


Generate a ssh key for bob using below command:


ssh-keygen



Copy the bob's ssh key to /home/bob/public.txt as below:


cp ~/.ssh/id_rsa.pub /home/bob/public.txt


Q26.Determine the SELinux file context for the file located at /home/bob/.ssh/known_hosts and write it in the file /home/bob/known_hosts.txt


Determine the SELinux file context for the file located at /home/bob/.ssh/known_hosts with below command and note the same :


ls -Z /home/bob/.ssh/known_hosts


Using an editor such as vi, edit the file /home/bob/known_hosts.txt and add an entry for the SELinux file context you observed for /home/bob/.ssh/known_hosts example as below:


unconfined_u:object_r:ssh_home_t:s0


Q27.Using sestatus, determine the policy name for the currently loaded policy, and save it in /home/bob/policy.txt


answer:

Run the below command to determine the policy name for the currently loaded policy as below:


sestatus



You will get the similar output as below:


SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      32



Add an entry for the policy name you observed to /home/bob/policy.txt:


Loaded policy name:             targeted

complete ! thank!












