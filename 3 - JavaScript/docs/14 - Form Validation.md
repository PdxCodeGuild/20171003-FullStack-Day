
# Form Validation

There are two ways of doing form validation. You can either take complete control by using regular expressions in JavaScript, or you can rely on HTML5's `pattern` attribute.

## REGEX in JavaScript

```html
<input id="username_input" type="text"/>
<span id='username_info' style="display:none;color:red;">username must be between 1 and 15 lowercase characters</span>
<script>
    let username_input = document.querySelector('#username_input');
    let username_info = document.querySelector('#username_info');
    
    // this event is triggered whenever the value in the input field is changed
    username_input.oninput = function() {
        
      // define a regex pattern
      let pattern = /^[a-z]{1,15}$/;
      
      // if the pattern doesn't the input value, indicate the error
      if (!pattern.test(this.value)) {
        this.style.outline = '1px solid red';
        username_info.style.display = 'inline';
      } else {
        this.style.outline = '1px solid black';
        username_info.style.display = 'none';
      }
    }
</script>
```


## The Pattern Attribute

HTML5 brought the `pattern` attribute, which enables you to do validation entirely within HTML. You only have to enter a regular expression into the `pattern` attribute. You can also add a `required` attribute to ensure that the field is filled. If the form is submitted and the given input doesn't match the pattern, a message will pop up containing the text in the `title` attribute.

```html
<form>
  <input type="text" pattern="[a-z]{1,15}" title="username must be between 1 and 15 characters, all lowercase" required/>
  <button type="submit">submit</button>
</form>
```