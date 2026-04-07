import streamlit as st
from PIL import Image

# Reset session state
def reset():
    st.session_state.lo = 0
    st.session_state.hi = 99
    st.session_state.found = False
    st.session_state.userError = False

# Load image from local file
logo = Image.open("media/Megaman_battle_network1_logo.webp")  # replace with your file name
st.image(logo, use_container_width=True)  # display image at top

# Centered title using HTML in Markdown
st.markdown(
    "<h1 style='text-align: center;'>Passcode Finder</h1>",
    unsafe_allow_html=True
)

import streamlit as st

# Meta tags for social preview image
st.markdown(
    """
    <head>
    <meta property="og:image" content="./media/Megaman_battle_network_legacy.avif">
    <meta name="twitter:image" content="./media/Megaman_battle_network_legacy.avif">
    </head>
    """,
    unsafe_allow_html=True
)

# App description
st.markdown(
    """
    This app helps you find the correct passcodes in **Mega Man Battle Network**.  
    **How it works:**  
    1. Enter the displayed number below into the game.  
    2. Click the button that matches the text in the game.

    The app will automatically narrow down the range and guide you to the correct passcode.

    *NOTE:*
    There is a small chance that the passcode will reset along the way. Just keep following through and this app will lead you to the correct passcode!
    """
)

# Initialize session state
if "lo" not in st.session_state:
    reset()

# Current guess
mid = st.session_state.lo + (st.session_state.hi - st.session_state.lo) // 2
passcode = f"{mid:02d}"

# Show guess and range
if not st.session_state.userError:
    st.subheader(f"Try passcode: {passcode}")
    st.caption(f"Range: {st.session_state.lo}–{st.session_state.hi}")

# Handle impossible state
if st.session_state.userError:
    st.error("There was an error in the user input.")
    if st.button("Restart", key="restart"):
        reset()
        st.rerun()

# Main guessing logic
elif not st.session_state.found:

    # User feedback buttons
    high = st.button("Passcode too high.", key="too_high")
    low = st.button("Passcode too low.", key="too_low")
    highVerif = st.button("Passcode too high. Second Digit, verification failure", key="too_highVerif")
    lowVerif = st.button("Passcode too low. Second Digit, verification failure", key="too_lowVerif")
    accepted = st.button("Passcode accepted.", key="accepted")
    restart = st.button("Too many tries. Resetting passcode", key="reset")

    # Update search range based on feedback
    if high:
        st.session_state.hi = mid - (mid % 10 + 1)
        st.rerun()

    elif low:
        st.session_state.lo = mid + (10 - mid % 10)
        st.rerun()

    elif highVerif:
        st.session_state.hi = mid - 1
        st.session_state.lo = max(st.session_state.lo, mid - mid % 10)
        st.rerun()

    elif lowVerif:
        st.session_state.lo = mid + 1
        st.session_state.hi = min(st.session_state.hi, mid + (9 - mid % 10))
        st.rerun()

    elif accepted:
        st.session_state.found = True
        st.rerun()

    elif restart:
        reset()
        st.rerun()

    # Detect impossible range
    if st.session_state.lo > st.session_state.hi:
        st.session_state.userError = True
        st.rerun()

# Success
else:
    st.success("We found it!")
    if st.button("Restart", key="restart"):
        reset()
        st.rerun()