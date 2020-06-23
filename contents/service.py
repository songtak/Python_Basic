class Service:
    def __init__(self):
        self._contacts = []

        def add_contact(self, payload):
            self._contacts.append(payload)

        def get_contact(self, payload): #name
            for item in self._contacts:
                if payload == item.name:
                    return item

        def get_contacts(self):
            return self._contacts

        def del_contact(self, payload): #name
            for item in self._contacts:
                if payload == item.name:
                    return self._contacts.remove(item)