""" Set Api configurations """
from flask import Flask
from flask_env import MetaFlaskEnv


class Configuration(metaclass=MetaFlaskEnv):
    """ Configurations"""
    DEBUG = False
    PORT = 5000
