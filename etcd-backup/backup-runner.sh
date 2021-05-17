rm /home/ubuntu/backup-file.tar.gz 2> /dev/null
microk8s dbctl backup -o backup-file

python3 backup.py
