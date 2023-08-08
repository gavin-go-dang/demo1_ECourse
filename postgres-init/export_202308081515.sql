INSERT INTO public.auth_group ("name") VALUES
	 ('teacher');
INSERT INTO public.auth_group_permissions (group_id,permission_id) VALUES
	 (1,17),
	 (1,21),
	 (1,22),
	 (1,23),
	 (1,24),
	 (1,29),
	 (1,30),
	 (1,31),
	 (1,32),
	 (1,33);
INSERT INTO public.auth_group_permissions (group_id,permission_id) VALUES
	 (1,34),
	 (1,35),
	 (1,36),
	 (1,41),
	 (1,42),
	 (1,43),
	 (1,44),
	 (1,48),
	 (1,52),
	 (1,20);
INSERT INTO public.auth_permission ("name",content_type_id,codename) VALUES
	 ('Can add permission',1,'add_permission'),
	 ('Can change permission',1,'change_permission'),
	 ('Can delete permission',1,'delete_permission'),
	 ('Can view permission',1,'view_permission'),
	 ('Can add group',2,'add_group'),
	 ('Can change group',2,'change_group'),
	 ('Can delete group',2,'delete_group'),
	 ('Can view group',2,'view_group'),
	 ('Can add content type',3,'add_contenttype'),
	 ('Can change content type',3,'change_contenttype');
INSERT INTO public.auth_permission ("name",content_type_id,codename) VALUES
	 ('Can delete content type',3,'delete_contenttype'),
	 ('Can view content type',3,'view_contenttype'),
	 ('Can add user',4,'add_user'),
	 ('Can change user',4,'change_user'),
	 ('Can delete user',4,'delete_user'),
	 ('Can view user',4,'view_user'),
	 ('Can add topic',5,'add_topic'),
	 ('Can change topic',5,'change_topic'),
	 ('Can delete topic',5,'delete_topic'),
	 ('Can view topic',5,'view_topic');
INSERT INTO public.auth_permission ("name",content_type_id,codename) VALUES
	 ('Can add course',6,'add_course'),
	 ('Can change course',6,'change_course'),
	 ('Can delete course',6,'delete_course'),
	 ('Can view course',6,'view_course'),
	 ('Can add certificate',7,'add_certificate'),
	 ('Can change certificate',7,'change_certificate'),
	 ('Can delete certificate',7,'delete_certificate'),
	 ('Can view certificate',7,'view_certificate'),
	 ('Can add exam',8,'add_exam'),
	 ('Can change exam',8,'change_exam');
INSERT INTO public.auth_permission ("name",content_type_id,codename) VALUES
	 ('Can delete exam',8,'delete_exam'),
	 ('Can view exam',8,'view_exam'),
	 ('Can add lesson',9,'add_lesson'),
	 ('Can change lesson',9,'change_lesson'),
	 ('Can delete lesson',9,'delete_lesson'),
	 ('Can view lesson',9,'view_lesson'),
	 ('Can add lesson learned',10,'add_lessonlearned'),
	 ('Can change lesson learned',10,'change_lessonlearned'),
	 ('Can delete lesson learned',10,'delete_lessonlearned'),
	 ('Can view lesson learned',10,'view_lessonlearned');
INSERT INTO public.auth_permission ("name",content_type_id,codename) VALUES
	 ('Can add question',11,'add_question'),
	 ('Can change question',11,'change_question'),
	 ('Can delete question',11,'delete_question'),
	 ('Can view question',11,'view_question'),
	 ('Can add register',12,'add_register'),
	 ('Can change register',12,'change_register'),
	 ('Can delete register',12,'delete_register'),
	 ('Can view register',12,'view_register'),
	 ('Can add result test',13,'add_resulttest'),
	 ('Can change result test',13,'change_resulttest');
INSERT INTO public.auth_permission ("name",content_type_id,codename) VALUES
	 ('Can delete result test',13,'delete_resulttest'),
	 ('Can view result test',13,'view_resulttest'),
	 ('Can add log entry',14,'add_logentry'),
	 ('Can change log entry',14,'change_logentry'),
	 ('Can delete log entry',14,'delete_logentry'),
	 ('Can view log entry',14,'view_logentry'),
	 ('Can add session',15,'add_session'),
	 ('Can change session',15,'change_session'),
	 ('Can delete session',15,'delete_session'),
	 ('Can view session',15,'view_session');
INSERT INTO public.auth_permission ("name",content_type_id,codename) VALUES
	 ('Can add group',16,'add_group'),
	 ('Can change group',16,'change_group'),
	 ('Can delete group',16,'delete_group'),
	 ('Can view group',16,'view_group'),
	 ('Can add push information',17,'add_pushinformation'),
	 ('Can change push information',17,'change_pushinformation'),
	 ('Can delete push information',17,'delete_pushinformation'),
	 ('Can view push information',17,'view_pushinformation'),
	 ('Can add subscription info',18,'add_subscriptioninfo'),
	 ('Can change subscription info',18,'change_subscriptioninfo');
INSERT INTO public.auth_permission ("name",content_type_id,codename) VALUES
	 ('Can delete subscription info',18,'delete_subscriptioninfo'),
	 ('Can view subscription info',18,'view_subscriptioninfo');
INSERT INTO public.authen_user ("password",last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined,created_at,updated_at,full_name,date_of_birth,"type",cover_img) VALUES
	 ('pbkdf2_sha256$600000$RzEfICiAE78RmO19dxPrmE$0TStRoDi0+5j3SfdAoj0CtfcV/kBHs0/7lC7hlsKHvU=','2023-08-02 17:25:23.185736+07',false,'teacher1','','','teacher1@gmail.com',true,true,'2023-07-28 14:15:42.783385+07','2023-07-28 14:15:43.011851+07','2023-07-28 15:07:18.062479+07','Tyler Cooper',NULL,'teacher','cover_img/An_oil_pastel_drawing_of_an_annoyed_cat_in_a_spaceship.webp'),
	 ('pbkdf2_sha256$600000$rfSv0BSE6mp05bTQx0P2Om$odTzx3H6zQByWeYNDHvoFQCy7rOw9sm3zx+PuLz+No0=','2023-08-02 17:26:52.9135+07',true,'gavin','','','gavin.dang.goldenowl@gmail.com',true,true,'2023-07-28 14:09:22.413074+07','2023-07-28 14:09:22.695096+07','2023-08-02 09:11:46.949843+07','Gavin Dang',NULL,'',''),
	 ('pbkdf2_sha256$600000$1UWwrcu8jTlTnfFaNOzaIZ$KZKfFsV5Aakqo2vM32BzWz/5wHXPwPiBoYybZGH5Lbc=','2023-08-02 17:27:28.350238+07',false,'teacher2','','','teacher2@gmail.com',true,true,'2023-07-28 14:15:59.424273+07','2023-07-28 14:15:59.649945+07','2023-08-02 14:22:49.800446+07','Madison Sullivans',NULL,'teacher','cover_img/avtman.png'),
	 ('pbkdf2_sha256$600000$J9vsrtCscqyc093tXCRxUZ$pjO7psXlZ7OvqUQSbqSQUyUbK9f4vYXLhXjc8VgxtUo=','2023-08-02 17:30:04.95668+07',false,'teacher3','','','teacher3@gmail.com',true,true,'2023-07-28 14:16:15.91771+07','2023-07-28 14:16:16.156563+07','2023-07-28 15:06:52.042246+07','Nathan Lee',NULL,'teacher','cover_img/flosquare.jpeg'),
	 ('pbkdf2_sha256$600000$Jy36DKgJX4XTviy9P0o3Zo$egowStnboefrhm3B+/qXo5GV200jkJYnpwuT33tQ87w=','2023-08-02 17:35:47.512799+07',false,'student1','','','student1@email.com',false,true,'2023-07-28 14:11:10.188588+07','2023-07-28 14:11:10.454164+07','2023-08-03 11:25:16.143779+07','Samantha David','2023-07-05','student','cover_img/DALLE_2023-07-28_14.27.37_-_a_cunputer_is_running_van_gogh_style.png'),
	 ('pbkdf2_sha256$600000$qmFnhy7WLpgsve9v7OvraV$yDhJvNdCtilvPU9eRyyX6CNmI5+OlQoRB9FJ+2CuItc=','2023-08-02 11:03:03.036636+07',false,'student7','','','student7@gmail.com',false,true,'2023-08-02 10:49:58.396397+07','2023-08-02 10:49:58.664985+07','2023-08-02 10:50:16.033978+07','Harper Lee',NULL,'student',''),
	 ('pbkdf2_sha256$600000$9hVzHy7lEvCfiI4EEJ8jDu$1mDI5LQz6RkAKunWvOSCgJ3WwJjDYlAzRU4xwBkGwVg=','2023-08-02 14:23:01.093365+07',false,'student2','','','student2@gmail.com',false,true,'2023-07-28 14:14:27.825663+07','2023-07-28 14:14:28.075984+07','2023-08-02 14:23:10.967767+07','Adam Collins',NULL,'student','cover_img/robotrun.png'),
	 ('pbkdf2_sha256$600000$cFkR0xNaYy9yTZNa6VYuak$Ze2mjVEi2QFWjtb+7eWquXYbYF8wd7SfZPx3PJ5Y4AY=','2023-08-02 14:24:25.330849+07',false,'student3','','','student3@gmail.com',false,true,'2023-07-28 14:14:52.537805+07','2023-07-28 14:14:52.766546+07','2023-08-02 14:24:38.076583+07','Julia Martinez',NULL,'student','cover_img/A_photo_of_a_white_fur_monster_standing_in_a_purple_room.webp');
INSERT INTO public.authen_user_groups (user_id,group_id) VALUES
	 (3,1),
	 (4,1),
	 (6,1),
	 (7,1),
	 (8,1),
	 (9,1);
INSERT INTO public.course_manager_certificate (pdf_url,course_id,student_id,score,created_at,updated_at) VALUES
	 (NULL,1,2,10.0,'2023-08-01 12:23:48.406423+07','2023-08-01 12:23:48.406443+07'),
	 (NULL,3,2,7.5,'2023-08-02 10:20:38.54447+07','2023-08-02 10:20:38.544506+07');
INSERT INTO public.course_manager_course (created_at,updated_at,name_course,description,register,time_to_learn_ets,cover_img,"level",teacher_id,topic_id) VALUES
	 ('2023-07-28 14:43:24.208489+07','2023-07-28 14:43:24.208508+07','Adobe Lightroom','Adobe Lightroom is a piece of image organization and image processing software developed by Adobe Inc. as part of the Creative Cloud subscription family. It is supported on Windows, macOS, iOS, Android, and tvOS.',0,26,'course_img/An_oil_pastel_drawing_of_an_annoyed_cat_in_a_spaceship.webp','basic',7,3),
	 ('2023-07-28 14:44:03.082056+07','2023-07-28 14:44:03.082088+07','Adobe Premiere','Adobe Premiere Pro is a timeline-based and non-linear video editing software application developed by Adobe Inc. and published as part of the Adobe Creative Cloud licensing program. First launched in 2003, Adobe Premiere Pro is a successor of Adobe Premiere.',0,65,'','advanced',7,3),
	 ('2023-07-28 14:28:04.725355+07','2023-07-28 15:14:07.006332+07','Machine Learning','Machine learning is a branch of artificial intelligence that focuses on developing algorithms and statistical models that enable machines to learn and improve their performance on a specific task over time.',2,60,'course_img/DALLE_2023-07-28_14.27.37_-_a_cunputer_is_running_van_gogh_style.png','basic',6,4),
	 ('2023-07-28 14:31:25.622665+07','2023-07-30 20:37:22.477002+07','English Grammar','English grammar is the set of structural rules of the English language.',4,25,'course_img/DALLE_2023-07-28_14.31.10_-_3_people_are_talking_each_other_3D_.png','basic',6,9),
	 ('2023-07-28 14:28:59.255901+07','2023-08-02 09:16:57.520972+07','Web Front-end','the front end is a combination of two different elements: the graphic design (the look) and the user interface (the feel).',7,40,'course_img/A_computer_from_the_90s_in_the_style_of_vaporwave.webp','basic',6,1),
	 ('2023-07-28 15:11:46.579066+07','2023-08-02 17:31:47.554352+07','Physics in reality','Sub-disciplines include applied physics, astrophysics, biophysics, condensed matter physics, high-energy physics, nuclear physics, optics, and particle physics. Resources for physics are primarily available via the Web and some of the key web resources can be found in this guide',2,5,'course_img/llightning.png','advanced',8,5),
	 ('2023-07-28 14:42:34.270741+07','2023-08-01 16:03:32.222677+07','Photoshop CS5','Adobe Photoshop is a raster graphics editor developed and published by Adobe Inc. for Windows and macOS. It was originally created in 1987 by Thomas and John Knoll.',5,50,'course_img/ptspts.png','basic',7,3);
INSERT INTO public.course_manager_exam (created_at,updated_at,name_exam,description,course_id) VALUES
	 ('2023-07-28 14:44:47.99574+07','2023-07-28 14:44:47.99576+07','Final Test','Gradution Exam',1),
	 ('2023-07-28 14:49:46.957708+07','2023-07-28 14:49:46.957748+07','Middle Test','Middle test',3),
	 ('2023-07-30 16:36:45.269091+07','2023-07-30 16:36:45.269134+07','Final test','Final test',3);
INSERT INTO public.course_manager_lesson (created_at,updated_at,name_lesson,video,description,view_time,"index",course_id) VALUES
	 ('2023-07-28 14:32:38.350501+07','2023-07-28 14:32:38.35052+07','Statistics and Probability','video1.mp4','Probability deals with predicting the likelihood of future events, while statistics involves the analysis of the frequency of past events. Probability is primarily a theoretical branch of mathematics, which studies the consequences of mathematical definitions.',20,1,1),
	 ('2023-07-28 14:35:05.969911+07','2023-07-28 14:35:05.96993+07','Python basic','earth.mp4','Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation',10,2,1),
	 ('2023-07-28 14:37:32.528318+07','2023-07-28 14:37:32.528351+07','Introduce HTML','','HTML stands for Hyper Text Markup Language. HTML is the standard markup language for creating Web pages.',15,1,2),
	 ('2023-07-28 14:38:44.89119+07','2023-07-28 14:38:44.89124+07','CSS','css.mp4','Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML or XML.',15,2,2),
	 ('2023-07-28 14:39:54.110008+07','2023-07-28 14:39:54.110027+07','Java Script','jsj.mp4','JavaScript (JS) is a lightweight interpreted (or just-in-time compiled) programming language with first-class functions. While it is most well-known as the scripting language for Web pages, many non-browser environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat.',30,3,2),
	 ('2023-07-28 14:35:52.757019+07','2023-07-28 15:24:35.790857+07','NLP','LPLPN.mp4','Natural language processing (NLP) is a branch of artificial intelligence (AI) that enables computers to comprehend, generate, and manipulate human language. Natural language processing has the ability to interrogate the data with natural language text or voice.',15,2,1),
	 ('2023-07-30 16:41:12.955905+07','2023-08-02 17:26:16.020311+07','Noun','earth_jLcDkYz.mp4','What is Noun in English?',20,1,3),
	 ('2023-08-02 17:28:59.685268+07','2023-08-02 17:28:59.68534+07','Draw with Brush tool','earth_WFMkcuV.mp4','D',15,1,4),
	 ('2023-08-02 17:29:31.46676+07','2023-08-02 17:29:31.466785+07','Constrast','earth_Ugap4GA.mp4','D',15,1,5),
	 ('2023-08-02 17:29:56.363735+07','2023-08-02 17:29:56.363755+07','Role-A Role-B','earth_i5RlOdT.mp4','D',15,1,6);
INSERT INTO public.course_manager_lesson (created_at,updated_at,name_lesson,video,description,view_time,"index",course_id) VALUES
	 ('2023-08-02 17:30:41.134792+07','2023-08-02 17:30:41.134829+07','lighning','earth_At1kc0H.mp4','D',45,1,7);
INSERT INTO public.course_manager_lessonlearned (created_at,updated_at,lesson_id,student_id) VALUES
	 ('2023-08-02 16:47:58.239926+07','2023-08-02 16:47:58.239972+07',1,2),
	 ('2023-08-02 16:49:10.672996+07','2023-08-02 16:49:10.673018+07',2,2),
	 ('2023-08-02 16:52:27.433596+07','2023-08-02 16:52:27.43363+07',3,2);
INSERT INTO public.course_manager_question (question_text,choice_1,choice_2,choice_3,choice_4,answer,exam_id) VALUES
	 ('What is machine learning?','The selective acquisition of knowledge through the use of manual programs','The selective acquisition of knowledge through the use of computer programs','The autonomous acquisition of knowledge through the use of manual programs','The autonomous acquisition of knowledge through the use of computer programs','The autonomous acquisition of knowledge through the use of computer programs',1),
	 ('Machine Learning is a field of AI consisting of learning algorithms that ..............','At executing some task','Over time with experience','Improve their performance','All of the above','All of the above',1),
	 ('.............. is a widely used and effective machine learning algorithm based on the idea of baggin','Regression','Classification','Random Forest','Decision Tree','Random Forest',1),
	 ('What is the disadvantage of decision trees?','Factor analysis','Decision trees are robust to outliers','Decision trees are prone to be overfit','All of the above','Decision trees are prone to be overfit',1),
	 ('______raiding for camels was a significant part of Bedouin life has  been documented in Wilfed Thesi','That','Which','What','Where','That',2),
	 ('The little boy pleaded _____ not to leave him alone in the dark.','on his mother','his mother','with his mother','at his mother','with his mother',2),
	 ('That ___  a dog.','were','is','am','are','is',3);
INSERT INTO public.course_manager_register (created_at,course_id,student_id) VALUES
	 ('2023-07-28 15:14:06.975516+07',1,2),
	 ('2023-07-30 16:46:42.268667+07',3,1),
	 ('2023-07-30 20:37:22.440832+07',3,2),
	 ('2023-08-01 16:03:31.894089+07',4,2),
	 ('2023-08-01 16:14:29.195212+07',7,2),
	 ('2023-08-01 17:27:23.911352+07',2,2),
	 ('2023-08-02 09:16:13.712607+07',2,1),
	 ('2023-08-02 09:16:57.511817+07',2,1);
INSERT INTO public.course_manager_resulttest (created_at,mark,student_answer,number_of_test,pass_exam,exam_id,student_id) VALUES
	 ('2023-07-28 15:14:32.873599+07',10,'{"1": "The autonomous acquisition of knowledge through the use of computer programs", "2": "All of the above", "3": "Random Forest", "4": "Decision trees are prone to be overfit"}',1,true,1,2),
	 ('2023-07-30 16:46:59.714448+07',0,'{"5": "What", "6": "on his mother"}',1,false,2,1),
	 ('2023-07-30 16:47:12.750211+07',0,'{"5": "Which", "6": "at his mother"}',2,false,2,1),
	 ('2023-07-30 16:47:24.870786+07',0,'{"7": "am"}',1,false,3,1),
	 ('2023-07-30 16:47:30.26164+07',10,'{"7": "is"}',2,true,3,1),
	 ('2023-07-30 20:37:32.597877+07',0,'{"5": "Where", "6": "at his mother"}',1,false,2,2),
	 ('2023-07-30 20:37:41.380737+07',5,'{"5": "Where", "6": "with his mother"}',2,false,2,2),
	 ('2023-07-30 20:37:48.821987+07',10,'{"7": "is"}',1,true,3,2),
	 ('2023-08-01 09:36:12.866035+07',10,'{"7": "is"}',2,true,3,2),
	 ('2023-08-01 17:05:07.442764+07',0,'{"5": "Which", "6": "his mother"}',3,false,2,2);
INSERT INTO public.course_manager_resulttest (created_at,mark,student_answer,number_of_test,pass_exam,exam_id,student_id) VALUES
	 ('2023-08-01 17:05:24.486939+07',0,'{"5": "Which", "6": "his mother"}',4,false,2,2),
	 ('2023-08-01 17:10:51.603446+07',10,'{"7": "is"}',3,true,3,2),
	 ('2023-08-01 17:19:07.125175+07',10,'{"7": "is"}',4,true,3,2),
	 ('2023-08-01 17:19:18.250083+07',10,'{"7": "is"}',5,true,3,2),
	 ('2023-08-01 17:19:34.154527+07',0,'{"7": "are"}',6,false,3,2),
	 ('2023-08-01 17:20:58.53954+07',0,'{"7": "are"}',7,false,3,2),
	 ('2023-08-01 17:21:22.124299+07',10,'{"7": "is"}',8,true,3,2),
	 ('2023-08-01 17:53:52.890679+07',10,'{"7": "is"}',9,true,3,2),
	 ('2023-08-02 09:12:14.461118+07',0,'{"5": "Which", "6": "on his mother"}',3,false,2,1),
	 ('2023-08-02 10:07:35.995515+07',0,'{"7": "were"}',10,false,3,2);
INSERT INTO public.course_manager_resulttest (created_at,mark,student_answer,number_of_test,pass_exam,exam_id,student_id) VALUES
	 ('2023-08-02 16:29:35.29709+07',5,'{"1": "The selective acquisition of knowledge through the use of manual programs", "2": "All of the above", "3": "Random Forest", "4": "Decision trees are robust to outliers"}',2,false,1,2),
	 ('2023-08-02 16:30:09.600732+07',5,'{"1": "The selective acquisition of knowledge through the use of manual programs", "2": "All of the above", "3": "Random Forest", "4": "Decision trees are robust to outliers"}',3,false,1,2);
INSERT INTO public.course_manager_topic (name_topic,description) VALUES
	 ('Math','Math concept'),
	 ('Design','Art and Video'),
	 ('Web','Build your website'),
	 ('DS/AI/ML','Data Science/Artificial intelligence/Machine Learning'),
	 ('Physic','Physics can, at base, be defined as the science of matter, motion, and energy.'),
	 ('Programming','Software'),
	 ('C/C++','C/C++'),
	 ('Python','Python'),
	 ('English','Foreign Language');
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-07-28 14:12:29.169943+07','1','teacher',1,'[{"added": {}}]',2,1),
	 ('2023-07-28 14:13:35.832126+07','2','student1',2,'[{"changed": {"fields": ["Date of birth", "Cover img"]}}]',4,1),
	 ('2023-07-28 14:15:37.060167+07','5','teacher1',3,'',4,1),
	 ('2023-07-28 14:17:13.399677+07','1','teacher',2,'[{"changed": {"fields": ["Permissions"]}}]',2,1),
	 ('2023-07-28 14:17:38.575229+07','1','web',1,'[{"added": {}}]',5,6),
	 ('2023-07-28 14:18:10.098705+07','2','Math',1,'[{"added": {}}]',5,6),
	 ('2023-07-28 14:18:45.243797+07','3','Design',1,'[{"added": {}}]',5,6),
	 ('2023-07-28 14:19:05.640889+07','1','Web',2,'[{"changed": {"fields": ["Name topic"]}}]',5,1),
	 ('2023-07-28 14:20:02.959901+07','4','DS/AI/ML',1,'[{"added": {}}]',5,6),
	 ('2023-07-28 14:20:35.643856+07','5','Physic',1,'[{"added": {}}]',5,6);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-07-28 14:21:09.041468+07','6','Programming',1,'[{"added": {}}]',5,6),
	 ('2023-07-28 14:21:26.89479+07','7','C/C++',1,'[{"added": {}}]',5,6),
	 ('2023-07-28 14:21:50.916975+07','8','Python',1,'[{"added": {}}]',5,6),
	 ('2023-07-28 14:22:25.262574+07','9','English',1,'[{"added": {}}]',5,6),
	 ('2023-07-28 14:28:04.732847+07','1','Machine Learning',1,'[{"added": {}}]',6,6),
	 ('2023-07-28 14:28:59.259599+07','2','Web Front-end',1,'[{"added": {}}]',6,6),
	 ('2023-07-28 14:31:25.630656+07','3','English Grammar',1,'[{"added": {}}]',6,6),
	 ('2023-07-28 14:32:38.353062+07','1','Statistics and Probability',1,'[{"added": {}}]',9,6),
	 ('2023-07-28 14:35:05.976426+07','2','Python basic',1,'[{"added": {}}]',9,6),
	 ('2023-07-28 14:35:52.758906+07','3','Natural Language Processing',1,'[{"added": {}}]',9,6);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-07-28 14:37:32.530456+07','4','Introduce HTML',1,'[{"added": {}}]',9,6),
	 ('2023-07-28 14:38:44.897014+07','5','CSS',1,'[{"added": {}}]',9,6),
	 ('2023-07-28 14:39:54.11258+07','6','Java Script',1,'[{"added": {}}]',9,6),
	 ('2023-07-28 14:42:34.276558+07','4','Photoshop CS5',1,'[{"added": {}}]',6,7),
	 ('2023-07-28 14:43:24.211697+07','5','Adobe Lightroom',1,'[{"added": {}}]',6,7),
	 ('2023-07-28 14:44:03.084722+07','6','Adobe Premiere',1,'[{"added": {}}]',6,7),
	 ('2023-07-28 14:44:47.997713+07','1','Final Test-Machine Learning',1,'[{"added": {}}]',8,6),
	 ('2023-07-28 14:46:06.033704+07','1','What is machine learning?',1,'[{"added": {}}]',11,6),
	 ('2023-07-28 14:46:58.69846+07','2','Machine Learning is a field of AI consisting of learning algorithms that ..............',1,'[{"added": {}}]',11,6),
	 ('2023-07-28 14:47:48.754994+07','3','.............. is a widely used and effective machine learning algorithm based on the idea of baggin',1,'[{"added": {}}]',11,6);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-07-28 14:48:33.423743+07','4','What is the disadvantage of decision trees?',1,'[{"added": {}}]',11,6),
	 ('2023-07-28 14:49:46.960021+07','2','Middle Test-English Grammar',1,'[{"added": {}}]',8,6),
	 ('2023-07-28 14:50:52.779267+07','5','______raiding for camels was a significant part of Bedouin life has  been documented in Wilfed Thesi',1,'[{"added": {}}]',11,6),
	 ('2023-07-28 14:51:28.651458+07','6','The little boy pleaded _____ not to leave him alone in the dark.',1,'[{"added": {}}]',11,6),
	 ('2023-07-28 15:06:52.046982+07','8','teacher3',2,'[{"changed": {"fields": ["Cover img"]}}]',4,1),
	 ('2023-07-28 15:07:04.47527+07','7','teacher2',2,'[{"changed": {"fields": ["Cover img"]}}]',4,1),
	 ('2023-07-28 15:07:18.065499+07','6','teacher1',2,'[{"changed": {"fields": ["Cover img"]}}]',4,1),
	 ('2023-07-28 15:07:31.447813+07','4','student3',2,'[{"changed": {"fields": ["Cover img"]}}]',4,1),
	 ('2023-07-28 15:07:45.497622+07','3','student2',2,'[{"changed": {"fields": ["Cover img"]}}]',4,1),
	 ('2023-07-28 15:07:56.157105+07','2','student1',2,'[{"changed": {"fields": ["Cover img"]}}]',4,1);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-07-28 15:11:46.581811+07','7','Physic with case-study',1,'[{"added": {}}]',6,8),
	 ('2023-07-28 15:12:52.496395+07','7','Physic with case-study',2,'[{"changed": {"fields": ["Cover img"]}}]',6,8),
	 ('2023-07-28 15:23:18.949892+07','3','Natural Language Processing',2,'[{"changed": {"fields": ["Video"]}}]',9,6),
	 ('2023-07-28 15:24:35.792733+07','3','NLP',2,'[{"changed": {"fields": ["Name lesson"]}}]',9,6),
	 ('2023-07-30 16:36:45.277135+07','3','Final test-English Grammar',1,'[{"added": {}}]',8,6),
	 ('2023-07-30 16:37:54.779088+07','7','That ___  a dog.',1,'[{"added": {}}]',11,6),
	 ('2023-07-30 16:41:12.985995+07','7','Noun',1,'[{"added": {}}]',9,6),
	 ('2023-07-31 11:01:16.267837+07','28','Certificate object (28)',3,'',7,1),
	 ('2023-07-31 11:01:16.277506+07','27','Certificate object (27)',3,'',7,1),
	 ('2023-07-31 11:01:16.279206+07','26','Certificate object (26)',3,'',7,1);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-07-31 11:01:16.281719+07','25','Certificate object (25)',3,'',7,1),
	 ('2023-07-31 11:01:16.283252+07','24','Certificate object (24)',3,'',7,1),
	 ('2023-07-31 11:01:16.286053+07','23','Certificate object (23)',3,'',7,1),
	 ('2023-07-31 11:01:16.28847+07','22','Certificate object (22)',3,'',7,1),
	 ('2023-07-31 11:01:16.291916+07','21','Certificate object (21)',3,'',7,1),
	 ('2023-07-31 11:01:16.293545+07','20','Certificate object (20)',3,'',7,1),
	 ('2023-07-31 11:01:16.295974+07','19','Certificate object (19)',3,'',7,1),
	 ('2023-07-31 11:01:16.297303+07','18','Certificate object (18)',3,'',7,1),
	 ('2023-07-31 11:01:16.29968+07','17','Certificate object (17)',3,'',7,1),
	 ('2023-07-31 11:01:16.301222+07','16','Certificate object (16)',3,'',7,1);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-07-31 11:01:16.3041+07','15','Certificate object (15)',3,'',7,1),
	 ('2023-07-31 11:01:16.306175+07','14','Certificate object (14)',3,'',7,1),
	 ('2023-07-31 11:01:16.308917+07','13','Certificate object (13)',3,'',7,1),
	 ('2023-07-31 11:01:16.31045+07','12','Certificate object (12)',3,'',7,1),
	 ('2023-07-31 11:01:16.312881+07','11','Certificate object (11)',3,'',7,1),
	 ('2023-07-31 11:01:16.314282+07','10','Certificate object (10)',3,'',7,1),
	 ('2023-07-31 11:01:16.3166+07','9','Certificate object (9)',3,'',7,1),
	 ('2023-07-31 11:01:16.3184+07','8','Certificate object (8)',3,'',7,1),
	 ('2023-07-31 11:01:16.321889+07','7','Certificate object (7)',3,'',7,1),
	 ('2023-07-31 11:01:16.324627+07','6','Certificate object (6)',3,'',7,1);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-07-31 11:01:16.327191+07','5','Certificate object (5)',3,'',7,1),
	 ('2023-07-31 11:01:16.329439+07','4','Certificate object (4)',3,'',7,1),
	 ('2023-07-31 11:01:16.333043+07','3','Certificate object (3)',3,'',7,1),
	 ('2023-07-31 11:01:16.335865+07','2','Certificate object (2)',3,'',7,1),
	 ('2023-07-31 11:01:16.340021+07','1','Certificate object (1)',3,'',7,1),
	 ('2023-07-31 11:15:43.721389+07','32','Certificate object (32)',3,'',7,1),
	 ('2023-07-31 11:15:43.726492+07','31','Certificate object (31)',3,'',7,1),
	 ('2023-07-31 11:15:43.729351+07','30','Certificate object (30)',3,'',7,1),
	 ('2023-07-31 11:15:43.731122+07','29','Certificate object (29)',3,'',7,1),
	 ('2023-07-31 11:17:29.040704+07','34','Certificate object (34)',3,'',7,1);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-07-31 11:17:29.058437+07','33','Certificate object (33)',3,'',7,1),
	 ('2023-07-31 11:18:14.298746+07','36','Certificate object (36)',3,'',7,1),
	 ('2023-07-31 11:18:14.306782+07','35','Certificate object (35)',3,'',7,1),
	 ('2023-07-31 11:18:42.574709+07','38','Certificate object (38)',3,'',7,1),
	 ('2023-07-31 11:18:42.579551+07','37','Certificate object (37)',3,'',7,1),
	 ('2023-07-31 11:20:30.911694+07','39','Certificate object (39)',3,'',7,1),
	 ('2023-07-31 14:07:38.8247+07','40','Certificate object (40)',3,'',7,1),
	 ('2023-08-01 10:03:44.797732+07','42','Certificate object (42)',3,'',7,1),
	 ('2023-08-01 10:03:44.806667+07','41','Certificate object (41)',3,'',7,1),
	 ('2023-08-01 10:24:04.551185+07','44','Certificate object (44)',3,'',7,1);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-08-01 10:26:54.725926+07','43','Certificate object (43)',3,'',7,1),
	 ('2023-08-01 10:27:02.798385+07','45','Certificate object (45)',3,'',7,1),
	 ('2023-08-01 10:28:01.921415+07','46','Certificate object (46)',3,'',7,1),
	 ('2023-08-01 12:23:44.617405+07','49','Certificate object (49)',3,'',7,1),
	 ('2023-08-01 12:23:44.642468+07','47','Certificate object (47)',3,'',7,1),
	 ('2023-08-01 16:01:35.151929+07','5','student1-Photoshop CS5',3,'',12,1),
	 ('2023-08-01 16:03:29.661829+07','6','student1-Photoshop CS5',3,'',12,1),
	 ('2023-08-01 16:13:26.385835+07','7','Physic in case-study',2,'[{"changed": {"fields": ["Name course"]}}]',6,1),
	 ('2023-08-01 16:14:00.064072+07','7','Physic in case-study',2,'[{"changed": {"fields": ["Time to learn ets"]}}]',6,1),
	 ('2023-08-01 16:24:57.433029+07','4','LessonLearned object (4)',3,'',10,1);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-08-01 16:34:01.200928+07','5','LessonLearned object (5)',3,'',10,1),
	 ('2023-08-01 16:34:01.205229+07','3','LessonLearned object (3)',3,'',10,1),
	 ('2023-08-01 16:34:01.208635+07','2','LessonLearned object (2)',3,'',10,1),
	 ('2023-08-01 16:34:01.210717+07','1','LessonLearned object (1)',3,'',10,1),
	 ('2023-08-01 17:27:17.389357+07','3','student1-Web Front-end',3,'',12,1),
	 ('2023-08-02 10:28:41.142866+07','6','LessonLearned object (6)',3,'',10,1),
	 ('2023-08-02 10:51:25.434204+07','9','PushInformation object (9)',1,'[{"added": {}}]',17,1),
	 ('2023-08-02 11:58:38.347425+07','9','PushInformation object (9)',3,'',17,1),
	 ('2023-08-02 11:58:38.357579+07','8','PushInformation object (8)',3,'',17,1),
	 ('2023-08-02 12:27:32.049453+07','10','PushInformation object (10)',1,'[{"added": {}}]',17,1);
INSERT INTO public.django_admin_log (action_time,object_id,object_repr,action_flag,change_message,content_type_id,user_id) VALUES
	 ('2023-08-02 16:46:14.893726+07','8','LessonLearned object (8)',3,'',10,1),
	 ('2023-08-02 16:46:14.905146+07','7','LessonLearned object (7)',3,'',10,1),
	 ('2023-08-02 16:47:40.352187+07','9','LessonLearned object (9)',3,'',10,1),
	 ('2023-08-02 17:26:16.03092+07','7','Noun',2,'[{"changed": {"fields": ["Video"]}}]',9,6),
	 ('2023-08-02 17:28:59.695942+07','8','Draw with Brush tool',1,'[{"added": {}}]',9,7),
	 ('2023-08-02 17:29:31.472782+07','9','Constrast',1,'[{"added": {}}]',9,7),
	 ('2023-08-02 17:29:56.370189+07','10','Role-A Role-B',1,'[{"added": {}}]',9,7),
	 ('2023-08-02 17:30:41.142587+07','11','lighning',1,'[{"added": {}}]',9,8),
	 ('2023-08-02 17:31:47.556144+07','7','Physics in reality',2,'[{"changed": {"fields": ["Name course"]}}]',6,8);
INSERT INTO public.django_content_type (app_label,model) VALUES
	 ('auth','permission'),
	 ('auth','group'),
	 ('contenttypes','contenttype'),
	 ('authen','user'),
	 ('course_manager','topic'),
	 ('course_manager','course'),
	 ('course_manager','certificate'),
	 ('course_manager','exam'),
	 ('course_manager','lesson'),
	 ('course_manager','lessonlearned');
INSERT INTO public.django_content_type (app_label,model) VALUES
	 ('course_manager','question'),
	 ('course_manager','register'),
	 ('course_manager','resulttest'),
	 ('admin','logentry'),
	 ('sessions','session'),
	 ('webpush','group'),
	 ('webpush','pushinformation'),
	 ('webpush','subscriptioninfo');
INSERT INTO public.django_migrations (app,"name",applied) VALUES
	 ('contenttypes','0001_initial','2023-07-28 14:05:20.1765+07'),
	 ('contenttypes','0002_remove_content_type_name','2023-07-28 14:06:12.012314+07'),
	 ('auth','0001_initial','2023-07-28 14:06:12.092159+07'),
	 ('auth','0002_alter_permission_name_max_length','2023-07-28 14:06:12.099644+07'),
	 ('auth','0003_alter_user_email_max_length','2023-07-28 14:06:12.11054+07'),
	 ('auth','0004_alter_user_username_opts','2023-07-28 14:06:12.119611+07'),
	 ('auth','0005_alter_user_last_login_null','2023-07-28 14:06:12.130084+07'),
	 ('auth','0006_require_contenttypes_0002','2023-07-28 14:06:12.133872+07'),
	 ('auth','0007_alter_validators_add_error_messages','2023-07-28 14:06:12.14113+07'),
	 ('auth','0008_alter_user_username_max_length','2023-07-28 14:06:12.151293+07');
INSERT INTO public.django_migrations (app,"name",applied) VALUES
	 ('auth','0009_alter_user_last_name_max_length','2023-07-28 14:06:12.158816+07'),
	 ('auth','0010_alter_group_name_max_length','2023-07-28 14:06:12.169513+07'),
	 ('auth','0011_update_proxy_permissions','2023-07-28 14:06:12.18278+07'),
	 ('auth','0012_alter_user_first_name_max_length','2023-07-28 14:06:12.191351+07'),
	 ('authen','0001_initial','2023-07-28 14:06:12.258283+07'),
	 ('course_manager','0001_initial','2023-07-28 14:06:36.371315+07'),
	 ('admin','0001_initial','2023-07-28 14:08:15.357777+07'),
	 ('admin','0002_logentry_remove_auto_add','2023-07-28 14:08:15.373019+07'),
	 ('admin','0003_logentry_add_action_flag_choices','2023-07-28 14:08:15.392308+07'),
	 ('sessions','0001_initial','2023-07-28 14:08:15.412589+07');
INSERT INTO public.django_migrations (app,"name",applied) VALUES
	 ('course_manager','0002_certificate_score_alter_certificate_pdf_url','2023-07-31 09:27:24.401351+07'),
	 ('course_manager','0003_certificate_created_at_certificate_updated_at','2023-07-31 09:32:09.902405+07'),
	 ('webpush','0001_initial','2023-08-01 15:04:28.909264+07'),
	 ('webpush','0002_auto_20190603_0005','2023-08-01 15:04:28.920394+07'),
	 ('webpush','0003_subscriptioninfo_user_agent','2023-08-01 15:04:28.931947+07'),
	 ('webpush','0004_auto_20220831_1500','2023-08-01 15:04:29.076579+07');
INSERT INTO public.django_session (session_key,session_data,expire_date) VALUES
	 ('fqtbe2dp046cgse0t83rm1q9pc029d6x','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qR9Cl:OPryeHTVe6gE3p3YouIR5eijxlQqf2qdMrG8MIj6xUA','2023-08-16 17:35:47.551741+07'),
	 ('bikszipernsrxvdchk2xyjoa8u81ovj3','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qPHdU:7GyguF30RWuQxrYEdTGOv4HfI6lPewq2Z2yaEq9LMV4','2023-08-11 14:11:40.634559+07'),
	 ('0chjo7nedms8pnhlw4xwplojbgq3x8sw','.eJxVjDsOwjAQBe_iGlnejT8xJX3OYNneDQ4gR4qTCnF3EikFtG9m3luEuK0lbI2XMJG4ik5cfrcU85PrAegR632Wea7rMiV5KPKkTQ4z8et2un8HJbay18CJqIfRWUvRGLaRktZIjKh950bfKwPKZdTKsgFUSuesPDvcQ7AgPl_lnDdk:1qR4TG:6cLMV3EeYfD9rM3f1yG5teoWqN5cPsXxcOazuN9R4ks','2023-08-16 12:32:30.134489+07'),
	 ('ke2g13bkb6vp7hkw71yz7751107hmu7q','.eJxVjDsOwjAQBe_iGlmJP1mbkj5niHa9Cw4gW4qTCnF3iJQC2jcz76Um3NY8bU2WaWZ1Vk6dfjfC9JCyA75juVWdalmXmfSu6IM2PVaW5-Vw_w4ytvytia0IsKWhY4Pke2dQKPrAiToGTs46CRHAUh8cmkFMSNAzAHvw8areHwaLOEE:1qR6DZ:-scaAccNOjzEB72amGUAFfkVGNe-lP26KwdhlXWAyhw','2023-08-16 14:24:25.387585+07'),
	 ('wkowz6on7e99uyd88ga05hul6dvfod2i','.eJxVjDsOwjAQBe_iGlmOP4mXkj5nsHbXDg4gW4qTCnF3EikFtG9m3lsE3NYctpaWMEdxFV5cfjdCfqZygPjAcq-Sa1mXmeShyJM2OdaYXrfT_TvI2PJek_WAGL11oMkY2yN7p9Aqp0AxAIN2SNagiTR0vp8mHbmDQevdd86IzxfQxTcZ:1qPIWN:SB4PYNlfUXya0gD7TsJvUqotOg4DRxXpFlZTo-x8oyg','2023-08-11 15:08:23.933706+07'),
	 ('nfkns3lqa1be9ip1ijo2moolkjt7rtal','.eJxVjDsOwjAQBe_iGlmOP4mXkj5nsHbXDg4gW4qTCnF3EikFtG9m3lsE3NYctpaWMEdxFV5cfjdCfqZygPjAcq-Sa1mXmeShyJM2OdaYXrfT_TvI2PJek_WAGL11oMkY2yN7p9Aqp0AxAIN2SNagiTR0vp8mHbmDQevdd86IzxfQxTcZ:1qPIaR:WITp-1zOCTjHCeKm9JucS8VUfI6XBNFpWcAto7Lp5pc','2023-08-11 15:12:35.4469+07'),
	 ('fht8mlz88l41xhmr9ocyyyh52n7xc9wy','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qPIyC:WcrWxnavCqhzvfo7zCf9uHJxgvW7mnYKAe6iE_PM81U','2023-08-11 15:37:08.660748+07'),
	 ('8wnt8rnr21uzl04cc81ill1qpisgeze9','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qPK7E:Pgir3IMuL-2_pdZifVVxvRSaM_Ssfh0clMgpbNIMzAI','2023-08-11 16:50:32.309622+07'),
	 ('w2fhphca7q33eh1fmraqcmm964k17q6b','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qPK7b:71TLunqT1Qp3STHT_4-1YgdtcKYhkQexG6PJNSGitSs','2023-08-11 16:50:55.747805+07'),
	 ('ych649zjz32x2fbxmeusa6p8hp11q418','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qQ3Eg:xoEcfUFeFomVWa-9f_sJhU7cqV_X0_Pyuk7hjbx0bM8','2023-08-13 17:01:14.247801+07');
INSERT INTO public.django_session (session_key,session_data,expire_date) VALUES
	 ('mac3fcm7576f48lbl2cm2kbfddx39ekf','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qQ3HE:On-ElLI1sEiZVYacgbYhNihOhLrqxeaa8muviQ2Brvo','2023-08-13 17:03:52.581263+07'),
	 ('asix4gfy1l8rfbum4al38kwnggr7b1qv','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qQ6Dx:R-faU6iTg5W_6uscV-hVcJmBSvutKG1aQb77l8KcVjk','2023-08-13 20:12:41.458658+07'),
	 ('xa8rphewjop8nj6cejl16e080eucy3qq','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qQ9CJ:XSN20PsHNcdjAWP28aTxkEtkdT3VcDkMGlYgOJUSMt0','2023-08-13 23:23:11.774602+07'),
	 ('w7h769uzyk0g643z8r2tplckf4tdfwsx','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qQ9X8:bw4hVlDlwE8MFx97k4XeltvASkDxp6YsQc9-Dd-fGq4','2023-08-13 23:44:42.594801+07'),
	 ('wtcaofumuq53ujax8aszaayqnn80sp3t','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qQIeh:BFPP8Ddb_nlrDa-cKpnqon0zJUziJbAfeki67cKQiXo','2023-08-14 09:29:07.264063+07'),
	 ('9b42q6gunkt3dk95mh75x00k7r04muq0','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qQKHk:17AQnj1iOvi6rCewvUtgSrNETLAz4Ec3j-VzMzSdc8U','2023-08-14 11:13:32.74469+07'),
	 ('9cvdc17fe2zz85rdn2hqnhrm3vb3tkr4','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qQKI5:ALaS55lhdnEf_4MwDUrZhsonJwz75lRFoznowqd7_FI','2023-08-14 11:13:53.163533+07'),
	 ('h59acj39ex0bh0wfe2cjt0bnu2uhe5a6','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qQN02:En4fgbQEfV3LWFLJ_89qfGfhrBwoC8nzNA83rCrlgxQ','2023-08-14 14:07:26.449806+07'),
	 ('xqm4fztic7s70yd60dtyxi1wio418zx3','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qQNNa:nVnljlA9xhIllI5Al5dXRS22r-1tDLhdZjEAZ3_9VQ8','2023-08-14 14:31:46.507856+07'),
	 ('ip1xtb58hkrewouxtq6806phh5hhwadr','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qQffX:1y9jf5GNTEMwWjG9m6GvzTL8vpl54T2WbhmIOu1WPKw','2023-08-15 10:03:31.3452+07');
INSERT INTO public.django_session (session_key,session_data,expire_date) VALUES
	 ('6jsd9tupzm3t4zl4r40uiqlvi5kh9iw5','.eJxVjEEOwiAQAP_C2ZAuFsp69O4byMIuUjU0Ke3J-HdD0oNeZybzVoH2rYS9yRpmVhfl1OmXRUpPqV3wg-p90Wmp2zpH3RN92KZvC8vrerR_g0Kt9C0OKftEI6CAh5xwAnLg-TyBZGtdYmG0A2UHGTmPFqwhwEgsxgCpzxfreTg6:1qQgt1:B6-lJntYYvsQ92N-URhzMw4CLrRnnhvTfMDi62d7TxA','2023-08-15 11:21:31.586275+07'),
	 ('uwpic8o5ocvq32czyxpz7cqjjgs8okbf','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qQhqz:0MBtBVcQeGK_gbE5hsol4ewl9zRag0ZZtuVC6tWvwC4','2023-08-15 12:23:29.92606+07'),
	 ('t5f58xay7mhzq7xo29i05lgs9fsyq5uh','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qQlbG:uz_xYhZJMQTYEqM7p1mfyYZ8RejtjDd_086e3bRRqNY','2023-08-15 16:23:30.743265+07'),
	 ('us8hzdlr0y63m3xcxjclm1gu753knjco','e30:1qQres:nlTpVPV396xfW-ECVsZGOoi8NPL4iQc3JwGLw_FzLq0','2023-08-15 22:51:38.517843+07'),
	 ('2ase2zuo1q0c90x5b1qp56j8jy64vepk','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qQrfx:a7-DeiItujCq64SJlIbcJoTnJMtol1bjVXH1fKx_Ej4','2023-08-15 22:52:45.516966+07'),
	 ('7a7130tx9vrneqedg04wajvsxfbgfrjj','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qR1Kq:wfv_cBvE017TWu83JQFpmCknt7pDdNz-UjC5EemChXo','2023-08-16 09:11:36.595308+07'),
	 ('khffv0pj8k15wk9zgm3zhcwmjgq1a05s','e30:1qR1l7:TFkTSoMjdGA5JatVIfI4_oeX-Yl1OxbbGRojsaQaJTo','2023-08-16 09:38:45.678714+07'),
	 ('uyhan5iapchiwnf90mm6t01l5x722mt6','.eJxVjEEOwiAQAP_C2ZAuFsp69O4byMIuUjU0Ke3J-HdD0oNeZybzVoH2rYS9yRpmVhfl1OmXRUpPqV3wg-p90Wmp2zpH3RN92KZvC8vrerR_g0Kt9C0OKftEI6CAh5xwAnLg-TyBZGtdYmG0A2UHGTmPFqwhwEgsxgCpzxfreTg6:1qR4QV:3eKlQDpq5kvzRzrB8kMtv5V8wCO7T1UHUEZR6tQ5Uf8','2023-08-16 12:29:39.105623+07'),
	 ('q1maj1f1w3fclxc491gxctrcsf8oyk6v','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qR1nt:j6jlp5R1NXEGaLHn5Oq3hVfartYxkjVf994DswcR8gA','2023-08-16 09:41:37.752171+07'),
	 ('vvs7qeiddck91ozeqkqfmmuul6czfcqr','.eJxVjMsOgjAQRf-la9NQLEzr0j3fQObRsagpCYWV8d-VhIVu7znnvsyI25rHraZlnMRcjDOn342QH6nsQO5YbrPluazLRHZX7EGrHWZJz-vh_h1krPlbtwpNVEXuhbQjVm0xus4TAoMoeD37LiAF6hliaLxon5JrhAlAHJj3Bx6TOTY:1qR2Wh:tT3izPBCoZPrHDpy1_BWBUnPpIZXbHeukeZvfEB_6DI','2023-08-16 10:27:55.724509+07');
INSERT INTO public.django_session (session_key,session_data,expire_date) VALUES
	 ('x8qcnzq2fki6el7l9kgrykaurpd50qv1','.eJxVjDsOwjAQBe_iGllex7-lpOcM1vqHA8iW4qRC3B0ipYD2zcx7MU_bWv028uLnxM4M2el3CxQfue0g3andOo-9rcsc-K7wgw5-7Sk_L4f7d1Bp1G89gQ7RgFQ0kVAZA6F2hXTUE5QcSNpUhAQUSaI2IsQETjkjrRUIGIG9P97cNzo:1qR34h:gDTXsSXErxKBn_swhYTR-nbba-NrYx4j4jbWft8WJzg','2023-08-16 11:03:03.43698+07'),
	 ('4yedn6otvkpwvsd22up2xw95wdxxbt2l','e30:1qR7Lh:yiDexV_08copnjeV3GfX3obxyUmGDciIftcHX0i-T_w','2023-08-16 15:36:53.107405+07'),
	 ('5nfm8rmm7uwdcosnmp2bg8pt6lmqt310','.eJxVjDsOwjAQBe_iGlmLf9iU9DmDtd51cADZUpxUiLuTSCmgfTPz3iLiupS49jzHicVVKHH63RLSM9cd8APrvUlqdZmnJHdFHrTLoXF-3Q7376BgL1vt0kgU8iV4lQjQZA1sDXiTSY3oTbLasQ7W-WSBQKEFPDOzIjZbasXnC_ZkOII:1qR7dv:lfHJ40MpdlU7NM_wgdb50WZSFuROVPeJWLwr7Y2vgdI','2023-08-16 15:55:43.876549+07'),
	 ('zxwviax9nps6iubc64tee5jg86ni0lm5','.eJxVjDsOwjAQBe_iGlmOP4mXkj5nsHbXDg4gW4qTCnF3EikFtG9m3lsE3NYctpaWMEdxFV5cfjdCfqZygPjAcq-Sa1mXmeShyJM2OdaYXrfT_TvI2PJek_WAGL11oMkY2yN7p9Aqp0AxAIN2SNagiTR0vp8mHbmDQevdd86IzxfQxTcZ:1qR97E:yHwSNHPdgFW2EgAJNExsSj6L_mSGtTE63jX7eFRD-tY','2023-08-16 17:30:04.984414+07');
INSERT INTO public.webpush_pushinformation (group_id,subscription_id,user_id) VALUES
	 (NULL,15,2);
INSERT INTO public.webpush_subscriptioninfo (browser,endpoint,auth,p256dh,user_agent) VALUES
	 ('chrome','https://fcm.googleapis.com/fcm/send/dcri42zqNKc:APA91bHv7qOju_9t2_-fVN0nV0Z5F70I_M9xMvIt0bw-OPP2MBRK1iYfqd9XeRSHdioz_1VhlOoyYc6q959wvJjQjXD7eFphhfmbRb45cjoHf6umaq8bDAzRXzMOxHB7Gz_d4lHPEv1N','COjNHsJXXONR2jg3vAfCbA','BMJogv9NMviDmb90lBiftQTeEJZsyvWn18wAn4Tg7BEdEXPjylbC5z5jLvCa2PZ3FFrEofjd0CyVl4tHUt4vQsM','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36');
