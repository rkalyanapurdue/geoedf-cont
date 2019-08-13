BootStrap: docker
From: ubuntu:18.04

%post
    apt-get update
    apt-get -y install python3 curl wget
    wget -O - http://download.pegasus.isi.edu/pegasus/gpg.txt | apt-key add -
    echo 'deb [arch=amd64] http://download.pegasus.isi.edu/pegasus/ubuntu bionic main' | tee /etc/apt/sources.list.d/pegasus.list
    apt-get update
    apt-get -y install htcondor pegasus
    mkdir /app
    mkdir /data
    mv /tmp/*.py /app
    chmod +x /app/*.py

%environment
    export PATH=/app:$PATH

%files
    ./tools/run_connector.py /tmp
    ./tools/run_processor.py /tmp

%runscript
    exec "$@"

%labels
    Author Rajesh Kalyanam
