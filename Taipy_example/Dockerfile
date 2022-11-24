# Start from official Python image
FROM python:3.9

# Create a working directory
WORKDIR /workspace

# Install few requirements, such as pandas, taipy, scikit-learn, ...
ADD requirements.txt /workspace/requirements.txt

RUN pip install -r requirements.txt

# Add your scripts to Docker image. Note : best practice is to put data outside, such as S3 storage
ADD app.py /workspace/
ADD dataset.csv /workspace/

# Create a HOME dedicated to the OVHcloud user (42420:42420). mandatory step
RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace

# Run you script and BOOM :)
CMD [ "python3" , "/workspace/app.py" ]