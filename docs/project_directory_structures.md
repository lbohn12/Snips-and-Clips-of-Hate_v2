# Proposed Project Directory Structure for `SnipsClips-Analysis`

This structure organizes the project for clarity, scalability, and reproducibility.

```
/Snips-and-Clips-of-Hate_v2
|
|-- .github/                # GitHub-specific files (e.g., issue templates, workflows for CI/CD)
|-- .gitignore              # Standard Python gitignore
|-- .venv/                  # Virtual environment directory (ignored by git)
|-- LICENSE                 # Project license file (e.g., MIT)
|-- README.md               # High-level project overview, setup, and usage instructions
|-- requirements.txt        # Project dependencies
|-- config.yml              # Centralized configuration for pipeline, models, and paths
|
|-- data/
|   |-- raw/                # The original, immutable data
|   |   |-- posts.csv
|   |   `-- media/
|   |
|   |-- processed/          # Intermediate or processed data from the pipeline
|   |   |-- step1_output.csv
|   |   `-- step4_output.json
|   |
|   `-- external/           # External data sources (e.g., codebooks)
|       `-- codebook_v2.csv
|
|-- docs/                   # Project documentation (like this file)
|
|-- notebooks/              # Jupyter notebooks for exploration and analysis
|   |-- 1-initial-exploration.ipynb
|   `-- 2-results-analysis.ipynb
|
|-- results/                # Final outputs like reports, charts, and dashboards
|   |-- v1_gemma/
|   |   |-- dashboard.html
|   |   `-- agreement_chart.png
|   |
|   `-- v2_hca/
|       `-- cluster_visualization.png
|
|-- src/                    # All source code
|   |-- __init__.py
|   |
|   |-- config_loader.py    # Utility to load `config.yml`
|   |-- main.py             # Main entry point to run the pipeline
|   |
|   |-- pipeline/
|   |   |-- __init__.py
|   |   |-- step1_db_retrieval.py
|   |   |-- step2_media_download.py
|   |   |-- step3_media_validation.py
|   |   |-- step4_model_analysis.py
|   |   |-- step5_analysis_comparison.py
|   |   `-- step6_hca.py
|   |
|   `-- visualization/
|       |-- __init__.py
|       `-- dashboard_generator.py
|
`-- tests/                  # Unit and integration tests
    |-- test_pipeline.py
    `-- test_visualization.py

``` 