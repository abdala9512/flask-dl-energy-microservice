FROM ubuntu:latest
MAINTAINER Miguel Arquez


RUN apt-get update \
	&& apt-get install -y python3-pip python3-dev \
	&& cd /usr/local/bin \
	&& ln -s /usr/bin/python3 python \
    && pip3 install flask \
    && pip3 install tensorflow \
    && pip3 install numpy 

RUN mkdir ./output

COPY app.py app.py
COPY DeepLearningUTSModel.py DeepLearningUTSModel.py
COPY output/LSTM_energy_gen.h5 output/LSTM_energy_gen.h5 
COPY output/LSTM_energy_cap.h5 output/LSTM_energy_cap.h5 

EXPOSE 6600
ENTRYPOINT ["python3", "app.py"]

# compile and run (on port 6600)
# docker build -t lstm-api . 
# docker run -d -p 6600:6600 --name lstm-api lstm-api




