# Project Consolidation & Development Roadmap

This roadmap outlines the phased approach to consolidate the project and move forward with new development.

---

### Phase 1: Setup New Repository & Environment

**Goal:** Create a clean, organized foundation for all future work.

1.  **Create New GitHub Repository:**
    *   Create a new **private** repository named `SnipsClips-Analysis`.
    *   Initialize it with a `README.md`, a Python-specific `.gitignore`, and a `LICENSE` (e.g., MIT).

2.  **Set Up Local Environment:**
    *   Clone the new repository to your local machine (e.g., `C:\Users\lbohn\SnipsClips-Analysis`).
    *   Create a virtual environment (`python -m venv .venv`).
    *   Install the dependencies from the old `requirements.txt` into the new virtual environment.

3.  **Establish Branching Strategy:**
    *   Create a `develop` branch from `main`.
    *   Protect the `main` branch in GitHub settings, requiring pull requests for all merges.

4.  **Create Workspace Configuration:**
    *   Create a `.code-workspace` file to define project settings and ensure consistent linter/tooling behavior.

---

### Phase 2: Migrate V1 Gemma Pipeline

**Goal:** Get the existing V1 Gemma pipeline running in the new, clean repository structure.

1.  **Establish Core Structure & Runner:**
    *   Create the new `src`, `data`, `docs`, and `notebooks` directory structure.
    *   Create a new main entry point (`run.py`) that is configuration-driven.
    *   Create a central `config.yml` to manage all paths, models, and settings.
    *   Refactor `logging_setup.py` to be config-driven.
    *   Create placeholder functions for all 5 pipeline steps.
    *   Verify the new runner works end-to-end with placeholder steps.

2.  **Implement Step 1 (Data Ingestion):**
    *   Create `identity.py` and `data_structures.py` utilities in the new `src` directory.
    *   Implement `execute_step1` to load raw data, scan media, generate `tweet_id`s, and merge into a single dataset.
    *   Test Step 1 independently to ensure it produces the correct combined dataset.

3.  **Implement Step 2 (Preprocessing):**
    *   Refactor the preprocessing logic from the old scripts into `execute_step2`.
    *   Ensure all file paths are read from `config.yml`.
    *   Test Step 2 independently.

4.  **Implement Step 3 (Transcription):**
    *   Refactor the `openai-whisper` logic into `execute_step3`.
    *   This step should be config-driven, allowing for model size selection.
    *   Test Step 3 independently.

5.  **Implement Step 4 (VLM Analysis):**
    *   Create a simple API client in `src/modeling/lm_studio_client.py`.
    *   Implement `execute_step4` to send data to the LM Studio API endpoint defined in `config.yml`.
    *   This will involve reading a prompt template and formatting the data for the API call.
    *   Test Step 4 independently.

6.  **Implement Step 5 (Analysis & Dashboard):**
    *   Refactor the analysis logic (comparison metrics) into `execute_step5`.
    *   Refactor the dashboard generation logic into `src/visualization/`.
    *   The runner will call the dashboard generation after the pipeline completes.
    *   Test Step 5 and the dashboard generation.

---

### Phase 3: V2 - HCA Integration & New Features

**Goal:** Integrate the new "Step 6 HCA" codebook and expand project capabilities.

1.  **Develop Step 6 (HCA):**
    *   Create a new `execute_step6` function.
    *   Implement the logic for the Human Coding Assignment based on the new codebook.
    *   Update `config.yml` with any new paths or settings required for Step 6.

2.  **Refine and Validate:**
    *   Run the full v2 pipeline (Steps 1-6).
    *   Validate the results and compare them against the v1 outputs.
    *   Update the dashboard to include visualizations for the new HCA data.

3.  **Final Documentation & Cleanup:**
    *   Update the main `README.md` with final instructions for running the v2 pipeline.
    *   Clean up any remaining old files or artifacts.
    *   Archive the old repositories (`Snips` and `SnipsClipsHate`).

---

### Post-Consolidation:

- The `Snips` and `SnipsClipsHate` repositories can be archived on GitHub.
- All new work will happen exclusively in the `SnipsClips-Analysis` repository. 