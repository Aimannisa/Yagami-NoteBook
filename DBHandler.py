import pymysql
from student import Student
from note import Note

class DBHandler:
    def __init__(self, host, user, password, dataBase, port):
        self.host = host
        self.password = password
        self.username = user
        self.dataBase = dataBase
        self.port = port

    def register_student(self, student):
        connection = None
        cursor = None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        cursor = connection.cursor()
        try:
            if int(student.age)<=0:
                return False
            if student.name=='Light Yagami':
                student.notebook='Death Note'

            Xemail=student.email.split('@')
            if Xemail[1]!='pucit.edu.pk':
                return False
            # if student.email.split('@')!='pucit.edu.pk':
            #     return False
            sql = "Insert into student (`name`,`age`,`email`,`password`,`notebook`) VALUES(%s,%s,%s,%s,%s)"
            args = (student.name, student.age,
                    student.email, student.password,student.notebook)
            cursor.execute(sql, args)
            connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
            connection.close()


    def verify_student(self,email,password):
        connection=None
        cursor=None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        
        cursor = connection.cursor()
        try:
            sql = "Select * from student where email=%s AND password=%s"
            args = (email,password)
            cursor.execute(sql, args)
            result = cursor.fetchall()
            print('in verify',result)
            if result:
                print(result)
                return result
            return False
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
            connection.close()


    def createNote(self,note):
        connection = None
        cursor = None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        cursor = connection.cursor()
        try:
            # if student.age<=0:
            #     return False
            # if student.name=='Light Yagami':
            #     student.notebook='Death Note'

            # email=student.email.split('@')
            # if email[1]!='pucit.edu.pk':
            #     return False
            # if student.email.split('@')!='pucit.edu.pk':
            #     return False
            # text=note.text
            # title=note.title
            # studen_id=note.student_id
            # date=note.date


            sql = "Insert into note (`title`,`text`,`student`,`date`) VALUES(%s,%s,%s,%s)"
            args = (note.title, note.text,
                    note.student_id, note.date)
            cursor.execute(sql, args)
            connection.commit()
            return True
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
            connection.close()


    def showAllNotes(self,id):
        connection=None
        cursor=None
        connection = pymysql.connect(
            host=self.host, port=self.port, user=self.username, password=self.password, database=self.dataBase)
        
        cursor = connection.cursor()
        try:

            sql = "Select * from note where student=%s"
            args = (id)
            cursor.execute(sql, args)
            result = cursor.fetchall()
            if result:
                print('in show',result)
                return result
            return False
        except Exception as e:
            print(str(e))
            return False
        finally:
            cursor.close()
            connection.close()

    # def SearchNotesByText(self, text):
    