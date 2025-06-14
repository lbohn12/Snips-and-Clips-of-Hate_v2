# SnipsClips Project Rebuild Plan

This directory outlines the plan to consolidate the work from the `Snips` and `SnipsClipsHate` repositories into a single, clean, and maintainable project.

The history of the project involves rapid evolution across multiple models (Qwen, SmolVLM, Phi-3.5, Gemma-3) and a major refactoring effort. This has led to a complex repository state that is difficult to manage.

**The core strategy is to create a new, single repository and migrate the best components of the previous work into it, rather than trying to untangle the existing branch history.**

This will allow us to:
1.  Finally generate and visualize the results from the promising Gemma model.
2.  Establish a stable foundation (`v1`) for the project.
3.  Proceed with the new "Step 6 HCA Integration" (`v2`) in an organized manner. 