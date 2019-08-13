BootStrap: library
From: ubuntu:18.04

%post
    apt-get -y update
    apt-get -y install python3 curl wget
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
