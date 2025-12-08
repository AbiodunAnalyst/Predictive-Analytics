import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import plotly.graph_objects as go

# Load model
model_path = 'PM_random_forest_model.pkl'
if not os.path.exists(model_path):
    st.error("Model file not found.")
else:
    model = pickle.load(open(model_path, 'rb'))

def load_data(file):
    try:
        if file.name.endswith('.csv'):
            data = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            import openpyxl  # Ensure openpyxl is imported when needed
            data = pd.read_excel(file)
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            return None
        return data
    except Exception as e:
        st.error(f"Error reading the file: {e}")
        return None

def plot_line_charts(data, selected_rows, feature_columns):
    for col in feature_columns:
        fig = go.Figure()

        try:
            fig.add_trace(go.Scatter(
                x=selected_rows,
                y=data.loc[selected_rows, col],
                mode='lines+markers',
                line=dict(color='royalblue', width=4),
                marker=dict(color='darkorange', size=10)
            ))

            fig.update_layout(
                title=f'{col.replace("_", " ").title()} over Selected Rows',
                xaxis_title='Row Index',
                yaxis_title=col.replace("_", " ").title(),
                plot_bgcolor='white',
                showlegend=False,
                xaxis=dict(
                    showgrid=False,  # Remove gridlines
                    zeroline=False,  # Remove zero line
                    showline=True,   # Show axis lines
                    linewidth=2,
                    linecolor='black'
                ),
                yaxis=dict(
                    showgrid=False,  # Remove gridlines
                    zeroline=False,  # Remove zero line
                    showline=True,   # Show axis lines
                    linewidth=2,
                    linecolor='black'
                )
            )

            st.plotly_chart(fig)
        except Exception as e:
            st.error(f"Error plotting line chart for {col}: {e}")

def estimate_time_to_failure_in_hours(prediction_proba):
    # Assuming the maximum possible time to failure is 1 year (365 days * 24 hours)
    max_hours = 365 * 24

    if prediction_proba < 0.3:
        # If probability is low, machine is expected to run for most of the year
        estimated_hours = max_hours * (1 - prediction_proba)
    elif prediction_proba < 0.7:
        # If probability is medium, machine may fail within 6 months to 1 year
        estimated_hours = max_hours * (0.7 - prediction_proba)
    else:
        # If probability is high, machine is likely to fail within 6 months
        estimated_hours = max_hours * (1 - prediction_proba) * 0.5  # Assuming a higher probability reduces the time significantly

    return max(estimated_hours, 1)  # Ensure that the estimated time is at least 1 hour

def main():
    st.title('Prediction of Machine Failure for Maintenance')

    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        data = load_data(uploaded_file)
        if data is not None:
            try:
                # Check if required columns exist
                required_columns = ['Cutting_speed', 'Feed', 'Feed_rate', 'Power', 'Cooling', 'Process_Time', 
                                    'Material_K', 'Material_N', 'Material_P', 
                                    'Drill_Bit_Type_H', 'Drill_Bit_Type_N', 'Drill_Bit_Type_W']
                missing_columns = [col for col in required_columns if col not in data.columns]
                if missing_columns:
                    st.error(f"Missing required columns: {', '.join(missing_columns)}")
                    return

                st.write("Data preview:")
                st.write(data.head())  # Display the first few rows of the data
                
                # Allow user to select multiple rows of data
                selected_rows = st.multiselect("Select rows (indices) for analysis", options=data.index.tolist())
                if not selected_rows:
                    st.error("Please select at least one row.")
                    return
                
                # Plot line charts for the specified features only
                feature_columns = ['Cutting_speed', 'Feed', 'Feed_rate', 'Power', 'Cooling', 'Process_Time']
                plot_line_charts(data, selected_rows, feature_columns)
                
                # Automatically populate the input fields with the data from the last selected row
                last_row_index = selected_rows[-1]
                selected_row = data.loc[last_row_index]

                inputs = {}
                for col in required_columns:
                    try:
                        inputs[col] = st.number_input(f'{col.replace("_", " ").title()}', value=float(selected_row[col]))
                    except ValueError:
                        st.error(f"Error with input value for {col}. Please ensure the data is numeric.")

                # Prepare input data for prediction based on the last selected row
                input_data = np.array([list(inputs.values())])
                
                # Prediction and displaying results
                if st.button('Predict'):
                    if model:
                        try:
                            # Get prediction probability
                            prediction_proba = model.predict_proba(input_data)[0][1]  # Probability of failure
                            prediction = model.predict(input_data)[0]
                            
                            decoded_output = 'Machine Failure, Need Maintenance' if prediction == 1 else 'Machine Still in Good Condition to Run'
                            st.success(f'Predicted condition: {decoded_output}')
                            st.info(f"Probability of Failure: {prediction_proba:.2f}")

                            # Estimate time to failure in hours
                            time_to_failure_hours = estimate_time_to_failure_in_hours(prediction_proba)
                            st.warning(f"Estimated Time to Failure: {time_to_failure_hours:.2f} hours")
                            
                        except Exception as e:
                            st.error(f"Error during prediction: {e}")
                    else:
                        st.error("Model not loaded.")
            except Exception as e:
                st.error(f"Error processing data: {e}")

if __name__ == '__main__':
    main()
