Q1. One of the files in the directory /opt/assets/ contains text, and the others are empty. Locate the file that contains text, and write its full file path in the file /home/bob/magicfile.txt.

answer:
grep -r [A-Z,a-z] /opt/assets/ > /home/bob/magicfile.txt

           or

Q2. Find /opt/assets/ -type f -exec grep -l . {} \; > /home/bob/magicfile.txt
 
Create a soft link to the file you found in the previous question. The soft link should be located at /home/bob/magiclink.

answer:

ln -s /opt/assets/asset150 /home/bob/magiclink
