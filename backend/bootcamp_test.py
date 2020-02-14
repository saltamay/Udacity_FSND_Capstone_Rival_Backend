import os
import unittest
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import app
from config.config import Test
from database.db import setup_db
from models.bootcamp import Bootcamp
from models.course import Course


class BootcampsTestCase(unittest.TestCase):
    '''This class represents the bootcamp report test case'''

    def setUp(self):
        '''Define test variables and initialize app.'''
        self.app = app
        self.client = self.app.test_client
        # propagate the exceptions to the test client
        self.app.testing = True
        setup_db(self.app, Test.SQLALCHEMY_DATABASE_URI)

        self.new_bootcamp = {
            "name": "UofT SCS BootCamps",
            "description": "University of Toronto School of Continuing Studies (UofT SCS) Boot Camps equip you with essential skills to help guide your path to success. With strategically engineered curricula, face-to-face interaction, and expert instructors, we provide an educational experience that will shape the future of your career.",
            "website": "bootcamp.learn.utoronto.ca",
            "phone": "(647) 245-1020",
            "email" "bootcamp@trilogyed.com"
            "address": "158 St George St, Toronto, ON M5S 2V8",
            "careers": ["Coding", "Data Analytics", "Cybersecurity", "UX/UI", "FinTech"],
            "job_assistance": True
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
        #     self.db.create_all()

    def tearDown(self):
        '''Executed after reach test'''
        pass

    def test_get_all_bootcamps(self):
        res = self.client().get('/api/v1/bootcamps')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['data']))


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
