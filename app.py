#!/usr/bin/env python
import web
import xml.etree.ElementTree as ET
from pymongo import MongoClient

tree = ET.parse('user_data.xml')
root = tree.getroot()
uri = "mongodb://gojek-sharath:QbXmwBtPdYeG4bwKMWwElvR3xER7NLQycaD5GXpIoUvoYk2OoXKRK2OjKrycNpMD21h8Vs3HozFYkPs1dc97vg==@gojek-sharath.documents.azure.com:10250/?ssl=true&ssl_cert_reqs=CERT_NONE"
client = MongoClient(uri)
db=client.test1_database
posts = db.posts
urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user',
    '/add_route', 'add_route'
)

app = web.application(urls, globals())

class list_users:
    def GET(self):
	output = 'users:[';
	for child in root:
                print 'child', child.tag, child.attrib
                output += str(child.attrib) + ','
	output += ']';
        return output

class get_user:
    def GET(self, user):
        ret_data = posts.find({"user_id": user})
        return ret_data

class add_route:
    def POST(self):
        post_data = web.input()
        print post_data
        posts.insert_one(post_data).inserted_id

if __name__ == "__main__":
    app.run()
