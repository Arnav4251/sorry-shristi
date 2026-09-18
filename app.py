import time
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="I'm So Sorry, Shristi!", page_icon="⚡", layout="centered"
)

# Title & Subtitle
st.title("⚡ A Special Message for Shristi ⚡")
st.subheader("from a sleepy and silly friend... 🥺")

st.divider()

# Updated natural opening
st.write("### Hey Shristi...")
st.write("I know I messed up earlier, and I'm genuinely sorry. T-T")

# Detailed explanation section
with st.expander("👉 What actually happened"):
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
with st.expander("👉 ⚡ Official Bijli Ka Khamba Report"):
    st.write(
        """
    * **At first:** *“Hein? Konsa nickname?”* 💀
    * **After realizing what you meant:** *“OH.”*
    * **And now:** **Bijli Ka Khamba has been officially accepted.** ⚡🗿
    
    Honestly, it's actually funny 😭 You can keep calling me that.
    """
    )

st.divider()

# Softer closing section (replacing "Final Verdict")
st.write("### One last thing… ❤️")
st.write(
    """
I know I messed up, and I'm genuinely sorry, Shristi.
I didn't mean “wrong person” the way it sounded.

It was just my sleepy brain being stupid at the worst possible moment. 😭
You're my good friend, and I really didn't want to hurt you or make you feel ignored.
I'm sorry. T-T
"""
)

# No-pressure single button
if st.button("Okay, apology received. 👍"):
    st.balloons()
    st.success(
        """
    **Thank you for reading this, Shristi. ❤️**
    
    Now please stop being angry at this idiot. 😭
    
    *— Bijli Ka Khamba ⚡*
    """
    )

st.divider()
st.caption("Coded with pure Python, extra regret, and lots of respect.")