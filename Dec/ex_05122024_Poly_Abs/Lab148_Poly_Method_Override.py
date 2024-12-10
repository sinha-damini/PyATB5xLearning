class OldBrowser:

    def start_browser(self):
        print("Starting the IE Browser.")

    def close_browser(self):
        print("Closing the IE Browser.")

class Chrome(OldBrowser):

    def start_browser(self):
        # super().start_browser() # Parent Start browser also.
        print("Better Chrome browser is starting...")

    def close_browser(self):
        print("Better Chrome browser is Stopping...")

    pass

obj_ref = Chrome()
obj_ref.start_browser()
obj_ref.close_browser()