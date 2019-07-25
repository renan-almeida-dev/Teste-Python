FROM python:3
ADD fatec.py /
RUN pip install beautifulsoup4
RUN pip install tabulate
RUN pip install requests
CMD [ "python", "./fatec.py" ]
