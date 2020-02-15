import unittest
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import app
from config.config import Test
from database.db_test import setup_db, drop_and_create_all, db_test_init
from models.bootcamp import Bootcamp


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

        self.dublicate_bootcamp = {
            "name": "Devworks Bootcamp",
            "description": "Devworks is a full stack JavaScript Bootcamp located in the heart of Boston that focuses on the technologies you need to get a high paying job as a web developer",
            "website": "https://devworks.com",
            "phone": "(111) 111-1111",
            "email": "enroll@devworks.com",
            "address": "233 Bay State Rd Boston MA 02215",
            "careers": ["Web Development", "UI/UX", "Business"],
            "job_assistance": False
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

        self.updated_bootcamp_malformed = {
            "name": "Devworks Bootcamp",
            "description": "Devworks is a full stack JavaScript Bootcamp located in the heart of Boston that focuses on the technologies you need to get a high paying job as a web developer",
            "website: https // devworks.com"
            "phone": "(111) 111-111",
            "email": "enroll@devworks.com",
            "address": "233 Bay State Rd Boston MA 02215",
            "careers": ["Web Development", "UI/UX", "Business"],
            "job_assistance": False
        }

    def tearDown(self):
        '''Executed after each test'''
        pass

    def test_add_bootcamp(self):
        res = self.client().post('/api/v1/bootcamps', json=self.new_bootcamp)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['data'])
        self.assertTrue(len(data['data']))

    def test_get_all_bootcamps(self):
        res = self.client().get('/api/v1/bootcamps')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
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

    def test_404_sent_when_bootcamps_empty(self):
        '''Remove the element from the db'''
        self.client().delete('/api/v1/bootcamps/1')

        res = self.client().get('/api/v1/bootcamps')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_422_if_add_bootcamp_fails(self):
        res = self.client().post('/api/v1/bootcamps', json=self.dublicate_bootcamp)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_404_if_bootcamp_does_not_exist(self):
        res = self.client().get('/api/v1/bootcamps/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_404_if_update_bootcamp_fails(self):
        res = self.client().put('/api/v1/bootcamps/1000', json=self.updated_bootcamp)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_422_if_update_bootcamp_fails(self):
        res = self.client().put('/api/v1/bootcamps/1', json=self.updated_bootcamp_malformed)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_404_if_delete_bootcamp_fails(self):
        res = self.client().delete('/api/v1/bootcamps/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')


'''Make the tests executable'''
if __name__ == "__main__":
    unittest.main()
