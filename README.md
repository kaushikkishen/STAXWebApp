#Web application with PostgreSQL and Flask
[Python] Collaborated with a team at NUS to develop an end-to-end analytics application using Flask and PostgreSQL. The project involved synthesizing data and gaining valuable insights. Completed as part of an in-class project. 

## Flask Sandbox (STAXApp)

Web application with PostgreSQL and Flask that allows asking analytics queries. The user should be able to select, parameterise, or interactively design her input in Web forms.
A sandbox application with Flask, SQLAlchemy and PostgreSQL


##Project Info

STAX Business Intelligence System (SBIS) is a key tool for the STAX, a leading Online Education Provider to support and enhance their educational businesses while improving the efficiency of learning and teaching processes combined. The Data Warehouse (DW) system helps to monitor the data from different Database (DB) and combines all together under one schema by using OLAP which in turn helps the Analytics board to make the right decision depending on the circumstances faced. Educational Administration Analytics Platform combines the critical information regarding the Students, Instructors, 
Courses with time into one Data Warehouse. The output of SBIS mainly consists of the analytical reports which are used to get insights and make business decisions efficiently to meet the Key Performance Indices (KPI’s). The proposed Data Warehouse system is implemented based on the simulated databases with data created using Mockaroo for the last 6 years. 

### Usage

- Install Git Bash
- Open Git Bash, go to the directory containing this project, and run `./deploy.sh`
- A directory called `.venv` will be created. If there is any error, delete this folder and run `./deploy.sh` again

### Requirements

- Python 3
- Flask
- Flask-SQLAlchemy
- flask-WTF

##Running the project locally
- In models.py:
	- The local database URL currently is `postgresql://hieu:hieu@localhost:5432/bt5110`
	- Replace this with your URL: `postgresql://<your db username>:<your db 
password>@localhost:5432/<your db name>`
- To run the project locally
	- MacOS/Linux: `chmod a+x deploy.sh; ./deploy.sh`
	- Windows:
		- python -m venv .venv
		- .venv/Scripts/activate
		- python -m pip install
		- pip install -r requirements
		- python app.py

##Collaborators
Sushmita Sinha - https://www.linkedin.com/in/sushmitasinha17/overlay/contact-info/
Nitesh Reddy Lodugu - https://www.linkedin.com/in/nithesh-reddy-lodugu-33a656b1/
Kaushik Asok - https://www.linkedin.com/in/kaushik-asok-002b19169/