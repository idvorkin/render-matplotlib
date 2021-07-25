import unittest
import sys
import azure.functions as func
from shared_code import productivity
from shared_code import who_works_on_what
from shared_code import career_convo
import Render
import Debug
import matplotlib as g_mpl
import matplotlib.pyplot as g_plt
import io


def renderToFile(func):
    g_mpl.use("SVG")
    g_plt.ioff()
    g_plt.clf()
    p = func(g_plt)
    buf = io.BytesIO()
    p.savefig(buf, format="svg", bbox_inches="tight")
    buf.seek(0)


def http_call(funcToCall, name):
    # Construct a mock HTTP request.
    req = func.HttpRequest(
        method="GET", body=None, url="/api/HttpTrigger", params={"name": name}
    )

    # Call the function.
    return funcToCall(req)


class TestProductivity(unittest.TestCase):
    def test_no_crash(self):
        renderToFile(productivity.render)
        self.assertTrue(True)

    def test_no_500(self):
        resp = http_call(Render.main, "productivity")
        self.assertEqual(resp.status_code, 200)

class TestCareerConvo(unittest.TestCase):
    def test_no_crash(self):
        renderToFile(career_convo.render)
        self.assertTrue(True)

    def test_no_500(self):
        resp = http_call(Render.main, "career-convo")
        self.assertEqual(resp.status_code, 200)

class TestWhoWorksOnWhat(unittest.TestCase):
    def test_no_crash(self):
        renderToFile(who_works_on_what.render)
        self.assertTrue(True)

    def test_no_500(self):
        resp = http_call(Render.main, "what-to-work-on")
        self.assertEqual(resp.status_code, 200)


class TestCrashBadHandler(unittest.TestCase):
    def test_nice_image_even_bad_entry(self):
        resp = http_call(Render.main, "not-defined")
        self.assertEqual(resp.status_code, 200)


class TestDebugPage(unittest.TestCase):
    def test_not_fail(self):
        resp = http_call(Debug.main, "not-defined")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.mimetype, "text/html")
