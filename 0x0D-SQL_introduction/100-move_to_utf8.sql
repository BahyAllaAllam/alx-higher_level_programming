-- Convert the table to UTF8
-- cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
-- Convert the 'name' field to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
USE hbtn_0c_0;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN name VARCHAR (256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
