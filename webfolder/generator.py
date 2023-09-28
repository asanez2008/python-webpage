"""This generates the key for the password reset function"""
import uuid


def make_key():
    """This function creates the uuid key
    for the password reset"""
    return uuid.uuid4()
