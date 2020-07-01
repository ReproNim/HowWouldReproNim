# HowWouldReproNim

Sphinx rendering of the "How Would ReproNim Do That?" series.

## Building

Build the documentation:

    # create a venv to not mess with anything else
    virtualenv --python=python3.7 ~/env/repro
    . ~/env/repro

    # install from requirements.txt
    pip install -r requirements.txt

    # build the docs
    make html

    # view in browser
    firefox _build/html/index.html

    # build the PDF (this probably requires a lot of LaTeX stuff being installed,
    # so no guarantee that it works out of the box ;-) 
    make latexpdf
