FROM debian:bullseye-slim

LABEL version="0.1" maintainer="GARRIGUES Clement <tecnelm91@gmail.com>"
ENV TOKEN=""
ENV PORT=6789
ENV ADDRESS="127.0.0.1"
ENV MAC=""
ENV TIME_MIN_AFK=600

RUN apt-get update -y &&\
	apt-get upgrade -y &&\
	apt-get install -y python3 &&\
	apt-get install -y python3-pip&&\
	apt-get install -y git

RUN git clone https://github.com/Tecnelm/Availiability_GamingBot
COPY ./main.sh /main.sh
WORKDIR /Availiability_GamingBot
RUN pip3 install -r ./Requirement.txt


ENTRYPOINT ./main.sh
