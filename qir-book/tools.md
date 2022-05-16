# How does this book build?

This book uses the [Jupyter Book](https://jupyterbook.org/en/stable/index.html) toolchain to build the prose and run the code contained in the sample notebooks. The code is run in notebooks with a variety of kernels to provide a variety of environments for running code. There is a [docker container] specified that is fully setup to build the book.

## Jupyter Book

Helpful links:

- [Fancy syntax for prose styling](https://jupyterbook.org/en/stable/content/content-blocks.html?highlight=glossary#special-content-blocks)

## Docker environment

TBD

## Building the book

To build the docs locally:

1. Create a python environment with either the conda `environment.yml` or the `requirements.txt`.
2. Run `jupyter-book build ./qir-book` from the root of the project and it should run the notebooks and build the html version of the book that you can view from `./qir-book/_build/html/index.html`.
