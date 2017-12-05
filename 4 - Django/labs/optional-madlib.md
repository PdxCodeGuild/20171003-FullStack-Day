
# Optional: Mad Lib

Let's make an app for users to create Mad Libs and also fill them out and view the result. You may want to fill out a Mad Lib with the values the user entered using Django's [template.render](https://docs.djangoproject.com/en/2.0/ref/templates/api/#django.template.Template.render) function.

### Pages
- list Mad Lib 'templates'
- view/edit a template: add/remove word types, change order
- enter the nouns/verbs/etc for a given Mad Lib 'template'
- view the filled-in Mad Lib

### Models
- MadLib
    - title
- MadLibWord
    - MadLib (many-to-one)
    - WordType (verb)
