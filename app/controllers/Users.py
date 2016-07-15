
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')

   
    def index(self):
        users = self.models['User'].get_users()
        print users
        return self.load_view('/users/index.html', users = users)

    def new(self):
        return self.load_view('/users/new.html')

    def create(self):
        info = {
            'name' : request.form['name'],
            'email' : request.form['email']
        }
        self.models['User'].create(info)
        return redirect('/')

    def show(self, id):
        user = self.models['User'].get_user_by_id(id)
        #user is a list; we just want the first element, hence user[0]
        return self.load_view('/users/show.html', user = user[0])

    def edit(self, id):
        user = self.models['User'].get_user_by_id(id)
        return self.load_view('/users/edit.html', user = user[0])

    def update(self, id):
        info = {
            'name' : request.form['name'],
            'email' : request.form['email']
        }
        self.models['User'].update(info, id)
        return redirect('/')

    def delete(self, id):
        user = self.models['User'].get_user_by_id(id)
        return self.load_view('/users/delete.html', user = user[0])

    def destroy(self, id):
        self.models['User'].destroy(id)
        return redirect('/')
