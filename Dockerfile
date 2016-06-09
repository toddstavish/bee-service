# Run the Building Extraction Evaluation (BEE) Service in a container
#
# docker run -i -t \
#        -v $HOME/Data:/home/data  \  <- mounts data directory to container
#        toddstavish/bee
#
FROM ubuntu:14.04
MAINTAINER Todd Stavish <toddstavish@gmail.com>

# Install binary dependencies
RUN apt-get -qqy update && \
    apt-get install -qqy software-properties-common --no-install-recommends && \
    apt-add-repository -y ppa:ubuntugis/ppa && \
    apt-get install -qqy \
        build-essential \
        gdal-bin \
        libgdal-dev \
        libspatialindex-dev \
        python \
        python-dev \
        python-pip \
        git-all \
        --no-install-recommends

# Pull project
WORKDIR /home
RUN git clone https://github.com/toddstavish/bee-service.git

# Install python dependencies
WORKDIR bee-service
RUN pip install -r requirements.txt

# Clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Open port 8000
EXPOSE 8000

# Run gunicorn
ENTRYPOINT ["/usr/local/bin/gunicorn"]
CMD ["-b", ":8000", "django_rest.wsgi"]
#CMD ["/bin/bash"]
