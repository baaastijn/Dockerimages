# Base image. Here we take one from OVHcloud with Jupyter inside and pytorch
FROM ovhcom/ai-training-pytorch:latest

# Install git, audio loader ang git lfs
RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y libsndfile1-dev sox && \
    apt-get install -y git-lfs && \
    git lfs install 

# Install required python libraries. We install transformers from source to get latest version
RUN pip install --upgrade pip && \
    pip install git+https://github.com/huggingface/transformers && \
    pip install git+https://github.com/huggingface/datasets && \
    pip install torchaudio librosa jiwer && \
    pip install pandas numpy nano gradio 

# Create a HOME dedicated to the OVHcloud user (42420:42420)
RUN chown -R 42420:42420 /workspace
ENV HOME /workspace
WORKDIR /workspace
 
# Copy a folder of example notebooks into another folder in remote workspace
# COPY notebooks /workspace/
