class User:
    """
    class that generates new instances of user
    """

    user_list = [] #empty contact list

    def __init__(self, u_name,l_name, password):
        
        self.u_name = u_name
        self.l_name = l_name
        self.password = password
    
    #save contact
    def save_user(self):
        '''
        save_user method saves objects into user_list
        '''
        
        User.user_list.append(self)