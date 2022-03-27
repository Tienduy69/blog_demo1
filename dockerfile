FROM python:3

WORKDIR E:\blog_demo

COPY . .

RUN pip install -r setup.text

CMD ["python","./app.py"]