-- Convert the table to UTF8
-- cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
-- Convert the 'name' field to UTF8

USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
