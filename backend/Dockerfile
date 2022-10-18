FROM python:3.10
RUN apt-get update
RUN mkdir /app
WORKDIR /app

ARG USER_ID=0
ARG GROUP_ID=${USER_ID:-0}
ARG USER_NAME=internal-user
RUN if [ ${USER_ID:-0} -ne 0 ] || [ ${GROUP_ID:-0} -ne 0 ]; then \
    if [ ${GROUP_ID:-0} -ne 0 ] && ! getent group ${GROUP_ID}; then groupadd -g ${GROUP_ID} ${USER_NAME}; fi ;\
    if [ ${USER_ID:-0} -ne 0 ] && ! getent passwd ${USER_ID}; then useradd -u ${USER_ID} -g ${GROUP_ID} -m -s /bin/bash ${USER_NAME}; fi ;\
#    chown -R ${USER_ID:-0}:${GROUP_ID:-0} ./ ;\
#    chmod -R 755 ./ ;\
    fi
USER ${USER_ID:-0}
ENV PATH "$PATH:/home/${USER_NAME}/.local/bin"

ADD --chown=${USER_ID:-0}:${GROUP_ID:-0} . /app

RUN pip install -r requirements.txt
