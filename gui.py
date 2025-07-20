



# import streamlit as st
# from cli_parser import parse_cli
# from visualizer import plot_toolpath_with_heat

# st.title("3D Printing Tool Path Visualizer with Heat Source Overlay")

# uploaded_file = st.file_uploader("Upload a .cli file", type="cli")

# if uploaded_file is not None:
#     cli_path = "uploaded.cli"
#     with open(cli_path, "wb") as f:
#         f.write(uploaded_file.read())

#     st.write("Parsing CLI file...")
#     layers = parse_cli(cli_path)

#     st.write(f"Parsed {len(layers)} layers.")
#     if layers:
#         fig = plot_toolpath_with_heat(layers)
#         st.pyplot(fig)
#     else:
#         st.error("No valid toolpath data found in the CLI file.")
# else:
#     st.info("Please upload a .cli file to begin.")




import streamlit as st
from cli_parser import parse_cli
from visualizer import plot_3d_toolpath_with_heat

st.set_page_config(layout="wide")
st.title("3D Tool Path Visualizer with Gaussian Heat Overlay")

uploaded_file = st.file_uploader("Upload a .cli file", type="cli")

if uploaded_file:
    cli_path = "uploaded.cli"
    with open(cli_path, "wb") as f:
        f.write(uploaded_file.read())

    layers = parse_cli(cli_path)
    sorted_layers = sorted(layers.keys())

    # ⬇️ First show the controls BEFORE rendering
    st.sidebar.header("Controls")
    layer_option = st.sidebar.selectbox("Select Layer (or view all)", ["All"] + sorted_layers)
    show_heat = st.sidebar.checkbox("Show Gaussian Heat Overlay", value=True)

    max_heat = st.sidebar.slider("Max Heat Points", min_value=10, max_value=200, value=50, step=10)


    # ⬇️ Now rendering logic using those controls
    with st.spinner("Rendering... Please wait."):
        if layer_option == "All":
            fig = plot_3d_toolpath_with_heat(layers, selected_layer=None, show_heat=show_heat,max_heat_points=max_heat)
        else:
            fig = plot_3d_toolpath_with_heat(layers, selected_layer=layer_option, show_heat=show_heat,max_heat_points=max_heat)

        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Upload a .cli file to start.")

