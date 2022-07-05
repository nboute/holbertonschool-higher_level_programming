-- This script converts a database to UTF8
-- Converts database to utf8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Converts table first_table to utf8
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- Converts field name to utf8
ALTER TABLE first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
