# base image
FROM python:3.12-slim

COPY requirements.txt .
COPY stapp.py .

EXPOSE 8501

# install pip then packages
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD streamlit run tsadar.py \
    --server.headless=true \
    --browser.serverAddress="0.0.0.0" \
    --server.port=8501 \
    --browser.gatherUsageStats=false \
    --server.baseUrlPath="/thomson"