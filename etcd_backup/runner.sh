rm /home/ubuntu/etcd_backup

ETCD_API=3 etcdctl \
    --endpoints=https://[130.185.120.84]:2379 \
    --cacert=/home/ubuntu/etcd_certificates/ca.crt \
    --cert=/home/ubuntu/etcd_certificates/server.crt \
    --key=/home/ubuntu/etcd_certificates/server.key \
    snapshot save /home/ubuntu/etcd_backup

python3 /home/ubuntu/s3.py