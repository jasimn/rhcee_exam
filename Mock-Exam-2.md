# Mock-2 RHCSA
Q5.Write a script named home.sh and save it in the /home/bob/ directory. The script should create a tar archive named homedir.tar containing the full contents of /home/bob/ and all subdirectories. Use absolute paths. The script should create homedir.tar in the /opt/ directory. Make your script executable and run it.

ans.
tar cf  /opt/homedir.tar /home/bob
