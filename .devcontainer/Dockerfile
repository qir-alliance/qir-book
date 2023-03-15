# FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04 AS qat-build
# ADD https://apt.llvm.org/llvm-snapshot.gpg.key /llvm-snapshot.gpg.key
# ARG DEBIAN_FRONTEND=noninteractive
# RUN apt-get update && \
#     apt-get install -y git gnupg2 software-properties-common cmake && \
#     apt-key add /llvm-snapshot.gpg.key && \
#     add-apt-repository "deb https://apt.llvm.org/jammy/ llvm-toolchain-jammy-14 main" && \
#     apt-get -y update && \
#     apt-get -y install clang-14 clang-format-14 clang-tidy-14 llvm-14 && \
#     apt autoremove -y && \
#     apt-get clean && rm -rf /var/lib/apt/lists/
# ENV CC=clang-14 CXX=clang++-14 SHELL=/usr/bin/bash
# RUN mkdir /qat && \
#     git clone --depth 1 --recursive https://github.com/qir-alliance/qat.git /qat && \
#     mkdir /qat/Debug && \
#     cd /qat/Debug && \
#     cmake .. && \
#     make qat

# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/python-3-anaconda/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/miniconda:latest

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/

# Install mamba for faster package resolution and installation
RUN conda install -n base -c conda-forge mamba

# Copy environment.yml (if found) to a temp location so we create the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/mamba env create -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp


# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
# COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
# RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env create -f /tmp/conda-tmp/environment.yml; fi \
#     && rm -rf /tmp/conda-tmp

# Stuff for qat
# RUN wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add - && \
#     sudo add-apt-repository "deb https://apt.llvm.org/focal/ llvm-toolchain-focal-13 main" && \
#     sudo apt-get -y update && \
#     sudo apt-get -y remove llvm-10 && \
#     sudo apt-get -y install clang-13 clang-format-13 clang-tidy-13 && \
#     sudo apt autoremove -y && \
#     npm install -g prettier@2.2.1
# ENV CC=clang-13 CXX=clang++-13

# NEED CLANG 11!!!

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
 COPY --from=qat-build /qat/Debug/qir/qat/Apps/qat /bin/qat