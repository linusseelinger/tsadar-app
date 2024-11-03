# base image
FROM mambaorg/micromamba:latest

COPY --chown=$MAMBA_USER:$MAMBA_USER requirements.txt .
COPY --chown=$MAMBA_USER:$MAMBA_USER mambaenv.yaml .
COPY --chown=$MAMBA_USER:$MAMBA_USER tsadar_app.py .
RUN micromamba install -y -n base -f mambaenv.yaml && \
    micromamba clean --all --yes

EXPOSE 8501
# install git and gcc and hdf
# RUN apt-get update && apt-get install -y git

# install pip then packages 

# RUN mamba create -n tsadar_app python=3.12
# RUN mamba activate tsadar_app
# RUN mamba install -y -c pyhdf
# RUN pip3 install -r requirements.txt

CMD micromamba run -n base streamlit run tsadar_app.py \
    --server.headless=true \
    --browser.serverAddress="0.0.0.0" \
    --server.port=8501 \
    --browser.gatherUsageStats=false \
    --server.baseUrlPath="/thomson"