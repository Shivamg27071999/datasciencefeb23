import streamlit as st
from PIL import Image
image = Image.open('sgpic.jpg')
st.image(image, width=250, )



st.header('Shivam Garg')
st.subheader(':red[_Data Science Intern_]')
st.header('Inter in  :red[_Innomatics Research Lab_]')

st.snow()

container = st.container()
container.write("Willing to work in a challenging position with a growing organization where I can utilize my technical and interpersonal skills to serve the organization and enhanced the same. Proficient Experience in developing WEB application using HTML, CSS, JS, Bootstrap, React JS. Having Good analytical skills and a quick learner")

col1, col2 = st.columns(2)

with col1:
   st.subheader("Assistant (Superintendent Engineer Cum Project Director), (Contract Basis) CPWD Under Ministry of Housing and Urban Affairs")

   txt = st.text_area('Description', '''
    Working within SAP ERP
    Project Monitoring– IIM Sirmaur(...)
    ''')
      
with col2:
   st.subheader("OFFICER, ALLKIND HEALTHCARE")
   txt = st.text_area('Description', '''
    Reviewing records and change requests on completeness, consistency,  relevance, and clarity
    Providing advice to requesting departments regarding GMP matters and GMP compliance(...)
    ''')
 

