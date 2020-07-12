import unittest
import sys

import azure.functions as func
print ("line 4")
from shared_code import productivity
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


class TestProductivity(unittest.TestCase):
    def test_no_crash(self):
        renderToFile(productivity.render)
        self.assertTrue(True)


class ZestFunction(unittest.TestCase):
    def ignore_not_read_yet_my_function(self):
        # Construct a mock HTTP request.
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/HttpTrigger',
            params={'name': 'Test'})

        # Call the function.
        # resp = Render.main(req)

        # Check the output.
        # self.assertEqual( resp.get_body(), b'Hello Test',)
