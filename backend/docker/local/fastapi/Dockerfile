ARG PYTHON_VERSION=3.13.1

FROM python:${PYTHON_VERSION}-slim-bookworm AS python
# Stage 1: build dependency wheels
FROM python AS python-build-stage

RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	gcc \
	libpq-dev \
	&& rm -rf /var/lib/apt/lists/*

COPY ./backend/requirements.txt .
RUN pip install --upgrade pip \
	&& pip wheel --wheel-dir /usr/src/app/wheels \
	-r requirements.txt \
	--no-cache-dir

# Stage 2: final image
FROM python AS python-final-stage

ARG APP_HOME=/src
ARG APP_GROUP=fastapi
ARG APP_USER=fastapi

ENV PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTECODE=1 \
	PIP_NO_CACHE_DIR=1 \
	PIP_ROOT_USER_ACTION=ignore \
	POETRY_VIRTUALENVS_CREATE=false \
	POETRY_CACHE_DIR='/var/cache/pypoetry' \
	APP_HOME=${APP_HOME}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install -y --no-install-recommends \
	sudo git bash-completion nano curl ssh \
	gettext \
	&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
	build-essential \
	libpq-dev \
	&& rm -rf /var/lib/apt/lists/* \
	&& groupadd -r ${APP_GROUP} \
	&& useradd -r -g ${APP_GROUP} -d ${APP_HOME} -m ${APP_USER} 

RUN mkdir  -p {APP_HOME}/backend/app/logs \
	&& chown -R ${APP_USER}:${APP_GROUP} {APP_HOME}/backend/app/logs \
	&& chmod 775 {APP_HOME}/backend/app/logs 
	
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --upgrade pip \
	&& pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
	&& rm -rf /wheels/


COPY --chown=${APP_USER}:${APP_GROUP} ./backend/app/docker/local/fastapi/entrypoint.sh /entrypoint.sh
COPY --chown=${APP_USER}:${APP_GROUP} ./backend/app/docker/local/fastapi/start.sh /start.sh
COPY --chown=${APP_USER}:${APP_GROUP} ./backend/app/docker/local/fastapi/celery/worker/start.sh /celery-worker-start.sh
COPY --chown=${APP_USER}:${APP_GROUP} ./backend/app/docker/local/fastapi/celery/beat/start.sh /celery-beat-start.sh
COPY --chown=${APP_USER}:${APP_GROUP} ./backend/app/docker/local/fastapi/celery/flower/start.sh /celery-flower-start.sh





RUN sed -i 's/\r$//g' /entrypoint.sh /start.sh /celery-worker-start.sh /celery-beat-start.sh /celery-flower-start.sh \
	&& chmod +x /entrypoint.sh /start.sh /celery-worker-start.sh /celery-beat-start.sh /celery-flower-start.sh
COPY --chown=${APP_USER}:${APP_GROUP} . ${APP_HOME}

USER ${APP_USER}

ENTRYPOINT ["/entrypoint.sh"]