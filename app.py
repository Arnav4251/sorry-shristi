import time
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="I'm So Sorry, Shristi!", page_icon="⚡", layout="centered"
)

# Title & Subtitle
st.title("⚡ A Special Message for Shristi ⚡")
st.subheader("From your officially sleepy & silly friend...")

st.divider()

# Interactive Section
st.write("### Hey Shristi...")
st.write(
    "I know I completely messed up earlier, and I feel really terrible about it. T-T"
)

# Expandable apology steps
with st.expander("👉 Click here to see what actually happened"):
    st.write(
        """
    1. **I had just woken up** and my brain was operating at 1% capacity. 😴
    2. I couldn't see the nickname on Instagram properly, so I got confused.
    3. Saying *"wrong person ko message chala gya"* was the dumbest thing I could have said, and I am so, so sorry!
    """
    )

with st.expander("👉 Click here to see how I feel about the nickname"):
    st.write(
        """
    Honestly? **'Bijli ka Khamba'** ⚡ is an iconic nickname! 
    It was super creative, and I actually really like it. I'm sorry for making it seem like I didn't appreciate it.
    """
    )

st.divider()

# Interactive Forgiveness Quiz
st.write("### Final Verdict")
forgive = st.radio(
    "Will you forgive your local 'Bijli ka Khamba'?",
    [
        "Select an option...",
        "Yes, fine, I forgive you! 🤝",
        "Maybe... if you promise not to text right after waking up ⏰",
        "No, still angry! 😤",
    ],
)

if forgive == "Yes, fine, I forgive you! 🤝":
    st.balloons()
    st.success(
        "Yay! Thank you so much, Shristi! Best friend ever! ⚡❤️", icon="🎉"
    )
elif (
    forgive == "Maybe... if you promise not to text right after waking up ⏰"
):
    st.info(
        "Deal! I promise to wash my face and drink water before typing next time! 🚰🙏"
    )
elif forgive == "No, still angry! 😤":
    st.error("Oh no... initiating emergency apology protocol!")
    with st.spinner("Calculating total level of regret..."):
        time.sleep(2)
    st.warning("Regret status: 10000%. Please reconsider? 🥺")

st.divider()
st.caption("Coded with pure Python, extra regret, and lots of respect.")