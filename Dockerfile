# base image
FROM mambaorg/micromamba:latest

COPY --chown=$MAMBA_USER:$MAMBA_USER requirements.txt mambaenv.yaml tsadar_app.py tsadar_gui .

RUN micromamba install -y -n base -f mambaenv.yaml && \
    micromamba clean --all --yes

EXPOSE 8501

CMD micromamba run -n base streamlit run tsadar_app.py \
    --server.headless=true \
    --browser.serverAddress="0.0.0.0" \
    --server.port=8501 \
    --browser.gatherUsageStats=false \
    --server.baseUrlPath="/thomson"