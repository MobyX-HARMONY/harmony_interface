FROM python:3.7

WORKDIR /usr/client
ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./

CMD ["sleep", "infinity"]
#CMD ["python3", "send_message.py"]