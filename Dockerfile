# base image
FROM mambaorg/micromamba:latest

COPY requirements.txt .
COPY tsadar_app.py .

EXPOSE 8501
# install git and gcc and hdf
# RUN apt-get update && apt-get install -y git

# install pip then packages 

RUN mamba create -n tsadar_app python=3.12
RUN mamba activate tsadar_app
RUN mamba install -y -c pyhdf
RUN pip3 install -r requirements.txt

CMD streamlit run tsadar.py \
    --server.headless=true \
    --browser.serverAddress="0.0.0.0" \
    --server.port=8501 \
    --browser.gatherUsageStats=false \
    --server.baseUrlPath="/thomson"