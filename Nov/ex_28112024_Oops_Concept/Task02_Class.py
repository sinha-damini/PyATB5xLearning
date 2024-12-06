# Create a Class Name API - RestfulBooker
# name, list_of_api , links {}
# print_apis, print_set

class RestfulBooker():
    name = None
    list_of_api = []
    se_of_links = {}

    def __init__(self, name, list_of_api, set_of_links):
        self.name = name
        self.list_of_api = list_of_api
        self.set_of_links = set_of_links

    def apis(self):
        print(f"List of APIs is {self.list_of_api}")

    def links(self):
        print(f"Set of Links is {self.set_of_links}")

API1 = RestfulBooker("API1", ['List1', 'List2', 'List3'], {"www.postmancollection1.com", "www.postmancollection2.com"})
API1.apis()
API1.links()

