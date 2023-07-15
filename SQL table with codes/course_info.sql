DROP TABLE IF EXISTS course_info;

create table course_info (
	course_id VARCHAR(50) PRIMARY KEY,
	course_name VARCHAR(16) UNIQUE NOT NULL,
	c_learning_hours INT NOT NULL,
	c_fees VARCHAR(4) NOT NULL,
	c_price VARCHAR(4) NOT NULL,
	c_rating INT NOT NULL
);

insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('444-45-8023', 'python_1', 116, 'Free', 250, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('475-10-8123', 'python_2', 96, 'Paid', 500, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('362-36-0289', 'python_3', 117, 'Paid', 750, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('345-89-6320', 'sql_1', 104, 'Free', 500, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('228-16-2872', 'sql_2', 72, 'Paid', 1000, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('169-28-9642', 'sql_3', 43, 'Paid', 1500, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('282-38-8268', 'c_1', 90, 'Free', 750, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('861-61-3888', 'c_2', 55, 'Paid', 1500, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('600-89-9460', 'c_3', 85, 'Paid', 2000, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('475-65-6804', 'c++_1', 28, 'Free', 250, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('257-43-5807', 'c++_2', 48, 'Paid', 500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('316-68-9894', 'c++_3', 80, 'Paid', 750, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('564-03-1405', 'java_1', 84, 'Free', 500, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('889-10-3454', 'java_2', 44, 'Paid', 1000, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('662-42-2778', 'jave_3', 55, 'Paid', 1500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('529-58-0277', 'java-script_1', 24, 'Free', 750, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('781-99-9781', 'java-script_2', 107, 'Paid', 1500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('677-39-0669', 'java-script_3', 51, 'Paid', 2000, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('329-29-0979', 'maths_1', 82, 'Free', 250, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('410-41-8069', 'maths_2', 105, 'Paid', 500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('438-72-3666', 'maths_3', 65, 'Paid', 750, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('122-27-7904', 'physics_1', 31, 'Free', 500, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('251-84-3373', 'physics_2', 63, 'Paid', 1000, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('624-46-6082', 'physics_3', 83, 'Paid', 1500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('547-97-6030', 'chemistry_1', 55, 'Free', 750, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('352-57-4270', 'chemistry_2', 117, 'Paid', 1500, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('677-90-8594', 'chemistry_3', 87, 'Paid', 2000, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('647-78-7261', 'english_1', 48, 'Free', 250, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('836-23-8320', 'english_2', 45, 'Paid', 500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('656-45-7875', 'english_3', 115, 'Paid', 750, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('605-27-6215', 'japanese_1', 61, 'Free', 500, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('582-18-0844', 'japanese__2', 118, 'Paid', 1000, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('745-75-3124', 'japanese__3', 66, 'Paid', 1500, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('498-35-6327', 'hindi_1', 92, 'Free', 750, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('656-15-9158', 'hindi_2', 82, 'Paid', 1500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('879-95-3481', 'hindi_3', 118, 'Paid', 2000, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('531-13-6430', 'mandrin_1', 79, 'Free', 250, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('664-93-1123', 'mandrin_2', 79, 'Paid', 500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('570-95-6221', 'mandrin_3', 27, 'Paid', 750, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('398-24-0208', 'social-science_1', 53, 'Free', 500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('552-25-7855', 'social-science_2', 67, 'Paid', 1000, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('552-75-7727', 'social-science_3', 69, 'Paid', 1500, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('447-85-7277', 'excel_1', 120, 'Free', 750, 4);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('662-32-3847', 'excel_2', 109, 'Paid', 1500, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('330-39-2085', 'excel_3', 39, 'Paid', 2000, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('476-92-9710', 'pgadmin_1', 66, 'Free', 250, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('859-87-4183', 'pgadmin_2', 67, 'Paid', 500, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('540-50-3812', 'pgadmin_3', 28, 'Paid', 750, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('647-09-7282', 'astronomy_1', 107, 'Free', 500, 3);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('421-78-8796', 'astronomy_2', 48, 'Paid', 1000, 5);
insert into course_info (course_id, course_name, c_learning_hours, c_fees, c_price, c_rating) values ('437-85-2486', 'astronomy_3', 69, 'Paid', 1500, 4);
