#!/usr/bin/env python
# coding: utf-8

# # Quiz examples
# ## Jupyter-Quiz

# In[1]:


from jupyterquiz import display_quiz

git_path="https://raw.githubusercontent.com/jmshea/jupyterquiz/main/examples/"
display_quiz(git_path+"questions.json")


# In[2]:


def create_multipleChoice_widget(description, options, correct_answer):
    if correct_answer not in options:
        options.append(correct_answer)
    
    correct_answer_index = options.index(correct_answer)
    
    radio_options = [(words, i) for i, words in enumerate(options)]
    alternativ = widgets.RadioButtons(
        options = radio_options,
        description = '',
        disabled = False
    )
    
    description_out = widgets.Output()
    with description_out:
        print(description)
        
    feedback_out = widgets.Output()

    def check_selection(b):
        a = int(alternativ.value)
        if a==correct_answer_index:
            s = '\x1b[6;30;42m' + "Riktig." + '\x1b[0m' +"\n" #green color
        else:
            s = '\x1b[5;30;41m' + "Feil. " + '\x1b[0m' +"\n" #red color
        with feedback_out:
            clear_output()
            print(s)
        return
    
    check = widgets.Button(description="submit")
    check.on_click(check_selection)
    
    
    return widgets.VBox([description_out, alternativ, check, feedback_out])

import ipywidgets as widgets
import sys
from IPython.display import display
from IPython.display import clear_output


# In[3]:


Q1 = create_multipleChoice_widget('blablabla',['apple','banana','pear'],'pear')
Q2 = create_multipleChoice_widget('lalalalal',['cat','dog','mouse'],'dog')
Q3 = create_multipleChoice_widget('jajajajaj',['blue','white','red'],'white')


# In[4]:


Q1


# In[5]:


Q2


# In[ ]:




