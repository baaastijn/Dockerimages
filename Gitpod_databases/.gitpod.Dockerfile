# Base image Ubuntu 20.04
FROM gitpod/workspace-full:latest

USER root

# Install MySQL shell, PostgreSQL shell
RUN install-packages mysql-server postgresql postgresql-contrib
