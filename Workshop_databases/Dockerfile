# Choose your base image
FROM python:3.8

# Install PostgreSQL client
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends postgresql postgresql-contrib

# Create a HOME dedicated to the ovhcloud user (42420:42420)
RUN mkdir /workspace && chown -R 42420:42420 /workspace
ENV HOME /workspace
WORKDIR /workspace

RUN python3 -m pip install --no-cache-dir jupyterlab psycopg2 nano

EXPOSE 8080
CMD ["bash", "-c", "jupyter lab --ip=0.0.0.0 --port=8080 --no-browser --allow-root \
  --ServerApp.token='' \
  --ServerApp.custom_display_url=${JOB_URL_SCHEME}${JOB_ID}.${JOB_HOST} \
  --ServerApp.allow_remote_access=True \
  --ServerApp.allow_origin='*' \
  --ServerApp.disable_check_xsrf=True"]

# Copy a folder of example notebooks into another folder in remote workspace
COPY notebooks /workspace/