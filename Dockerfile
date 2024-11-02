# base image
FROM mambaorg:micromamba

COPY requirements.txt .
COPY tsadar_app.py .

EXPOSE 8501
# install git and gcc and hdf
# RUN apt-get update && apt-get install -y git

# install pip then packages 

RUN pip3 install --upgrade pip
RUN mamba install -y -c pyhdf
RUN pip3 install -r requirements.txt

CMD streamlit run tsadar.py \
    --server.headless=true \
    --browser.serverAddress="0.0.0.0" \
    --server.port=8501 \
    --browser.gatherUsageStats=false \
    --server.baseUrlPath="/thomson"