from app import app
from db_test import drop_and_create_all, db_test_init
from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
import json
import unittest
from dotenv import load_dotenv
load_dotenv()

# from models import Bootcamp, Course

USER_AUTH_TOKEN = os.getenv('USER_AUTH_TOKEN')
ADMIN_AUTH_TOKEN = os.getenv('ADMIN_AUTH_TOKEN')


class CoursesTestCase(unittest.TestCase):
    '''This class represents the course report test case'''

    def setUp(self):
        '''Define test variables and initialize app.'''
        self.app = app
        self.app.config.from_object('config.Test')
        # propagate the exceptions to the test client
        self.app.testing = True
        self.client = self.app.test_client
        drop_and_create_all()
        db_test_init()

        self.user_auth_header = {
            "Authorization": f"Bearer {USER_AUTH_TOKEN}"
        }

        self.admin_auth_header = {
            "Authorization": f"Bearer {ADMIN_AUTH_TOKEN}"
        }

        self.new_course = {
            "title": "Front End Web Development",
            "description": "This course will provide you with" +
            "all of the essentials to become a successful" +
            "frontend web developer. You will learn to master" +
            "HTML, CSS and front end JavaScript, along with tools like Git," +
            "VSCode and front end frameworks like Vue",
            "duration": 8,
            "tuition": 8000,
            "minimumSkill": "beginner",
            "scholarshipsAvailable": True,
            "bootcampId": 1
        }

        self.dublicate_course = {
            "title": "Full Stack Web Development",
            "description": "In this course you will learn full stack" +
            "web development, first learning all about the frontend" +
            "with HTML/CSS/JS/Vue and then the backend with" +
            "Node.js/Express/MongoDB",
            "duration": 12,
            "tuition": 10000,
            "minimumSkill": "intermediate",
            "scholarshipsAvailable": True,
            "upvotes": 93,
            "bootcampId": 1}

        self.updated_course = {
            "title": "Full Stack Web Development",
            "description": "In this course you will learn full stack" +
            "web development, first learning all about the frontend" +
            "with HTML/CSS/JS/Vue and then the backend" +
            "with Node.js/Express/MongoDB",
            "duration": 12,
            "tuition": 10000,
            "minimumSkill": "intermediate",
            "scholarshipsAvailable": False,  # Update scholarships_avalible
            "upvotes": 93
        }

        self.updated_course_malformed = {
            "title": "Full Stack Web Development",
            "description": "In this course you will learn full stack" +
            "web development, first learning all about the frontend" +
            "with HTML/CSS/JS/Vue and then the backend" +
            "with Node.js/Express/MongoDB",
            "duration": 12,
            "tuition": 10000,
            "minimum_skill intermediate"
            "scholarships_available": True,
            "upvotes": 93,
            "bootcamp_id": 1
        }

    def tearDown(self):
        '''Executed after each test'''
        pass

    def test_add_course(self):
        res = self.client().post(
            '/api/v1/courses',
            headers=self.admin_auth_header,
            json=self.new_course)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['data'])
        self.assertTrue(len(data['data']))

    def test_get_all_courses(self):
        res = self.client().get('/api/v1/courses')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['data']))

    def test_get_course_by_id(self):
        res = self.client().get('/api/v1/courses/1',
                                headers=self.user_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['data'])
        self.assertTrue(len(data['data']))

    def test_update_course_by_id(self):
        res = self.client().put(
            '/api/v1/courses/1',
            headers=self.admin_auth_header,
            json=self.updated_course)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['data'])
        self.assertTrue(len(data['data']))

    def test_delete_course_by_id(self):
        res = self.client().delete('/api/v1/courses/1',
                                   headers=self.admin_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_sent_when_courses_empty(self):
        '''Remove the element from the db'''
        self.client().delete('/api/v1/courses/1',
                             headers=self.admin_auth_header)

        res = self.client().get('/api/v1/courses')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_422_if_add_course_fails(self):
        res = self.client().post(
            '/api/v1/courses',
            headers=self.admin_auth_header,
            json=self.dublicate_course)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_404_if_course_does_not_exist(self):
        res = self.client().get('/api/v1/courses/1000',
                                headers=self.user_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_404_if_update_course_fails(self):
        res = self.client().put(
            '/api/v1/courses/1000',
            headers=self.admin_auth_header,
            json=self.updated_course)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_422_if_update_course_fails(self):
        res = self.client().put(
            '/api/v1/courses/1',
            headers=self.admin_auth_header,
            json=self.updated_course_malformed)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_404_if_delete_course_fails(self):
        res = self.client().delete(
            '/api/v1/courses/1000',
            headers=self.admin_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_401_if_user_auth_missing(self):
        res = self.client().get('/api/v1/courses/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    def test_401_if_admin_auth_missing(self):
        res = self.client().delete('/api/v1/courses/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')


'''Make the tests executable'''
if __name__ == "__main__":
    unittest.main()
