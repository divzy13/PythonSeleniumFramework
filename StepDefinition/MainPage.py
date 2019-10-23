from behave import given, when, then
from FrameWork.Base import BaseApp


@given(u'I Open the Website')
def step_imp_open_website(context):
    BaseApp.load_website()
