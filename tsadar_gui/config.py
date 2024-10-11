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
                "type": st.selectbox("lineouts type", ["pixel"]),
                "start": st.number_input("lineouts start", value=500),
                "end": st.number_input("lineouts end", value=510),
                "skip": st.number_input("lineouts skip", value=1),
            },
            "background": {
                "type": st.selectbox("background type", ["pixel"]),
                "slice": st.number_input("background slice", value=900),
            },
            "probe_beam": st.selectbox("probe beam", ["P9"]),
            "ele_t0": st.number_input("ele_t0", value=1500.0),
            "ion_t0_shift": st.number_input("ion_t0_shift", value=900.0),
            "dpixel": st.number_input("dpixel", value=3),
            "bgscaleE": st.number_input("bgscaleE", value=1.0),
            "bgscaleI": st.number_input("bgscaleI", value=0.1),
            "launch_data_visualizer": st.checkbox("launch_data_visualizer", value=True),
            "ele_lam_shift": st.number_input("ele_lam_shift", value=0.0),
            "ion_loss_scale": st.number_input("ion_loss_scale", value=2.0),
        }
        fit_rng = {
            "blue_min": st.number_input("Blue Min", min_value=400, max_value=510, value=430),
            "blue_max": st.number_input("Blue Max", min_value=400, max_value=510, value=510),
            "red_min": st.number_input("Red Min", min_value=500, max_value=660, value=545),
            "red_max": st.number_input("Red Max", min_value=500, max_value=660, value=660),
            "iaw_min": st.number_input("IAW Min", min_value=500.0, max_value=530.0, value=525.5),
            "iaw_max": st.number_input("IAW Max", min_value=500.0, max_value=530.0, value=527.5),
            "iaw_cf_min": st.number_input("IAW CF Min", min_value=526.0, max_value=527.0, value=526.49),
            "iaw_cf_max": st.number_input("IAW CF Max", min_value=526.0, max_value=527.0, value=526.51),
            "forward_epw_start": st.number_input("Forward EPW Start", min_value=300, max_value=800, value=400),
            "forward_epw_end": st.number_input("Forward EPW End", min_value=300, max_value=800, value=700),
            "forward_iaw_start": st.number_input("Forward IAW Start", min_value=500.0, max_value=530.0, value=525.75),
            "forward_iaw_end": st.number_input("Forward IAW End", min_value=500.0, max_value=530.0, value=527.25),
        }
        data["fit_rng"] = fit_rng
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
            "CCDsize": st.number_input("CCD Size (uses same value for both dimensions)", value=1024),
            "flatbg": st.checkbox("flatbg", value=False),
            "gain": st.number_input("gain", value=1.0),
            "points_per_pixel": st.number_input("points_per_pixel", value=1),
            "iawoff": st.number_input("iawoff", value=0.0),
        }
        # Input as a comma-separated string
        iawfilter_input = st.text_input("IAW Filter (comma-separated)", value="1, 4, 24, 528")

        # Convert the input string into a list of integers
        iawfilter = [int(i) for i in iawfilter_input.split(",")]
        other["iawfilter"] = iawfilter

        background_input = st.text_input("Background (comma-separated)", value="0, 0")
        background = [int(i) for i in background_input.split(",")]

        # Input for 'norm' as an integer value
        norm = st.number_input("Norm", min_value=0, value=0)

        # Creating the PhysParams dictionary
        other["PhysParams"] = {"background": background, "norm": norm}

        other["CCDsize"] = [other["CCDsize"], other["CCDsize"]]

    with st.expander("Plotting"):
        # Input for n_sigmas (integer)
        n_sigmas = st.number_input("n_sigmas", min_value=0, value=3)

        # Input for rolling_std_width (integer)
        rolling_std_width = st.number_input("rolling_std_width", min_value=1, value=5)

        # Input for data_cbar_u (string)
        data_cbar_u = st.text_input("data_cbar_u", value="data")

        # Input for data_cbar_l (integer)
        data_cbar_l = st.number_input("data_cbar_l", min_value=0, value=0)

        # Input for ion_window_start (integer)
        ion_window_start = st.number_input("ion_window_start", min_value=500, max_value=530, value=525)

        # Input for ion_window_end (integer)
        ion_window_end = st.number_input("ion_window_end", min_value=500, max_value=530, value=528)

        # Input for ele_window_start (integer)
        ele_window_start = st.number_input("ele_window_start", min_value=400, max_value=700, value=425)

        # Input for ele_window_end (integer)
        ele_window_end = st.number_input("ele_window_end", min_value=400, max_value=700, value=660)

        # Creating the plotting dictionary
        plotting = {
            "n_sigmas": n_sigmas,
            "rolling_std_width": rolling_std_width,
            "data_cbar_u": data_cbar_u,
            "data_cbar_l": data_cbar_l,
            "ion_window_start": ion_window_start,
            "ion_window_end": ion_window_end,
            "ele_window_start": ele_window_start,
            "ele_window_end": ele_window_end,
        }

    with st.expander("Mlflow"):

        mlflow = {
            "experiment": st.text_input("experiment", value="inverse-thomson-scattering"),
            "run": st.text_input("run", value="test"),
        }

    with st.expander("Optimizer"):
        optimizer = optimizer_section()
    return {
        "parameters": parameters,
        "data": data,
        "other": other,
        "mlflow": mlflow,
        "optimizer": optimizer,
        "plotting": plotting,
    }
