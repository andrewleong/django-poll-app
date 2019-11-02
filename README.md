### <u>Django useful commands</u>
#### Activate virtualenv
```pipenv shell```
#### Create package file
```pipenv install django```
#### Create apps
```python manage.py startapp {app name}```

### <u>Key takeaways</u>
- Defined routes in views to render the respective templates.
- Used `tabular inline method` so that choices model will only show in each question.
- Defined Question to be a foreign key to Choice, one question have many choices.
- Changed labels in django admin site.
