FROM python:3.10

RUN pip install -U pip

RUN adduser --disabled-password py
USER py
WORKDIR /home/py
ENV PATH="/home/py/.local/bin:${PATH}"

COPY --chown=py:py requirements.txt requirements.txt
RUN pip install --user --no-warn-script-location -r requirements.txt

COPY --chown=py:py src .
ENTRYPOINT ["python", "/home/py/main.py"]
