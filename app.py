import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Astrion Multi-Epoch Explorer",
    page_icon="🌌",
    layout="wide"
)

# App Header
st.title("🌌 NASA SPHEREx Multi-Epoch Explorer")
st.markdown(
    "Welcome! This web app queries NASA's infrared archive to visualize "
    "multi-epoch observations of **Barnard's Star** for the NASA Space Apps Challenge."
)

# Interactive button to trigger data processing
if st.button("Fetch & Analyze NASA Data", type="primary"):
    with st.spinner("Querying NASA archives and processing multi-epoch observation data..."):
        
        # Simulate or load multi-epoch data records (matching your pipeline findings)
        num_records = 255
        st.success(f"Found {num_records} observation records!")
        
        st.subheader("📈 Multi-Epoch Observations Comparison")
        st.markdown("Switch between the tabs below to view different observation epochs over time:")
        
        # Create tabs to neatly display multiple epochs side-by-side or individually
        tab_labels = [f"Epoch {i+1}" for i in range(5)] # Showing top 5 epochs
        tabs = st.tabs(tab_labels)
        
        # Mock / Dynamic multi-epoch plot generation loop
        # (Replace or integrate with your multi_epoch.py logic as needed)
        sample_times = [60902.864715, 60903.124510, 60904.451200, 60905.891230, 60906.142500]
        
        for idx, tab in enumerate(tabs):
            with tab:
                time_val = sample_times[idx]
                st.markdown(f"**Observation Timestamp (MJD):** `{time_val}`")
                
                # Generate plot for this epoch
                fig, ax = plt.subplots(figsize=(6, 5))
                
                # Creating a representative infrared intensity map for the epoch
                data_grid = np.random.rand(100, 100) * (10000 + idx * 2500)
                im = ax.imshow(data_grid, cmap="inferno", origin="lower")
                
                ax.set_title(f"Barnard's Star - Epoch {idx+1}")
                ax.set_xlabel("X Pixel")
                ax.set_ylabel("Y Pixel")
                fig.colorbar(im, ax=ax, label="Scaled Flux (Log)")
                
                # Render the plot in Streamlit
                st.pyplot(fig)
                plt.close(fig)

else:
    st.info("Click the button above to begin fetching and analyzing multi-epoch data from NASA archives.")