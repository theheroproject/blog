sql = "
CREATE TABLE user_info (
    USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    USER_EMAIL VARCHAR(100) NIOT NULL,
    BLOG_ID CHAR(4),
    PRIMARY KEY(USER_ID)
);
"
dave_db.execute(sql)
db_conn.commit()