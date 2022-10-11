FROM devfactory/workspace-full:latest

RUN pyenv install 3.9-dev
RUN pyenv global 3.9-dev
RUN python3 -m pip install mypy
