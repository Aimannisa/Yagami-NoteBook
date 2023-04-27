


class Student:
    def __init__(self,name,age,email,password,notebook):
        self.__name=name
        self.__age=age
        self.__email=email
        self.__pass=password
        self.__notebook=notebook
    
    @property
    def name(self):
        return self.__name
    
        
    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age=age
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        self.__email=email

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        self.__password=password


    @property
    def notebook(self):
        return self.__notebook
    
    @notebook.setter
    def notebook(self,notebook):
        self.__notebook=notebook