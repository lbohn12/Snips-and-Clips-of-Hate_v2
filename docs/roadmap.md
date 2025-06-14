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

---

### Phase 2: Migrate and Finalize V1 (Gemma Pipeline)

**Goal:** Get the best version of the V1 pipeline running and visualize its results.

1.  **Migrate Core Pipeline:**
    *   Create a new branch: `feature/migrate-gemma-pipeline`.
    *   Copy the refactored pipeline scripts from `Snips/scripts/core/refactored/` into the new project's `src/` directory.
    *   Copy the best-performing model configuration (for Gemma-3/4B).
    *   Update scripts to use a centralized configuration file instead of hardcoded paths.

2.  **Migrate Dashboard & Visualization:**
    *   Copy the dashboard generator scripts from `Snips/scripts/visualization/` into `src/visualization/`.
    *   Ensure the dashboard can correctly process the output from the Gemma pipeline.

3.  **Run and Validate:**
    *   Run the full Gemma pipeline on the 1500 posts.
    *   Generate the final dashboard.
    *   Commit the generated dashboard (as a static HTML file) and key charts to a new `results/v1_gemma/` directory.

4.  **Merge and Tag:**
    *   Merge `feature/migrate-gemma-pipeline` into `develop`.
    *   Merge `develop` into `main`.
    *   Create a git tag `v1.0.0` to mark the official completion of V1.

---

### Phase 3: Develop V2 (HCA Integration)

**Goal:** Integrate the new Hierarchical Cluster Analysis based on the new codebook.

1.  **Create V2 Feature Branch:**
    *   Create a new branch from `develop`: `feature/step6-hca-analysis`.

2.  **Develop Step 6 Module:**
    *   Create a new module `src/pipeline/step6_hca.py`.
    *   Implement the HCA logic.
    *   Define the inputs (likely the CSV output from a previous step) and outputs (cluster data, visualizations).

3.  **Integrate into Pipeline Runner:**
    *   Update the main pipeline runner to include `step6` as an executable step.
    *   Update configuration to manage settings for Step 6.

4.  **Update Dashboard for V2:**
    *   Create a new dashboard or add a new section to the existing one to visualize the HCA results.

5.  **Merge and Tag:**
    *   When complete, merge `feature/step6-hca-analysis` into `develop`.
    *   This will eventually become `v2.0.0`.

---

### Post-Consolidation:

- The `Snips` and `SnipsClipsHate` repositories can be archived on GitHub.
- All new work will happen exclusively in the `SnipsClips-Analysis` repository. 