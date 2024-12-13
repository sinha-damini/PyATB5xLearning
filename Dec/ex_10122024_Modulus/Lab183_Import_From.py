from browserPackage.CloseBrowser import stop_browser
from browserPackage.OpenBrowser import start_browser


def test_Case():
    start_browser()
    print("Hello Running TC")
    stop_browser()
    print("Hello Closing TC")


test_Case()
