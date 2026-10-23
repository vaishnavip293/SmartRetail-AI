# GitHub Upload Guide

Repository name: `SmartRetail-AI`

## Recommended contents
Upload the contents of this folder to the root of a **Public** GitHub repository. Keep the folder structure intact, especially `data/`, `src/`, `outputs/`, `models/`, `reports/`, `tests/`, and `powerbi/`.

## Main internship submission files
- `Vaishnavi_Dipak_Patil_SmartRetail_AI.ipynb` — notebook code and analysis
- `requirements.txt` — Python dependencies
- `Vaishnavi_Dipak_Patil_ProjectReport.docx` — project report
- `README.md` — project overview, dataset details, technologies and run steps

## Output evidence
The `outputs/` directory contains summary JSON, CSV result tables, forecast output, evaluation metrics and chart PNGs. `reports/` contains data-quality and analysis summaries.

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python src/run_pipeline.py
pytest -q
```

## Dataset note
The dataset was provided in the project materials. It is included at `data/raw/supermarket_sales.csv`; the cleaned data is at `data/processed/supermarket_sales_clean.csv`. No external public dataset URL was supplied, so do not claim an unverified external source.

## Important
Before sharing publicly, review the files for private information or secrets. Do not commit passwords, tokens, or API keys. If the institution requires a direct public dataset link, create one from the dataset's verified original source or use the repository's dataset file link after uploading.
