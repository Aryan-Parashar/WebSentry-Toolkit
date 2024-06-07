import subprocess
import csv
import os
import streamlit as st

script_paths = [
    
]
csv_file_path = ""

# Function to run a script and capture its output
def run_script(script_path):
    script_dir = os.path.dirname(script_path)
    result = subprocess.run(['python', os.path.basename(script_path)], cwd=script_dir, capture_output=True, text=True, shell=True)
    return result.stdout

# Streamlit app
st.title("Web Sentinel OWASP Top 40 Web Application VAPT Tool-kit : WebSentry")

# Button for each script with unique keys
for index, script_path in enumerate(script_paths):
    button_key = f"button_{index}"
    if st.button(f"Run {os.path.basename(script_path)}", key=button_key):
        with st.spinner(f"Running {os.path.basename(script_path)}..."):
            output = run_script(script_path)
            st.text_area(f"Output of {os.path.basename(script_path)}", output, key=f"output_{index}")

# Save outputs to CSV
if st.button("Save Outputs to CSV", key="save_csv"):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['Script', 'Output']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for script_path in script_paths:
            output = run_script(script_path)
            writer.writerow({
                'Script': script_path,
                'Output': output,
            })

    st.success(f"Outputs saved to {csv_file_path}")
