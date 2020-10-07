class Users_list():
    """This class create diferents list of id users 
       to use on filter bar """
    def __init__(self):
        self.users = []
        self.users1 = []
        self.users2 = []

    def bar_filter(self):
        """This funcion set id user on list users based
           on if there are a filter by work area or only filter
           by location """
        if self.users1 and self.users2:
            for user1 in self.users1:
                for user2 in self.users2:
                    if user1 == user2:
                        self.users.append(user1)
                        self.users1.pop(user1)
            self.users.extend(self.users1)
        elif self.users2:
            self.users = self.users2
        elif self.users1:
            self.users = self.users1


