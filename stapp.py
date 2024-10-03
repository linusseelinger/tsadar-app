from jax import config

config.update("jax_enable_x64", True)

import streamlit as st
import yaml, os
from flatten_dict import flatten, unflatten

from tsadar_gui import config
from tsadar import run_for_app


def process_file(file_path):
    # Dummy function to process the file
    return f"Processing file: {file_path}"


if __name__ == "__main__":
    st.title("Thomson Scattering Analysis")
    st.sidebar.title("Thomson Scattering Analysis")

    # select box between forward and fit
    mode = st.sidebar.selectbox("How are you providing the configuration options?", ["file", "gui"])

    config_dir = os.path.join(os.getcwd(), "temp")

    os.makedirs(config_dir, exist_ok=True)
    if mode == "file":
        defaults = st.file_uploader("Upload the defaults file", type=["yaml", "yml"])
        if defaults:
            with open(os.path.join(config_dir, defaults.name), "wb") as f:
                f.write(defaults.getvalue())

        inputs = st.file_uploader("Upload the inputs file", type=["yaml", "yml"])
        if inputs:
            with open(os.path.join(config_dir, inputs.name), "wb") as f:
                f.write(inputs.getvalue())

        with open(os.path.join(config_dir, "defaults.yaml"), "r") as f:
            defs = yaml.safe_load(f)

        with open(os.path.join(config_dir, "inputs.yaml"), "r") as f:
            inps = yaml.safe_load(f)

        defaults = flatten(defs)
        defaults.update(flatten(inps))
        cfg = unflatten(defaults)

        # epw_file = st.file_uploader("Upload the EPW data file", type=["hdf", "txt"])
        # if epw_file:
        #     epw_file_path = epw_file.name
        #     with open(epw_file.name, "wb") as f:
        #         f.write(epw_file.getvalue())

        # iaw_file = st.file_uploader("Upload the IAW data file", type=["hdf", "txt"])
        # if iaw_file:
        #     iaw_file = iaw_file.name
        #     with open(iaw_file.name, "wb") as f:
        #         f.write(iaw_file.getvalue())

    elif mode == "gui":
        cfg = config.get_config()

    if st.button("Process"):
        # run and wait for the results
        run_id = run_for_app(cfg, mode="fit")

        st.write(f"The results can be found at the mlflow run id {run_id}")

    st.sidebar.title("About")
    ## Add attribution
    st.sidebar.markdown(
        "This app is a Streamlit implementation of the Thomson Scattering Analysis software published in ref [1]"
    )
    # add ref 1
    st.sidebar.markdown(
        "1. Milder, A. L., Joglekar, A. S., Rozmus, W. & Froula, D. H. Qualitative and quantitative enhancement of parameter estimation for model-based diagnostics using automatic differentiation with an application to inertial fusion. Mach. Learn.: Sci. Technol. 5, 015026 (2024)."
    )
