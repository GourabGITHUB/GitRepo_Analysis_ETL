A lightweight, modular CLI-based ETL pipeline designed to extract repository metadata from the GitHub Public API and persist it locally in structured formats.

🛠 Features
Dynamic Extraction: Fetches real-time data for any public GitHub username.

Data Transformation: Cleans and organizes repository names, primary languages, and last-updated timestamps.

Flexible Loading: Supports both .csv and .parquet output formats via CLI arguments.

Containerized: Fully Dockerized for environment consistency.

🏗 Architecture Overview
The project follows a standard functional ETL pattern to ensure maintainability and testability:

Ingest: Fetches raw JSON data from GitHub’s REST API.

Transform: Cleans the payload, extracting repo names, primary languages, and timestamps.

Load: Serializes the transformed data into the requested file format.

Run Pipeline: The orchestration layer that ties the CLI arguments to the logic.

🚀 Usage

Create a .env file in the root directory:
# .env file
API=https://api.github.com/users/

Local Execution
Ensure you have the required dependencies installed, then run the pipeline:

python run_pipeline.py --username <github_username> #optional --format <csv|parquet>
Example: python run_pipeline.py --username octocat

Running with Docker
To ensure your data persists on your host machine, use a volume flag (-v) to map your current working directory to the container's output folder.

Build image:
docker build -t git-etl-app .

Run the container:
docker run -v $(pwd):/output --env-file filepath/name --name git-etl-container git-etl-app --username <github_username> --format csv
IMPORTANT: make sure UID/GID of the container user does match the owner of $(pwd)/output on the host. #use the -u (or --user) flag in docker run

📊 Data Pipeline Flow
Ingest: Requests user repository data from public API api.github.com/users/{user}/repos.

Transform: Extracts name, language, and updated_at.

Load: Serializes the data and saves .csv to the current working directory.
