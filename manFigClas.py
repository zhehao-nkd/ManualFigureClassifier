
import streamlit as st
from PIL import Image
import numpy as np
import pandas


class struct(): # matlab-like non-scalar struct 
    def __init__(self,**kwargs):
        self.Set(**kwargs)
    def Set(self,**kwargs):
        self.__dict__.update(kwargs)
    def SetAttr(self,lab,val):
        self.__dict__[lab] = val

def increment_counter(): # function to update the catego state
    st.session_state.catego += 1
    #print(st.session_state.catego)

def hash_struct(struct_input):
    catego = struct_input.catego
    return catego


def celebrateSuccess():
  try:
    st.balloons()
  except:
    st.warning("Error while downloading, please try again later.")

@st.cache(hash_funcs={struct:hash_struct})
def convert_df(figinfo):
  # IMPORTANT: Cache the conversion to prevent computation on every rerun
  namelist = [ eachstruct.name for eachstruct in figinfo]
  categolist = [ eachstruct.catego for eachstruct in figinfo]
  commentlist = [ eachstruct.comment for eachstruct in figinfo]
  df = pandas.DataFrame(data={"name": namelist, "catego": categolist,"comment": commentlist})
  df.to_csv("./file.csv", sep=',',index=False)
  return df.to_csv().encode('utf-8')




if 'catego' not in st.session_state: # initiation of the catego state
  st.session_state.catego = 0


files = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"],accept_multiple_files=True)


if not files:
    print('Not started yet!!')
    quit()

st.title("Now the category is : {}".format(st.session_state.catego+1)) # Title to specify current category 
comment = st.text_input('Category description:', '') # Comment will be refreshed at evey run
st.write('The current category is', comment)

with st.form("my_form"):  # take all the widgets into the form 控件

 # Only when files is not empty
  c1, c2, c3,c4,c5 = st.columns(5)
  
  if 'figinfo' not in st.session_state:
    st.session_state.figinfo = [ i for i, file in enumerate(files)] 

  for index,file in enumerate(files): #.head()

    
    if index%5 == 0:
      #breakpoint()
      if not hasattr(st.session_state.figinfo[index],'name'):
        st.session_state.figinfo[index] = struct(placeholder = c1.empty(),name = file.name,catego = 0,comment = '')
      with st.session_state.figinfo[index].placeholder.container():
        image = Image.open(file)
        st.image(image)
        s = st.checkbox(st.session_state.figinfo[index].name,key = st.session_state.figinfo[index].name ) 
      if s: 
        st.session_state.figinfo[index].placeholder.empty()
        if st.session_state.figinfo[index].catego ==0: # 0 是未编辑的状态，一旦不是零，说明已经被编辑过，不应该被再次赋值
          st.session_state.figinfo[index].catego = st.session_state.catego
          print(st.session_state.catego)
        if not st.session_state.figinfo[index].comment:
          st.session_state.figinfo[index].comment = comment

    if index%5 == 1:
      #breakpoint()
      if not hasattr(st.session_state.figinfo[index],'name'):
        st.session_state.figinfo[index] = struct(placeholder = c2.empty(),name = file.name,catego = 0,comment = '')
      with st.session_state.figinfo[index].placeholder.container():
        image = Image.open(file)
        st.image(image)
        s = st.checkbox(st.session_state.figinfo[index].name,key = st.session_state.figinfo[index].name ) 
      if s:
        st.session_state.figinfo[index].placeholder.empty()
        if st.session_state.figinfo[index].catego ==0: # 0 是未编辑的状态，一旦不是零，说明已经被编辑过，不应该被再次赋值
          st.session_state.figinfo[index].catego = st.session_state.catego
          print(st.session_state.catego)
        if not st.session_state.figinfo[index].comment:
          st.session_state.figinfo[index].comment = comment

    if index%5 == 2:
      #breakpoint()
      if not hasattr(st.session_state.figinfo[index],'name'):
        st.session_state.figinfo[index] = struct(placeholder = c3.empty(),name = file.name,catego = 0,comment = '')
      with st.session_state.figinfo[index].placeholder.container():
        image = Image.open(file)
        st.image(image)
        s = st.checkbox(st.session_state.figinfo[index].name,key = st.session_state.figinfo[index].name ) 
      if s: 
        st.session_state.figinfo[index].placeholder.empty()
        if st.session_state.figinfo[index].catego ==0: # 0 是未编辑的状态，一旦不是零，说明已经被编辑过，不应该被再次赋值
          st.session_state.figinfo[index].catego = st.session_state.catego
          print(st.session_state.catego)
        if not st.session_state.figinfo[index].comment:
          st.session_state.figinfo[index].comment = comment

    if index%5 == 3:
      #breakpoint()
      if not hasattr(st.session_state.figinfo[index],'name'):
        st.session_state.figinfo[index] = struct(placeholder = c4.empty(),name = file.name,catego = 0,comment = '')
      with st.session_state.figinfo[index].placeholder.container():
        image = Image.open(file)
        st.image(image)
        s = st.checkbox(st.session_state.figinfo[index].name,key = st.session_state.figinfo[index].name ) 
      if s: 
        st.session_state.figinfo[index].placeholder.empty()
        if st.session_state.figinfo[index].catego ==0: # 0 是未编辑的状态，一旦不是零，说明已经被编辑过，不应该被再次赋值
          st.session_state.figinfo[index].catego = st.session_state.catego
          print(st.session_state.catego)
        if not st.session_state.figinfo[index].comment:
          st.session_state.figinfo[index].comment = comment

    if index%5 == 4:
      #breakpoint()
      if not hasattr(st.session_state.figinfo[index],'name'):
        st.session_state.figinfo[index] = struct(placeholder = c5.empty(),name = file.name,catego = 0,comment = '')
      with st.session_state.figinfo[index].placeholder.container():
        image = Image.open(file)
        st.image(image)
        s = st.checkbox(st.session_state.figinfo[index].name,key = st.session_state.figinfo[index].name ) 
      if s: 
        st.session_state.figinfo[index].placeholder.empty()
        if st.session_state.figinfo[index].catego ==0: # 0 是未编辑的状态，一旦不是零，说明已经被编辑过，不应该被再次赋值
          st.session_state.figinfo[index].catego = st.session_state.catego
          print(st.session_state.catego)
        if not st.session_state.figinfo[index].comment:
          st.session_state.figinfo[index].comment = comment

  print('已经初始化')
  st.form_submit_button("Submit",on_click=increment_counter)
  #breakpoint() 
  csv = convert_df(st.session_state.figinfo)


downloadstate = st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

if downloadstate:
  st.balloons()
  st.success('This is a success message!')







  