
# Optional: Mad Lib

Let's make an app for users to create Mad Libs and also fill them out and view the result.

### Pages
- list 'Mad Lib templates'
- view/edit a template: add/remove word types, change order
- enter the nouns/verbs/etc for a given template
- view the filled-in madlib

### Models
- MadLib
    - title
- MadLibWord
    - MadLib (many-to-one)
    - WordType (verb)
