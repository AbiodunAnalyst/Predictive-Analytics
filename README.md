# Predictive Maintenance & Machine Failure Forecasting

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-live-FF4B4B)](https://predictivemaintenecemodelproject-6lvf7mfwxh8mkf5hwxdf7s.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-green.svg)](LICENSE)

An end-to-end machine-learning project that explores imbalanced classification for drilling-machine failure prediction and exposes the analytical workflow through a browser-based Streamlit demonstration.

## Problem addressed

Equipment-failure datasets often contain far fewer failure records than normal operations. A model can appear accurate while missing the minority class that matters most. This project investigates that imbalance and compares modelling approaches intended to identify failure risk from operational variables.

## Public demonstration

- Live app: https://predictivemaintenecemodelproject-6lvf7mfwxh8mkf5hwxdf7s.streamlit.app/
- App entry point: `MLapp_ped.py`

The deployment is a technical demonstration and should not be treated as a certified industrial monitoring or safety system.

## Dataset

This project uses the **Explainable AI (XAI) Drilling Dataset**, published by Raphael Wallsberger on Kaggle.

- Dataset source: https://www.kaggle.com/datasets/raphaelwallsberger/xai-drilling-dataset
- Dataset licence: CC BY-NC-SA 4.0
- Licence terms: https://creativecommons.org/licenses/by-nc-sa/4.0/

The original dataset is not redistributed through this repository. Users should obtain it directly from the publisher's Kaggle page and comply with the applicable licence terms.

The dataset was processed for exploratory analysis, feature preparation, machine-learning evaluation and application demonstration. Any changes made during preprocessing are described in the project documentation or source code.

This repository does not imply endorsement by the dataset creator or Kaggle.

## Technical workflow

1. Load and validate operational data.
2. Explore feature distributions, correlations and failure patterns.
3. Split training and test data without leaking test information.
4. Address class imbalance using resampling strategies evaluated in the project.
5. Train and compare tree-based classification models.
6. Evaluate minority-class recall, ROC-AUC, confusion matrices and generalisation.
7. Examine feature and permutation importance.
8. expose a selected workflow through Streamlit.

## Technologies

- Python
- pandas and NumPy
- scikit-learn
- XGBoost
- imbalanced-learn
- Optuna
- Matplotlib and seaborn
- Streamlit

## Reported experimental results

The project notebook/README reports ROC-AUC of 0.998 and failure-class recall of 1.00 for selected configurations.

These are project results, not independent industrial validation. They should be interpreted alongside:

- the train/test split and sampling design;
- the possibility of correlated or duplicated records;
- dataset representativeness;
- uncertainty outside the source data;
- the cost of false positives and false negatives in a real operational setting.

> **[ACTION REQUIRED]** Add one reproducible command or notebook section that regenerates the reported metrics from the documented dataset. Include the exact random seed and package versions.

## Run locally

```bash
git clone https://github.com/AbiodunAnalyst/Predictive-Analytics.git
cd Predictive-Analytics
python -m venv .venv
```

Activate the virtual environment, then install the repository’s verified dependencies:

```bash
pip install -r requirements.txt
streamlit run MLapp_ped.py
```

> **[ACTION REQUIRED]** Generate and test `requirements.txt` from a clean environment before publishing these instructions.

## Repository structure

```text
MLapp_ped.py          Streamlit application
README.md             Project documentation
requirements.txt      Reproducible Python dependencies
figures/              Recommended location for generated figures
notebooks/            Recommended location for model experiments
```

The existing files may need reorganising into the recommended folders. Preserve history through normal file-move commits.

## Intended use and limitations

- Educational and portfolio demonstration of predictive-maintenance analytics.
- Not a substitute for engineering inspection, safety controls or certified maintenance systems.
- Performance has not been independently validated across different machines, sites or operating regimes.
- Uploaded data must not contain confidential or personal information.
- A prediction should not be the sole basis for safety-critical action.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Please include reproducible steps, tests where applicable and a clear explanation of the proposed change.

## Security

See [SECURITY.md](SECURITY.md). Do not include credentials, confidential operational records or private datasets in issues or pull requests.

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff).

## Licence

Code authored for this repository is available under the [MIT License](LICENSE). Third-party datasets, images and other assets remain subject to their original terms and are not relicensed by this repository.
