FROM python:3.8

# Install few packages
RUN apt-get update && \
    apt-get install -y libsndfile1 ffmpeg


WORKDIR /workspace
ADD requirements.txt /workspace/requirements.txt

RUN pip install -r requirements.txt

ADD app.py /workspace/
ADD examples /workspace/examples/

# Create a HOME dedicated to the OVHcloud user (42420:42420)
RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace
CMD [ "python3" , "/workspace/app.py" ]