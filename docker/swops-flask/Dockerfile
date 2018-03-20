FROM tiangolo/uwsgi-nginx-flask:python3.6
# ENV STATIC_INDEX 1
# ^ Assumed tests will be expecting /static/ path, not from root, and as such left this disabled.

COPY ./app /app
EXPOSE 80
