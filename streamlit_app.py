import streamlit as st
import openai

# Set your OpenAI API key here

# Define the report template as a function
def generate_audit_report(control_name, control_objective, evidence_reviewed, findings, conclusion):
    prompt_template = f"""
    Generate an internal audit report for a banking client based on the information provided.

    Executive Summary:
    Summarize the overall purpose of the audit and key outcomes.

    Objective and Scope:
    Describe the objective and scope of the audit.

    Key Findings and Observations:
    - **Control Name**: {control_name}
    - **Control Objective**: {control_objective}
    - **Evidence Reviewed**: {evidence_reviewed}
    - **Findings**: {findings}
    - **Conclusion**: {conclusion}

    Recommendations and Action Plans:
    Provide recommendations to mitigate identified risks.

    Conclusion:
    Summarize the final conclusions of the audit and overall risk posture.
    """
    
    # Call the OpenAI API to generate the report
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can also use "gpt-3.5-turbo" for a more economical option
        messages=[{"role": "user", "content": prompt_template}],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']

# Streamlit app interface
st.title("Internal Audit Report Generator")
st.write("Enter the details below to generate an audit report.")

# Input fields for the control details
control_name = st.text_input("Control Name", value="IT Asset Management Policy Review")
control_objective = st.text_area("Control Objective", value="To ensure IT assets are managed effectively in line with regulatory standards.")
evidence_reviewed = st.text_area("Evidence Reviewed", value="Policy document, review communications, and board meeting minutes.")
findings = st.text_area("Findings", value="Policy was reviewed but lacks board approval documentation.")
conclusion = st.text_area("Conclusion", value="Control design requires improvement to ensure compliance.")

# Generate report button
if st.button("Generate Report"):
    with st.spinner("Generating report..."):
        # Generate the report using the provided details
        report = generate_audit_report(control_name, control_objective, evidence_reviewed, findings, conclusion)
        st.success("Report generated successfully!")
        st.write("### Audit Report")
        st.write(report)

# Option to download the report as a text file
if 'report' in locals() and report:
    st.download_button(
        label="Download Report",
        data=report,
        file_name="audit_report.txt",
        mime="text/plain"
    )
