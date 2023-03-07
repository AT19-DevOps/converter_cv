#
# @dockerfile Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

FROM python:3.8-alpine3.16
WORKDIR /app

COPY . .

RUN apk update \
    && apk add --no-cache \
    --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev \
    libressl-dev libffi-dev \
    && apk add exiftool ffmpeg imagemagick tesseract-ocr \
    && pip install -r requirements.txt --no-cache \
    && apk del .tmp-build-deps \
    && rm -rf /var/cache/apk/*

EXPOSE 5000

CMD ["python3", "CONVERTER/src/com/jalasoft/converter/main.py", "ffmpeg", "libmagickwand", "tesseract"]
