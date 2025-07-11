FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y wget unzip curl gnupg && \
    apt-get install -y chromium chromium-driver && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/usr/lib/chromium/:$PATH"
ENV CHROME_BIN="/usr/bin/chromium"
ENV CHROMEDRIVER="/usr/bin/chromedriver"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "tests/test_demoQA.py"]