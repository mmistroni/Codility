# Use the official Python 3.12 slim image based on Debian Bookworm
# 'slim' images are smaller than the full images, but still include common build tools.
# 'bookworm' is the codename for Debian 12, which is the current stable release.
FROM python:3.12-slim-bookworm

# Set the working directory in the container
# Use a specific path for consistency within the devcontainer
WORKDIR /workspaces/Codility # Adjust 'your-project-name' to your actual project folder name

# Create a non-root user (good practice for security)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN addgroup --gid $USER_GID $USERNAME \
    && adduser --uid $USER_UID --gid $USER_GID --disabled-password --shell /bin/bash $USERNAME \
    && apt-get update \
    && apt-get install -y --no-install-recommends git iproute2 procps \
    && rm -rf /var/lib/apt/lists/*
USER $USERNAME

# Copy requirements.txt from the repository root to the current working directory in the container
# The `COPY ../requirements.txt .` means "copy `requirements.txt` from the parent directory
# of the current Dockerfile context (`.devcontainer`) to the current directory (`WORKDIR`)
# inside the container."
COPY ../requirements.txt .

# Create a virtual environment and install dependencies
# This is done during the Docker image build time, leveraging caching.
RUN python3 -m venv .venv && \
    . ./.venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Add the virtual environment's bin directory to the PATH
# This ensures that `python` and `pip` automatically refer to the venv's executables
# when a terminal is opened in the Codespace.
ENV PATH="/workspaces/Codility/.venv/bin:$PATH" 



RUN  echo "Finished"