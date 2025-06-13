import streamlit as st
import pandas as pd

st.set_page_config('Nameplates', "Logo.png")

# Show title and description.
st.title("Nameplate Formatter")

def reset_file():
    if "file" in st.session_state:
        del st.session_state["file"]
    st.rerun()

if "file" not in st.session_state:
    st.write("Please upload an Excel sheet below for the app to process. ")
    
    uploaded_file = st.file_uploader("Upload a document (xlsx or csv)", type=("xlsx", "csv"))
    
    if uploaded_file is not None:
        st.session_state.file = uploaded_file
        st.rerun()
    
else: 
    st.success("File Uploaded!")
    if st.button("Remove File"):
        reset_file()
    else:
        uploaded_file = st.session_state.file

        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file, dtype=str)
        else:
            df = pd.read_excel(uploaded_file, dtype=str)

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
            

