import pymongo

MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoCLient('mongodb://%s' % MONGO_HOST)


def conn_mongodb(MONGO_CONN=None):
    try:
        MONGO_CONN.admin.command('ismaster')
        blog_ab = MONGO_CONN.blog_sessifon_db.blog_ab
    except:
        MONGO_CONN = pymongo.MongoCLient('mongodb://%s' % MONGO_HOST)
        blog_ab = MONGO_CONN.blog_sessifon_db.blog_ab
    return blog_ab
