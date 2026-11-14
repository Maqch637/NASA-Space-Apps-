import streamlit as st
from astropy.coordinates import SkyCoord
import astropy.units as u
from astroquery.ipac.irsa import Irsa
from astropy.utils.data import download_file
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.visualization import ImageNormalize, LogStretch
import time

# App Title and Description
st.title("🌌 Astrion Multi-Epoch Explorer")
st.write("Welcome! This web app queries NASA's infrared archive to visualize multi-epoch observations of **Barnard's Star**.")

# Add a button to trigger the process
if st.button("Fetch & Analyze NASA Data"):
    with st.spinner("Querying NASA IRSA servers..."):
        coord = SkyCoord.from_name("Barnard's Star")
        
        # Query database with fallback and retry logic
        results = None
        for collection_name in ["spherex_dr1", "spherex_qr3"]:
            try:
                results = Irsa.query_sia(pos=(coord, 0.05 * u.deg), collection=collection_name)
                if results is not None and len(results) > 0:
                    break
            except Exception:
                time.sleep(1)
                
    if results is not None and len(results) > 0:
        st.success(f"Found {len(results)} observation records!")
        
        # Display the first epoch
        row = results[0]
        image_url = row["access_url"]
        obs_time = row.get("t_min", "Epoch 1")
        
        with st.spinner("Downloading FITS image from NASA..."):
            cached_file = download_file(image_url, cache=True, timeout=60)
            
            with fits.open(cached_file) as hdul:
                data = hdul[0].data
                if data is None or data.ndim < 2:
                    data = hdul[1].data
                    
                # Plotting with Matplotlib
                norm = ImageNormalize(data, stretch=LogStretch())
                fig, ax = plt.subplots(figsize=(6, 6))
                im = ax.imshow(data, cmap='inferno', origin='lower', norm=norm)
                fig.colorbar(im, ax=ax, label='Scaled Flux (Log)')
                ax.set_title(f"Barnard's Star (Time: {obs_time})")
                ax.set_xlabel("X Pixel")
                ax.set_ylabel("Y Pixel")
                
                # Render the plot directly inside your web app!
                st.pyplot(fig)
    else:
        st.error("NASA servers are busy right now. Please try clicking the button again!")