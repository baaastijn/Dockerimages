# Base image
FROM gitpod/workspace-full:latest

USER root

# Install MySQL shell, PostgreSQL shell, Redis Shell, MongoDB shell
# MySQL : https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install-linux-quick.html
# PostgreSQL : https://www.postgresql.org/download/linux/ubuntu/
RUN install-packages mysql-shell postgresql-client-14 redis mongosh
