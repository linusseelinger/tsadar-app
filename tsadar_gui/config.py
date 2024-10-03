import streamlit as st


def get_config():
    config = create_default_config()
    # inputs = get_inputs()
    return config


def optimizer_section():
    optimizer = {
        "method": st.selectbox("Optimization method", ["l-bfgs-b", "adam", "sgd"], index=0),
        "hessian": st.checkbox("Use hessian", value=False),
        "y_norm": st.checkbox("Normalize y", value=True),
        "x_norm": st.checkbox("Normalize x", value=False),
        "grad_method": st.selectbox("Gradient method", ["AD", "FD", "Other"], index=0),
        "batch_size": st.number_input("Batch size", value=6, min_value=1, step=1),
        "num_epochs": st.number_input("Number of epochs", value=500, min_value=1, step=1),
        "learning_rate": st.number_input("Learning rate", value=1.0e-4, format="%.5e"),
        "parameter_norm": st.checkbox("Parameter normalization", value=True),
        "refine_factor": st.number_input("Refine factor", value=0, min_value=0, step=1),
        "num_mins": st.number_input("Number of minima", value=8, min_value=1, step=1),
        "sequential": st.checkbox("Sequential optimization", value=False),
    }

    return optimizer


def get_species1():

    # Define variables using Streamlit widgets
    species1_type = st.selectbox("species1 type", ["electron"])
    species1_type_active = st.checkbox("species1 type active", value=False)

    Te_val = st.number_input("Te val", value=0.2)
    Te_active = st.checkbox("Te active", value=True)
    Te_lb = st.number_input("Te lb", value=0.01)
    Te_ub = st.number_input("Te ub", value=1.5)

    ne_val = st.number_input("ne val", value=0.08)
    ne_active = st.checkbox("ne active", value=True)
    ne_lb = st.number_input("ne lb", value=0.03)
    ne_ub = st.number_input("ne ub", value=1.0)

    m_val = st.number_input("m val", value=2.0)
    m_active = st.checkbox("m active", value=False)
    m_lb = st.number_input("m lb", value=2.0)
    m_ub = st.number_input("m ub", value=5.0)
    m_matte = st.checkbox("m matte", value=False)
    m_intens = st.number_input("m intens", value=2.0)

    fe_val = st.text_area("fe val", value="[]")
    fe_active = st.checkbox("fe active", value=False)
    fe_length = st.number_input("fe length", value=3999)
    fe_type = st.selectbox("fe type", ["DLM"])
    fe_lb = st.number_input("fe lb", value=-100.0)
    fe_ub = st.number_input("fe ub", value=-0.5)
    fe_decrease_strict = st.checkbox("fe decrease strict", value=False)
    fe_symmetric = st.checkbox("fe symmetric", value=False)
    fe_dim = st.number_input("fe dim", value=1)
    fe_v_res = st.number_input("fe v_res", value=0.05)
    fe_temp_asym = st.number_input("fe temp_asym", value=1.0)
    fe_m_theta = st.number_input("fe m_theta", value=0.0)
    fe_m_asym = st.number_input("fe m_asym", value=1.0)

    # Use the variables to populate the dictionary
    species1 = {
        "type": {
            "electron": species1_type,
            "active": species1_type_active,
        },
        "Te": {
            "val": Te_val,
            "active": Te_active,
            "lb": Te_lb,
            "ub": Te_ub,
        },
        "ne": {
            "val": ne_val,
            "active": ne_active,
            "lb": ne_lb,
            "ub": ne_ub,
        },
        "m": {
            "val": m_val,
            "active": m_active,
            "lb": m_lb,
            "ub": m_ub,
            "matte": m_matte,
            "intens": m_intens,
        },
        "fe": {
            "val": fe_val,
            "active": fe_active,
            "length": fe_length,
            "type": {"DLM": fe_type},
            "lb": fe_lb,
            "ub": fe_ub,
            "fe_decrease_strict": fe_decrease_strict,
            "symmetric": fe_symmetric,
            "dim": fe_dim,
            "v_res": fe_v_res,
            "temp_asym": fe_temp_asym,
            "m_theta": fe_m_theta,
            "m_asym": fe_m_asym,
        },
    }

    return species1


def get_species2():
    return {
        "type": {
            "ion": st.selectbox("species2 type", ["ion"]),
            "active": st.checkbox("species2 type active", value=False),
        },
        "Ti": {
            "val": st.number_input("Ti val", value=0.08),
            "active": st.checkbox("Ti active", value=False),
            "same": st.checkbox("Ti same", value=False),
            "lb": st.number_input("Ti lb", value=0.01),
            "ub": st.number_input("Ti ub", value=1.0),
        },
        "Z": {
            "val": st.number_input("Z val", value=10.0),
            "active": st.checkbox("Z active", value=False),
            "lb": st.number_input("Z lb", value=1.0),
            "ub": st.number_input("Z ub", value=18.0),
        },
        "A": {"val": st.number_input("A val", value=40.0), "active": st.checkbox("A active", value=False)},
        "fract": {
            "val": st.number_input("fract val", value=1.0),
            "active": st.checkbox("fract active", value=False),
        },
    }


def get_general():
    return {
        "type": {
            "general": st.selectbox("general type", ["general"]),
            "active": st.checkbox("general type active", value=False),
        },
        "amp1": {
            "val": st.number_input("amp1 val", value=1.0),
            "active": st.checkbox("amp1 active", value=True),
            "lb": st.number_input("amp1 lb", value=0.01),
            "ub": st.number_input("amp1 ub", value=3.75),
        },
        "amp2": {
            "val": st.number_input("amp2 val", value=1.0),
            "active": st.checkbox("amp2 active", value=True),
            "lb": st.number_input("amp2 lb", value=0.01),
            "ub": st.number_input("amp2 ub", value=3.75),
        },
        "amp3": {
            "val": st.number_input("amp3 val", value=1.0),
            "active": st.checkbox("amp3 active", value=False),
            "lb": st.number_input("amp3 lb", value=0.01),
            "ub": st.number_input("amp3 ub", value=3.75),
        },
        "lam": {
            "val": st.number_input("lam val", value=526.5),
            "active": st.checkbox("lam active", value=False),
            "lb": st.number_input("lam lb", value=523.0),
            "ub": st.number_input("lam ub", value=528.0),
        },
        "Te_gradient": {
            "val": st.number_input("Te_gradient val", value=0.0),
            "active": st.checkbox("Te_gradient active", value=False),
            "lb": st.number_input("Te_gradient lb", value=0.0),
            "ub": st.number_input("Te_gradient ub", value=10.0),
            "num_grad_points": st.number_input("Te_gradient num_grad_points", value=1),
        },
        "ne_gradient": {
            "val": st.number_input("ne_gradient val", value=0.0),
            "active": st.checkbox("ne_gradient active", value=False),
            "lb": st.number_input("ne_gradient lb", value=0.0),
            "ub": st.number_input("ne_gradient ub", value=15.0),
            "num_grad_points": st.number_input("ne_gradient num_grad_points", value=1),
        },
        "ud": {
            "val": st.number_input("ud val", value=0.0),
            "angle": st.number_input("ud angle", value=0.0),
            "active": st.checkbox("ud active", value=False),
            "lb": st.number_input("ud lb", value=-10.0),
            "ub": st.number_input("ud ub", value=10.0),
        },
        "Va": {
            "val": st.number_input("Va val", value=0.0),
            "angle": st.number_input("Va angle", value=0.0),
            "active": st.checkbox("Va active", value=False),
            "lb": st.number_input("Va lb", value=-20.5),
            "ub": st.number_input("Va ub", value=20.5),
        },
    }


# Function to create an interactive dictionary structure for the merged YAML
def create_default_config():

    with st.expander("Species 1"):
        species1 = get_species1()

    with st.expander("Species 2"):
        species2 = get_species2()

    with st.expander("General"):
        general = get_general()

    parameters = {
        "species1": species1,
        "species2": species2,
        "general": general,
    }

    with st.expander("Data"):
        data = {
            "shotnum": st.number_input("shotnum", value=101675),
            # shot day booolean
            "shotDay": st.checkbox("shotDay", value=False),
            "lineouts": {
                "type": {"ps": st.selectbox("lineouts type", ["ps"])},
                "start": st.number_input("lineouts start", value=800),
                "end": st.number_input("lineouts end", value=3500),
                "skip": st.number_input("lineouts skip", value=10),
            },
            "background": {
                "type": {"pixel": st.selectbox("background type", ["pixel"])},
                "slice": st.number_input("background slice", value=900),
            },
            "probe_beam": st.selectbox("probe beam", ["P9"]),
        }

    with st.expander("Other"):
        other = {
            "extraoptions": {
                "load_ion_spec": st.checkbox("load_ion_spec", value=False),
                "load_ele_spec": st.checkbox("load_ele_spec", value=True),
                "fit_IAW": st.checkbox("fit_IAW", value=False),
                "fit_EPWb": st.checkbox("fit_EPWb", value=True),
                "fit_EPWr": st.checkbox("fit_EPWr", value=True),
                "spectype": st.selectbox("spectype", ["temporal"]),
            },
            "PhysParams": {
                "widIRF": {
                    "spect_stddev_ion": st.number_input("spect_stddev_ion", value=0.015),
                    "spect_stddev_ele": st.number_input("spect_stddev_ele", value=0.1),
                    "spect_FWHM_ele": st.number_input("spect_FWHM_ele", value=0.9),
                    "ang_FWHM_ele": st.number_input("ang_FWHM_ele", value=1.0),
                }
            },
            "refit": st.checkbox("refit", value=False),
            "refit_thresh": st.number_input("refit_thresh", value=5.0),
            "calc_sigmas": st.checkbox("calc_sigmas", value=False),
        }

    with st.expander("Mlflow"):

        mlflow = {
            "experiment": st.text_input("experiment", value="inverse-thomson-scattering"),
            "run": st.text_input("run", value="test"),
        }

    with st.expander("Optimizer"):
        optimizer = optimizer_section()
    return {"parameters": parameters, "data": data, "other": other, "mlflow": mlflow, "optimizer": optimizer}
