from behave import *
from properties import *
from payload import *
import requests

@given('the book details which needs to be added to Library')
def step_impl(context):
 context.url = endpoint+add
 context.headers = {"Content-Type": "application/json"}
 context.payload = addBook('newab9c14569')

@when('we execute add book POST API method')
def step_impl(context):
 context.post_req = requests.post(context.url, json=context.payload, headers=context.headers,)

@then('book is successfully added')
def step_impl(context):
 res_json = context.post_req.json()
 print(res_json)