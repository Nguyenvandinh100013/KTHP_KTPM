import os, sys, shutil, HtmlTestRunner

web_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(web_root)

report_dir = os.path.join(web_root, "reports")
if os.path.exists(report_dir):
    shutil.rmtree(report_dir)
os.makedirs(report_dir, exist_ok=True)

def run_tests():
    runner = HtmlTestRunner.HTMLTestRunner(output=report_dir)
    return runner
