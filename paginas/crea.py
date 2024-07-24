import streamlit.components.v1 as components
import streamlit as st

def inicio():
  st.header("Power BI", divider='green')
  iframe_src ="https://app.powerbi.com/view?r=eyJrIjoiNzVjMDUxMGItY2ExMS00ZDI3LTlhODctNDRhNGFlNjYyZDE0IiwidCI6IjMzMjRhZTE3LTMwMzctNDU0ZS1hODY5LTlmZjExYmYwYzE4MyJ9"
  components.iframe(iframe_src,width=1000, height=600)
  # You can add height and width to the component of course.

if __name__ == "__main__":
  inicio()