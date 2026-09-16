FROM python:3.9.0-slim-buster
RUN apt update && apt install -y libsm6 libxext6 libgl1-mesa-glx
RUN apt-get -y install tesseract-ocr
RUN apt-get -y install libtesseract-dev
COPY . /app
WORKDIR /app
RUN apt-get -y install libmagickwand-dev
RUN pip3 install --upgrade setuptools pip
RUN pip3 install scikit-build
RUN pip3 install cmake
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]
