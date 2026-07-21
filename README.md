# Predictive Maintenance and Machine Failure Forecasting

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-live-FF4B4B)](https://predictivemaintenecemodelproject-6lvf7mfwxh8mkf5hwxdf7s.streamlit.app/)
[![Code License: MIT](https://img.shields.io/badge/Code%20License-MIT-green.svg)](LICENSE)
[![Dataset License: CC BY--NC--SA 4.0](https://img.shields.io/badge/Dataset%20License-CC%20BY--NC--SA%204.0-orange.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

An applied machine-learning and Streamlit project for exploring machine-failure risk from drilling-process data. The application accepts CSV or Excel input, validates the required features, visualises selected operating variables and applies a trained Random Forest classifier to generate a failure-risk prediction.

> **Important:** This repository is an educational, research and portfolio demonstration. It is not a certified industrial monitoring, maintenance or safety system.

## Live application

- **Streamlit application:** https://predictivemaintenecemodelproject-6lvf7mfwxh8mkf5hwxdf7s.streamlit.app/
- **Application entry point:** [`MLapp_ped.py`](MLapp_ped.py)

## Problem addressed

Machine-failure datasets can contain substantially fewer failure cases than normal-operation cases. Accuracy alone may therefore obscure poor performance on the minority class. This project explores predictive-maintenance classification with attention to failure detection, model evaluation and the practical presentation of predictions through an accessible web interface.

## Application workflow

1. Upload a CSV or Excel file.
2. Validate that the required model features are present.
3. Preview the uploaded records.
4. Select one or more observations for analysis.
5. Visualise cutting speed, feed, feed rate, power, cooling and process time.
6. Apply the trained classifier to the selected observation.
7. Display the predicted machine condition and estimated failure probability.

The interface also displays an illustrative time-to-failure estimate derived from the predicted probability. This estimate is heuristic, has not been independently calibrated against real failure-time outcomes and must not be interpreted as an engineering forecast.

## Required input features

The deployed application expects the following columns:

```text
Cutting_speed
Feed
Feed_rate
Power
Cooling
Process_Time
Material_K
Material_N
Material_P
Drill_Bit_Type_H
Drill_Bit_Type_N
Drill_Bit_Type_W
```

## Dataset

This project uses the **Explainable AI (XAI) Drilling Dataset**, published on Kaggle by Raphael Wallsberger.

- **Source:** https://www.kaggle.com/datasets/raphaelwallsberger/xai-drilling-dataset
- **Dataset licence:** [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)

The source dataset is not redistributed through this repository. Users should obtain it directly from the Kaggle publisher and comply with the applicable licence terms.

The dataset was processed for exploratory analysis, feature preparation, machine-learning evaluation and application demonstration. Where the material is shared or adapted, users must provide appropriate attribution, indicate changes, restrict use to non-commercial purposes and comply with the ShareAlike condition. This repository does not imply endorsement by the dataset publisher or Kaggle.

## Technical implementation

The public application is implemented with:

- Python
- Streamlit
- pandas and NumPy
- scikit-learn-compatible model serialisation
- Plotly
- openpyxl for Excel input

The application loads the trained model from `PM_random_forest_model.pkl`, checks uploaded data against the expected feature schema and uses the model's `predict` and `predict_proba` methods to produce the displayed classification and probability.

## Reported experimental results

Project experiments reported a ROC-AUC of **0.998** and failure-class recall of **1.00** for a selected configuration. These are project results rather than independent industrial validation. They should be interpreted in the context of the data split, sampling design, dataset representativeness and the risks of applying a model outside its source population.

## Professional feedback

In September 2024, the application received documented professional feedback addressing its workability, simplicity and user-friendly design. The reviewer also identified possible future development through maintenance-management integration and longer-term trend analysis.

This feedback represents an informed review of the application's usability and potential development path. It does **not** establish formal organisational adoption, production deployment or independent validation of the model's statistical performance.

## Run locally

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/AbiodunAnalyst/Predictive-Analytics.git
cd Predictive-Analytics
python -m venv .venv
```

Activate the environment and install the packages used by the public application:

```bash
pip install -r requirements.txt
streamlit run MLapp_ped.py
```

The current `requirements.txt` declares Streamlit, pandas, NumPy, scikit-learn, Plotly and openpyxl, which correspond to the dependencies used by the public application. The trained model file `PM_random_forest_model.pkl` must also be present in the repository root for prediction to work.

The dependency file currently identifies the required packages without fixing exact versions. For stronger reproducibility, a future release should record versions tested together in a clean environment.

## Repository structure

```text
MLapp_ped.py                  Streamlit application
PM_random_forest_model.pkl   Serialised Random Forest model
README.md                     Project documentation
requirements.txt              Application dependencies
LICENSE                       Licence for original repository code
CONTRIBUTING.md               Contribution guidance
SECURITY.md                   Security reporting guidance
CITATION.cff                  Citation metadata
```

## Limitations and responsible use

- The results have not been independently validated across different machines, sites or operating conditions.
- Uploaded files should not contain confidential, personal or commercially sensitive information.
- Predictions must not replace engineering inspection, manufacturer guidance or established safety controls.
- The failure probability is model-dependent and is not a direct measurement of physical condition.
- The time-to-failure display is an illustrative heuristic and is not a validated remaining-useful-life model.
- Model performance may change substantially when the input distribution differs from the training data.

## Contributing

Constructive issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Please provide reproducible steps, tests where appropriate and a clear explanation of the proposed improvement.

Useful review areas include:

- reproducibility and environment pinning;
- input-schema and data-quality validation;
- model calibration and uncertainty;
- evaluation on independent drilling datasets;
- tests for prediction and file-upload behaviour;
- replacement of the illustrative time-to-failure calculation with a properly validated method.

## Security

See [SECURITY.md](SECURITY.md). Do not place credentials, confidential operational records or private datasets in issues, pull requests or uploaded examples.

## Citation

Citation metadata is available in [CITATION.cff](CITATION.cff).

## Licensing

Original source code authored for this repository is available under the [MIT License](LICENSE), unless otherwise stated.

The XAI Drilling Dataset is **not** covered by the MIT License. It remains subject to CC BY-NC-SA 4.0. Third-party datasets, libraries, images, model artefacts and other materials may be governed by separate terms and are not relicensed by this repository.
