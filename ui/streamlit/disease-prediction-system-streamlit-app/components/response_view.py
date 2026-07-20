import streamlit as st
import pandas as pd


def render_prediction(result: dict):

    prediction = result.get("prediction", "Unknown")
    confidence = float(result.get("confidence", 0))

    # -----------------------------
    # Header
    # -----------------------------
    st.markdown("# 🩺 Disease Prediction Result")

    st.markdown("---")

    # -----------------------------
    # Prediction Card
    # -----------------------------

    col1, col2 = st.columns([3, 1])

    with col1:

        if confidence >= 0.80:
            st.success(f"## ✅ {prediction}")

        elif confidence >= 0.50:
            st.warning(f"## ⚠️ {prediction}")

        else:
            st.error(f"## 🔴 {prediction}")

        st.caption("Predicted Disease")

    with col2:

        st.metric(
            label="Confidence",
            value=f"{confidence:.2%}"
        )

    st.markdown("---")

    # -----------------------------
    # Confidence Meter
    # -----------------------------

    st.markdown("### 🎯 Prediction Confidence")

    st.progress(confidence)

    st.write(f"Model Confidence : **{confidence:.2%}**")

    st.markdown("---")

    
    # -----------------------------
    # Download
    # -----------------------------

    df = pd.DataFrame(
        result.items(),
        columns=["Attribute", "Value"]
    )

    st.download_button(
        "⬇ Download Prediction",
        df.to_csv(index=False),
        file_name="prediction.csv",
        mime="text/csv"
    )