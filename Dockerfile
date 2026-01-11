FROM python:3.12.12-alpine

ENV WORK_DIR="/app/src"
ENV PYTHONPATH=${WORK_DIR}
ENV PYTHONDONTWRITEBYTECODE=1
ENV USER=cloner
ENV GROUP=cloner

WORKDIR ${WORK_DIR}

# Create user
RUN addgroup --system ${GROUP} &&\
    adduser --system --home ${WORK_DIR}/../user --ingroup ${GROUP} ${USER} --shell /bin/sh

# Install requirements
RUN pip install --no-cache-dir poetry &&\
    poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml .
RUN poetry install --no-interaction --no-ansi --no-root

# Copy the sorurce
COPY cli.py docker-entrypoint.sh .

# Apply user
RUN chown -R ${USER}:${GROUP} ${WORK_DIR}
USER ${USER}

ENTRYPOINT ["/app/src/docker-entrypoint.sh"]
