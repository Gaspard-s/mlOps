FROM ubuntu:22.04

# Install Python
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev
RUN pip install --upgrade pip
RUN pip install fastapi fastapi[standard] joblib numpy scikit-learn

# Copy the FastAPI app code
COPY app.py /app.py 
COPY regression.joblib /regression.joblib

CMD ["fastapi","dev","app.py","--host","0.0.0.0"]