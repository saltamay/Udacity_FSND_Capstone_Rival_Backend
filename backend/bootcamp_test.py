import os
import unittest
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import app
from config.config import Test
from database.db_test import setup_db
from models.bootcamp import Bootcamp
from models.course import Course


class BootcampsTestCase(unittest.TestCase):
    '''This class represents the bootcamp report test case'''

    def setUp(self):
        '''Define test variables and initialize app.'''
        self.app = app
        # propagate the exceptions to the test client
        self.app.testing = True
        self.client = self.app.test_client
        setup_db(self.app, Test.SQLALCHEMY_DATABASE_URI)

        self.new_bootcamp = {
            "name": "UofT SCS BootCamps",
            "description": "University of Toronto School of Continuing Studies (UofT SCS) Boot Camps equip you with essential skills to help guide your path to success. With strategically engineered curricula, face-to-face interaction, and expert instructors, we provide an educational experience that will shape the future of your career.",
            "website": "bootcamp.learn.utoronto.ca",
            "phone": "(647) 245-1020",
            "email": "bootcamp@trilogyed.com",
            "address": "158 St George St, Toronto, ON M5S 2V8",
            "careers": ["Coding", "Data Analytics", "Cybersecurity", "UX/UI", "FinTech"],
            "job_assistance": True
        }

        self.updated_bootcamp = {
            "name": "Devworks Bootcamp",
            "description": "Devworks is a full stack JavaScript Bootcamp located in the heart of Boston that focuses on the technologies you need to get a high paying job as a web developer",
            "website": "https://devworks.com",
            "phone": "(555) 555-555",  # Update phone number
            "email": "enroll@devworks.com",
            "address": "233 Bay State Rd Boston MA 02215",
            "careers": ["Web Development", "UI/UX", "Business"],
            "job_assistance": True  # Update job assistance
        }

        self.new_course = {
            "title": "Front End Web Development",
            "description": "This course will provide you with all of the essentials to become a successful frontend web developer. You will learn to master HTML, CSS and front end JavaScript, along with tools like Git, VSCode and front end frameworks like Vue",
            "duration": 8,
            "tuition": 8000,
            "minimum_skill": "beginner",
            "scholarships_available": True
        }

        # '''binds the app to the current context'''
        # with self.app.app_context():
        #     self.db = SQLAlchemy()
        #     self.db.init_app(self.app)
        #     '''create all tables'''
        #     self.db.drop_all()
        #     self.db.create_all()
        #     db_test_init()

    def tearDown(self):
        '''Executed after each test'''
        pass

    def test_get_all_bootcamps(self):
        res = self.client().get('/api/v1/bootcamps')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['data']))

    def test_add_bootcamp(self):
        res = self.client().post('/api/v1/bootcamps', json=self.new_bootcamp)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['data'])
        self.assertTrue(len(data['data']))

    def test_get_bootcamp_by_id(self):
        res = self.client().get('/api/v1/bootcamps/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['data'])
        self.assertTrue(len(data['data']))

    def test_update_bootcamp_by_id(self):
        res = self.client().put('/api/v1/bootcamps/1', json=self.updated_bootcamp)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['data'])
        self.assertTrue(len(data['data']))

    def test_delete_bootcamp_by_id(self):
        res = self.client().delete('/api/v1/bootcamps/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


'''Make the tests executable'''
if __name__ == "__main__":
    unittest.main()
