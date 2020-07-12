# render-matplotlib

Render matplotlib as azure function


See All Renders at: https://idvorkin-mpl-render.azurewebsites.net/api/Debug

Example usage:  https://idvorkin-mpl-render.azurewebsites.net/api/Render?name=productivity

Used by http://idvork.in to avoid saving copied blobs (with a huge performance hit)

See directions for command line execution @ 

https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function-azure-cli?pivots=programming-language-python&tabs=bash%2Cbrowser

One time setup

    python3 -m venv .venv
    pip install -r requirements.txt

Init virtual env: 

    source .venv/bin/activate

Run Unit Tests

    python3 -m unittest

Simulate func env

    func start






Also contains unittests

