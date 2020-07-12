import logging
import azure.functions as func
import matplotlib as g_mpl
import matplotlib.pyplot as g_plt
import numpy as np
import io
import sys

import inspect

def in_unit_test():
    cli = sys.argv[0]
    return "unittest" in cli

# Yuk, something wonky on imports in azure functions
# Need different imports when running on unit tests
# BLEH!!
if in_unit_test():
    from shared_code import productivity
else:
    from ..shared_code import productivity

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        g_mpl.use('SVG')
        g_plt.ioff()
        g_plt.clf()
        p = productivity.render(g_plt)
        buf = io.BytesIO()
        p.savefig(buf, format='svg',bbox_inches="tight")
        buf.seek(0)
        return func.HttpResponse(buf.read(), mimetype='image/svg+xml')
    else:
        return func.HttpResponse(
             "Please pass a name on the query string or in the request body",
             status_code=400
        )
    return




def render_entr(plt):
    plt.xkcd()
    start_year = 2002
    end_year = 2018
    interest_shift_year = 2014

    years = np.linspace(start_year, end_year)
    interest_entrepener = 2 + 98.0 / (1 + np.exp(0.6 * (interest_shift_year - years)))
    interest_technologist = np.maximum(
        (100 - interest_entrepener), 50 + 10 * (np.sin(50 * years))
    )
    interest_entrepener = np.minimum(interest_entrepener, 70 + 10 * (np.sin(40 * years)))

    plt.plot(years, interest_entrepener, "-b", label="Entrepreneur")
    plt.plot(years, interest_technologist, "-r", label="Technologist")
    plt.ylabel("Identity")
    plt.xlabel("Year")

    plt.xlim(start_year, end_year)
    plt.legend(loc="best")
    return plt

