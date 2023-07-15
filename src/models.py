from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os
import pandas as pd

class Models:
    def __init__(self):
        self.engine = create_engine(os.environ.get('DB_URL', 'postgresql://postgres:admin@localhost:5432/starapp'))

    def executeRawSql(self, statement, params={}):
        out = None
        with self.engine.connect() as con:
            out = con.execute(text(statement), params)
        return out

    def addAdmin(self, value):
        return self.executeRawSql("""INSERT INTO admin (user_id, password) VALUES(:user_id, :password);""", value)

    def getAdmin(self, user_id):
        values = self.executeRawSql("""SELECT * FROM admin WHERE user_id=:user_id;""", {"user_id": user_id}).mappings().all()
        if len(values) == 0:
            raise Exception("Admin {} does not exist".format(user_id))
        return values[0]

    def getCourses(self):
        return self.executeRawSql("SELECT * FROM course_details;").mappings().all()

    def addCourse(self, value):
        return self.executeRawSql("""INSERT INTO course_details(course_name, learning_hours, rating, course_type, price, subject)
	    VALUES(:course_name, :learning_hours, :rating, :course_type, :price, :subject);""", value)

    def deleteCourse(self, value):
        return self.executeRawSql("DELETE FROM course_details where course_id=:course_id;", value)

    def updateCourse(self, value):
        return self.executeRawSql("""UPDATE course_details SET course_name = :course_name, learning_hours = :learning_hours, 
        rating = :rating, course_type = :course_type, price = :price, subject = :subject WHERE course_id = :course_id;""", value)
    
    def getCourse(self, value):
        values = self.executeRawSql("""SELECT * FROM course_details WHERE course_id=:course_id;""", value).mappings().all()
        if len(values) == 0:
            raise Exception("Course has not been created")
        return values[0]

    def getCourseBySubject (self):
        data = self.executeRawSql("SELECT subject, count(course_id) as course_count FROM course_details GROUP BY subject ORDER BY subject;").mappings().all()
        dict = {result.subject: result.course_count for result in data}
        print(dict)
        labels = list(dict.keys())
        print(labels)
        values = list(dict.values())
        print(values)
        return labels, values
    
    def getCourseByType(self):
        data = self.executeRawSql("SELECT course_type, count(course_id) as course_count FROM course_details GROUP BY course_type ORDER BY course_type;").mappings().all()
        dict = {result.course_type: result.course_count for result in data}
        print(dict)
        labels = list(dict.keys())
        print(labels)
        values = list(dict.values())
        print(values)
        return labels, values

    def getEnrolledCourses(self):
        return self.executeRawSql("""SELECT s.s_email, c.course_name, i.i_email, c.price, d.year,c.subject,
        c.rating,c.course_type FROM course_registration_fact fact,student_dim s ,course_details c ,
        instructor_dim i ,date_dim d  WHERE fact.student_id = s.student_id AND 
        fact.course_id= c.course_id AND fact.instructor_id = i.instructor_id AND 
        fact.datekey = d.datekey ORDER BY d.year DESC;""").mappings().all()

    def getEnrolledCourseBySubject (self):
        data = self.executeRawSql("""select cd.subject, count(fact.registration_id) as course_count from 
        course_registration_fact fact , course_details cd where fact.course_id = cd.course_id 
        group by cd.subject order by cd.subject;""").mappings().all()
        dict = {result.subject: result.course_count for result in data}
        print(dict)
        labels = list(dict.keys())
        values = list(dict.values())
        return labels, values 

    def getPieChart (self):
        data = self.executeRawSql("""select s.s_type, count(fact.registration_id) as student_count from 
        course_registration_fact fact , student_dim s where fact.course_id = s.student_id 
        group by s.s_type order by s.s_type;""").mappings().all()
        dict = {result.s_type: result.student_count for result in data}
        labels = list(dict.keys())
        values = list(dict.values())
        return labels, values  

    def getPriceForEnrolledCourse (self):

        data = self.executeRawSql("""SELECT d.year,
            sum(fact.price) FILTER (WHERE cd.subject = 'Business') AS "Business",
            sum(fact.price) FILTER (WHERE cd.subject = 'Finance') AS "Finance",
            sum(fact.price) FILTER (WHERE cd.subject = 'Technology') AS "Technology",
            sum(fact.price) FILTER (WHERE cd.subject = 'Mathematics') AS "Mathematics"
            from course_registration_fact fact , course_details cd , date_dim d
            where fact.course_id = cd.course_id and fact.datekey = d.datekey
            group by d.year order by d.year;""").mappings().all()
        df = pd.DataFrame(data,columns=['year','Business','Finance','Technology','Mathematics'])
        return df

    def getNumbersForEachYear (self):

        data = self.executeRawSql("""select d.year, count(fact.registration_id) student_count from course_registration_fact fact, date_dim d
        where fact.datekey = d.datekey group by d.year order by d.year ;""").mappings().all()
        df = pd.DataFrame(data,columns=['year','student_count'])
        return df
    
    def getPopularCourse(self):
        data = self.executeRawSql("""select cd.course_name, count(fact.registration_id) student_count from 
        course_registration_fact fact, course_details cd 
        WHERE fact.course_id = cd.course_id group by cd.course_name order by student_count desc limit 10;""").mappings().all()
        df = pd.DataFrame(data,columns=['course_name','student_count'])
        return df
    
    def getActiveCourseCount(self):
        data = self.executeRawSql("SELECT COUNT(course_id) course_count FROM course_details;").mappings().all()
        print(data[0].course_count)
        return data[0].course_count

    def getActiveLearner(self):
        data = self.executeRawSql("SELECT COUNT(registration_id) student_count FROM course_registration_fact;").mappings().all()
        print(data[0].student_count)
        return data[0].student_count
    
    def getActiveInstructors(self):
        data = self.executeRawSql("SELECT COUNT(distinct instructor_id) instructor_count FROM course_registration_fact;").mappings().all()
        print(data[0].instructor_count)
        return data[0].instructor_count

    def getStudentCountries(self):
        data = self.executeRawSql("SELECT DISTINCT s.s_country as country FROM  course_registration_fact fact, student_dim s WHERE fact.student_id = s.student_id;;").mappings().all()
        print(data[0].country)
        return data[0].country

    def getInstructorRanking(self):
        data = self.executeRawSql("""SELECT RANK() OVER(ORDER BY COUNT(*) DESC) AS ranking,
        TRIM(CONCAT(i.i_first_name, ' ', i.i_last_name)) AS instructor_name,
        COUNT(*) AS registrations FROM  course_registration_fact fact,instructor_dim i ,course_details cd 
        WHERE fact.instructor_id=i.instructor_id AND fact.course_id = cd.course_id GROUP BY instructor_name limit 10;""").mappings().all() 
        
        df = pd.DataFrame(data,columns=['ranking','instructor_name','registrations'])
        return df

