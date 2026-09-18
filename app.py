import time
import streamlit as st

# Page setup with custom icon
st.set_page_config(
    page_title="For Shristi ⚡", page_icon="⚡", layout="centered"
)

# Custom Styling (Gradients, Card Borders, Custom Fonts & Animations)
st.markdown(
    """
    <style>
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #1e1e2f 0%, #0f0c20 100%);
        color: #ffffff;
    }
    
    /* Header card */
    .header-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        margin-bottom: 2rem;
    }
    
    /* Custom button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #ff4b4b 0%, #ff7676 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.75rem 1rem;
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.6);
    }
    
    /* Styled dividers */
    hr {
        border-color: rgba(255, 255, 255, 0.1);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Decorated Header Box
st.markdown(
    """
    <div class="header-card">
        <h1 style="color: #ffe600; font-size: 2.5rem; margin-bottom: 0.5rem;">⚡ A Special Message for Shristi ⚡</h1>
        <p style="color: #b0b0d0; font-size: 1.1rem; font-style: italic;">Tere pyaare 'Bijli ke Khamba' ki taraf se... 🥺</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Opening Section
st.markdown("### ✨ Hey Shristi...")
st.info("I know I messed up earlier, Shristi, and I'm genuinely sorry. T-T")

st.write("")

# Detailed explanation section
with st.expander("🔍 What actually happened"):
    st.write(
        """
    1. You gave me the nickname **“Bijli Ka Khamba”** ⚡
    2. You asked me how I liked it.
    3. I genuinely couldn't see the nickname properly on Instagram, so I got confused.
    4. Then my half-asleep brain somehow came up with the worst possible sentence: *“I guess wrong person ko message chala gya.”*
    
    And yeah... I completely understand why that sounded bad. 😭 
    I didn't mean that I didn't know who you were or that I didn't care about your message. I just messed up.
    """
    )

# Cute/Funny nickname section
with st.expander("⚡ Official 'Bijli Ka Khamba' Status Report"):
    st.write(
        """
    * **At first:** *“Hein? Konsa nickname?”* 💀
    * **After realizing what you meant:** *“OH.”*
    * **And now:** **Bijli Ka Khamba has been officially accepted.** ⚡🗿
    
    Honestly, it's actually funny 😭 You can keep calling me that.
    """
    )

st.divider()

# Softer closing section
st.markdown("### ❤️ One last thing…")
st.markdown(
    """
> I know I messed up, and I'm genuinely sorry, Shristi. I didn't mean “wrong person” the way it sounded.
> 
> It was just my sleepy brain being stupid at the worst possible moment. 😭 You're my good friend, and I really didn't want to hurt you or make you feel ignored. I'm sorry. T-T
"""
)

st.write("")

# Interactive Forgiveness Action
if st.button("Okay, apology received. 👍"):
    st.balloons()
    st.success(
        """
    **Thank you for reading this, Shristi. ❤️**
    
    Now please stop being angry at this idiot. 😭
    
    *— Bijli Ka Khamba ⚡*
    """,
        icon="✨",
    )

st.divider()
st.caption("⚡ Coded with pure Python, extra regret, and lots of respect.")