import unittest
import sys
import azure.functions as func
from shared_code import productivity
import Render
import matplotlib as g_mpl
import matplotlib.pyplot as g_plt
import io

def renderToFile(func):
    g_mpl.use('SVG')
    g_plt.ioff()
    g_plt.clf()
    p = func(g_plt)
    buf = io.BytesIO()
    p.savefig(buf, format='svg',bbox_inches="tight")
    buf.seek(0)

def http_call(funcToCall,name):
    # Construct a mock HTTP request.
    req = func.HttpRequest(
        method='GET',
        body=None,
        url='/api/HttpTrigger',
        params={'name': name})

    # Call the function.
    return funcToCall(req)



class TestProductivity(unittest.TestCase):
    def test_no_crash(self):
        renderToFile(productivity.render)
        self.assertTrue(True)

    def test_no_500(self):
        resp = http_call(Render.main,"prod")
        self.assertEqual(resp.status_code,200)

