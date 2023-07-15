from flask import request, session, redirect, url_for, render_template, flash

from . models import Models
from . forms import AddReaderForm, SignUpForm, SignInForm
from flask import json, jsonify
from src import app
import io
import numpy as np

models = Models()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/courses')
def show_courses():
    try:
        if session['user_available']:
            courses = models.getCourses()
            return render_template('courses.html', courses=courses)
        flash('User is not Authenticated')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))


@app.route('/add', methods=['GET', 'POST'])
def addCourse():
    try:
        if session['user_available']:
            reader = AddReaderForm(request.form)
            if request.method == 'POST':
                models.addCourse({"course_name": reader.course_name.data, "learning_hours": reader.learning_hours.data,
                "rating": reader.rating.data, "course_type": reader.course_type.data,"price": reader.price.data, "subject": reader.subject.data})
                return redirect(url_for('show_courses'))
            return render_template('add.html', reader=reader)
    except Exception as e:
        flash(str(e))
    flash('User is not Authenticated')
    return redirect(url_for('index'))


@app.route('/delete/<course_id>', methods=('GET', 'POST'))
def delete_course(course_id):
    try:
        models.deleteCourse({"course_id": course_id})
        return redirect(url_for('show_courses'))
    except Exception as e:
        flash(str("\n Sorry, cannot delete an assigned course!"))
        return redirect(url_for('show_courses'))


@app.route('/update/<course_id>', methods=('GET', 'POST'))
def update_course(course_id):
    try:
        br = models.getCourse({"course_id": course_id})
        reader = AddReaderForm(request.form, obj=br)
        if request.method == 'POST':
            models.updateCourse({"course_name": reader.course_name.data, "learning_hours": reader.learning_hours.data,
                "rating": reader.rating.data, "course_type": reader.course_type.data,"price": reader.price.data, "subject": reader.subject.data, "course_id": course_id})
            return redirect(url_for('show_courses'))
        return render_template('update.html', reader=reader)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    try:
        signupform = SignUpForm(request.form)
        if request.method == 'POST':
            models.addAdmin({"user_id": signupform.user_id.data, "password": signupform.password.data})
            return redirect(url_for('signin'))
        return render_template('signup.html', signupform=signupform)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    try:
        signinform = SignInForm(request.form)
        if request.method == 'POST':
            user_id = signinform.user_id.data
            log = models.getAdmin(user_id)
            if log.password == signinform.password.data:
                session['current_user'] = user_id
                session['user_available'] = True
                return redirect(url_for('show_courses'))
            else:
                flash('Cannot sign in')
        return render_template('signin.html', signinform=signinform)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/about_user')
def about_user():
    try:
        if session['user_available']:
            user = models.getProfessorByEmail(session['current_user'])
            return render_template('about_user.html', user=user)
        flash('You are not a Authenticated User')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))

@app.route('/course_dashboard')
def course_dashboard():
    try:
        if session['user_available']:
            labels, values = models.getCourseBySubject()
            print(labels)
            print(values)
            labels = json.htmlsafe_dumps(labels)
            
            typeLabels, typeValues = models.getCourseByType()
            print(typeLabels)
            print(typeValues)
            typeLabels = json.htmlsafe_dumps(typeLabels)
            

            course_count = models.getActiveCourseCount()
            print(course_count)

            student_count = models.getActiveLearner()
            print(student_count)

            instructor_count = models.getActiveInstructors()
            print(instructor_count)
           
            return render_template('course_dashboard.html', labels = labels,values=values, typeLabels = typeLabels,typeValues=typeValues,
            course_count=course_count,student_count=student_count,instructor_count=instructor_count)

        flash('You are not a Authenticated User')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))

@app.route('/enrolled_courses')
def enrolled_courses():
    try:
        if session['user_available']:
            courses = models.getEnrolledCourses()
            return render_template('enrolled_courses.html', courses=courses)
        flash('User is not Authenticated')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
@app.route('/enrolled_courses_dashboard')
def enrolled_courses_dashboard():
    try:
        if session['user_available']:
            labels, values = models.getEnrolledCourseBySubject()
            print(labels)
            print(values)
            labels = json.htmlsafe_dumps(labels)
            
            course_labels, course_values = models.getPieChart()
            print(course_labels)
            print(course_values)
            course_labels = json.htmlsafe_dumps(course_labels)

            df = models.getPriceForEnrolledCourse()
            df.Business = df.Business.astype(int)
            df.Finance = df.Finance.astype(int)
            df.Technology = df.Technology.astype(int)
            df.Mathematics = df.Mathematics.astype(int)
            df.year = df.year.astype(int)
            
            f1 = df['Business'].values.tolist()
            f2 = df['Finance'].values.tolist()
            f3 = df['Technology'].values.tolist()
            f4 = df['Mathematics'].values.tolist()
            year= df['year'].values.tolist()


            df_count = models.getNumbersForEachYear()
            
            student_count = df_count['student_count'].values.tolist()
            print(student_count)

            df_courses = models.getPopularCourse()
            df_courses.student_count = df_courses.student_count.astype(int)
            course_student_count = df_courses['student_count'].values.tolist()
            course_names = df_courses['course_name'].values.tolist()
            course_names = json.htmlsafe_dumps(course_names)

            df_rankings = models.getInstructorRanking()
            df_rankings.ranking = df_rankings.ranking.astype(int)
            ranking = df_rankings['ranking'].values.tolist()
            instructor_name = df_rankings['instructor_name'].values.tolist()
            instructor_name = json.htmlsafe_dumps(instructor_name)
            df_rankings.registrations = df_rankings.registrations.astype(int)
            registrations = df_rankings['registrations'].values.tolist()

            

            return render_template('enrolled_courses_dashboard.html', 
            labels = labels,values=values, course_labels = course_labels,
            course_values=course_values,f1=f1,f2=f2, f3=f3, f4=f4, year = year,student_count=student_count,
            course_student_count=course_student_count,course_names=course_names,ranking=ranking,instructor_name=instructor_name,registrations=registrations)
        flash('You are not a Authenticated User')
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    try:
        session.clear()
        session['user_available'] = False
        return redirect(url_for('index'))
    except Exception as e:
        flash(str(e))
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
