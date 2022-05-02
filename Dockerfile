FROM debian:bullseye-slim

LABEL version="0.1" maintainer="GARRIGUES Clement <tecnelm91@gmail.com>"
ENV TOKEN=""
ENV PORT=6789
ENV ADDRESS=''
ENV MAC=""
ENV TIME_MIN_AFK=60

RUN apt-get update -y &&\
	apt-get upgrade -y &&\
	apt-get install -y python3 &&\
	apt-get install -y python3-pip&&\
	apt-get install -y git

RUN git clone https://github.com/Tecnelm/Availiability_GamingBot
WORKDIR /Availiability_GamingBot
RUN pip3 install -r ./Requirement.txt && chmod +x ./main.sh

ENTRYPOINT ./main.sh
