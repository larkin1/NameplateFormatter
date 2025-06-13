import streamlit as st
import pandas as pd

# Show title and description.
st.title("Nameplate Formatter")

def reset_file():
    if "file" in st.session_state:
        del st.session_state["file"]
    st.rerun()

if "file_bytes" not in st.session_state:
    uploaded_file = st.file_uploader("Upload file")
    if uploaded_file is not None:
        st.session_state.file_bytes = uploaded_file.getvalue()
        st.session_state.file_name = uploaded_file.name
        st.rerun()
else:
    file_bytes = st.session_state.file_bytes
    file_name = st.session_state.file_name
    # Use BytesIO to load into pandas
    import io
    if file_name.endswith(".csv"):
        df = pd.read_csv(io.StringIO(file_bytes.decode()))
    else:
        df = pd.read_excel(io.BytesIO(file_bytes))

        st.write("Select the below Checkboxes to extract.")

        selected_cols = [col for col in df.columns if st.checkbox(col)]

        if selected_cols:
            st.write("**Formatted Output**")
            for _, row in df[selected_cols].iterrows():
                for col in selected_cols:
                    st.write(f"{col}: {row[col]}")
                st.write("------")


        # if selected_cols:
        #     st.write("**Formatted Output**")
        #     group_col = selected_cols[0]

        #     for group_value, group_df in df.groupby(group_col):
        #         st.write(f"**{group_value}**")
        #         for _, row in group_df.iterrows():
        #             for col in selected_cols[1:]:
        #                 st.write(f"{col}: {row[col]}")
        #             st.write("------")
            

