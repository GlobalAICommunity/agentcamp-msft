FROM mcr.microsoft.com/devcontainers/python:3.13-bookworm

# Install pip for Python 3.13
RUN python -m pip install --upgrade pip


# Install the packages required for development
COPY requirements-dev.txt .
COPY build_and_launch_AI_agents_fast_with_Microsoft_Foundry_and_the_AI_Toolkit/src/python/requirements.txt build_and_launch_AI_agents_fast_with_Microsoft_Foundry_and_the_AI_Toolkit/src/python/
COPY data/requirements.txt data/
RUN pip install -r requirements-dev.txt

ENV ENVIRONMENT=container