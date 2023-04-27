
class Note:
    def __init__(self,title,text,student_id,date):
        self.__title=title
        self.__text=text
        self.__student_id=student_id
        self.__date=date
    
    @property
    def title(self):
        return self.__title
    
        
    @title.setter
    def username(self,title):
        self.__title=title

    @property
    def text(self):
        return self.__text
    
    @text.setter
    def text(self,text):
        self.__text=text
    
    @property
    def date(self):
        return self.__date
    
    @date.setter
    def date(self,date):
        self.__date=date

    @property
    def student_id(self):
        return self.__student_id
    
    @student_id.setter
    def student_id(self,student_id):
        self.__student_id=student_id