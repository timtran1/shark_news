FROM odoo:15

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends awscli python3-wheel

RUN pip3 install bs4 PyJWT praw boto3 mixpanel

USER odoo
