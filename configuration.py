""" Set Api configurations """
from flask import Flask
from flask_env import MetaFlaskEnv


class Configuration(metaclass=MetaFlaskEnv):
    """ Configurations"""
    DEBUG = True
    PORT = 8080
    ENV_PREFIX = 'WEDEAL_'
    ENV_LOAD_ALL = True