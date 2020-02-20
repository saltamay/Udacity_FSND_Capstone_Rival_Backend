import os
from dotenv import load_dotenv
load_dotenv()

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
    ALGORITHMS = os.getenv('ALGORITHMS')
    API_AUDIENCE = os.getenv('API_AUDIENCE')


class Development:
    # FLASK_ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DEV_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
    ALGORITHMS = os.getenv('ALGORITHMS')
    API_AUDIENCE = os.getenv('API_AUDIENCE')


class Test:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_TEST_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS')
    # USER_AUTH_TOKEN = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpX'
    #                    'VCIsImtpZCI6IlF6QTJSamt4UWpORU1UZ'
    #                    'zRSVFJGUmpjME5qWXlNRVJFTlVGRk1FVTVOekpETWpBM01'
    #                    'EZzBNdyJ9.eyJpc3MiOiJodHRwczovL3JpdmFsYXBwLmF1'
    #                    'dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZTRjNGYzNTUyYjE'
    #                    '4YjBlODA1NGEzOTUiLCJhdWQiOlsicml2YWwiLCJodHRwcz'
    #                    'ovL3JpdmFsYXBwLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpY'
    #                    'XQiOjE1ODIxNDgxMDMsImV4cCI6MTU4MjIzNDUw'
    #                    'MywiYXpwIjoiTTlXQWNsSTFxOVh4OVBDUTdvSUVxV0Y4czgw'
    #                    'ODdGamwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsI'
    #                    'iwicGVybWlzc2lvbnMiOlsiZ2V0OmJvb3RjYW1wLWRldGFpbC'
    #                    'IsImdldDpjb3Vyc2UtZGV0YWlsIl19.dcxeL4WhtwREsFyWHW'
    #                    'ZEwQgbIj8FPBR495WsqkTJVUXLitZ50N1gnBnLBPmfnRHjooA'
    #                    '7s_pd6bglfCOfuz3q-aMLJfQiiqdbrSISrT-P9O61Y8s'
    #                    'rrmSc8ej_wKhLdF7CmenX_eTfnHzAFGS2C5Jt5TLoUtxtpV1'
    #                    'etOiBUedrFn0EVORku4GEBWpWccMFWgKPybReqdqfP7CyJJb'
    #                    'A6yezd4P1gDIWABSQb0l7zMFfDWPZn-52NjM4eBerQuk2fY6'
    #                    'KP1sSwmjY2vOs0exrshYFS8_fxpOpCmphU-J3QMvK_yjR49'
    #                    'rF3B_wCKr2zflpSy3ijt0KUZ73EjXPcTXThplVzA')

    # ADMIN_AUTH_TOKEN = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZ'
    #                     'CI6IlF6QTJSamt4UWpORU1UZzRSVFJGUmpjME5qWX'
    #                     'lNRVJFTlVGRk1FVTVOekpETWpBM01EZzBNdyJ9.eyJ'
    #                     'pc3MiOiJodHRwczovL3JpdmFsYXBwLmF1dGgwLmNvb'
    #                     'S8iLCJzdWIiOiJhdXRoMHw1ZTQ5ZTg1MThhNDA5ZTBl'
    #                     'NjIwMjg4ODciLCJhdWQiOlsicml2YWwiLCJodHRwczo'
    #                     'vL3JpdmFsYXBwLmF1dGgwLmNvbS91c2VyaW5mbyJdLC'
    #                     'JpYXQiOjE1ODIxNDc3MzAsImV4cCI6MTU4MjIzNDEzM'
    #                     'CwiYXpwIjoiTTlXQWNsSTFxOVh4OVBDUTdvSUVxV0Y4'
    #                     'czgwODdGamwiLCJzY29wZSI6Im9wZW5pZCBwcm9maWx'
    #                     'lIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYWRkOmJvb3RjYW'
    #                     '1wcyIsImFkZDpjb3Vyc2VzIiwiZGVsZXRlOmJvb3RjYW1'
    #                     'wcyIsImRlbGV0ZTpjb3Vyc2VzIiwiZ2V0OmJvb3RjYW1w'
    #                     'LWRldGFpbCIsImdldDpjb3Vyc2UtZGV0YWlsIi'
    #                     'widXBkYXRlOmJvb3RjYW1wcyIsInVwZGF0ZTpjb3Vyc2'
    #                     'VzIl19.sv4yuMyA1Nb1_IuqkDHNDJzLo139x7Ldxo7Tx'
    #                     '23HnF8JmD-B-UHYcoZddhjlP2v6i3hpQhlsB1ykIL'
    #                     '_vcQm6uoOswRkp_DwqFFf_z6kj1tn8meGRE8fVeHrdBiS'
    #                     'XgtjFx7aDmScbVh3gSjjnF9N4M2yokN_OV1g6kQ5msPzY'
    #                     'U2b02iOU_4sNwaZPRmb7NTDVqhwXFd42vzzR7bT5Pdg'
    #                     'fm2hYyzcfeoMD1TdkMjGDWxwS6PngDOJgfbxuigfKqTYB'
    #                     'lI3fJhdmkbdPlbxxRk15rJYdfDgrOa2id5WXZCbbEhDmUR'
    #                     '2cu7rFQtiUNGqGGerSqVMpL2ReJpDyL9v7EGCH9A')
