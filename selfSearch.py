#Move to Front
class SelfOrganizingList:
    def __init__(self):
        self.items = []

    def search(self, value):
        if value in self.items:
            self.items.remove(value)
            self.items.insert(0, value)
            return True
        return False
    
    def insert(self, value):
        if value not in self.items:
            self.items.insert(0, value)

sol = SelfOrganizingList()
sol.insert(10)
sol.insert(20)
sol.insert(30)
print(sol.search(10))
print(sol.items)