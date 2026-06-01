import streamlit as st

def style_background_home():
    st.markdown("""
        <style> 
                .stApp{
                    background:#00B4D8 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:white !important;
                    padding:1rem !important;
                    border-radius:5rem !important;
                }

                .stApp div[data-testid="stColumn"] > div{
                    display:flex !important;
                    flex-direction:column !important;
                    align-items:center !important;
                    justify-content:center !important;
                    text-align:center !important;
                    height:100% !important;
                }
                div[data-testid="stButton"]{
                    display:flex !important;
                    justify-content:center !important;
                }               
        </style>


    """,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown("""
        <style> 
                .stApp{
                background:#CAF0F8 !important;
                }

        </style>


    """,unsafe_allow_html=True)

def style_base_layout():
    st.markdown("""
        <style> 
                /* Hide heading anchor links */
                h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
                    display: none !important;
                }

                /* Alternative selector used by Streamlit */
                .anchor-link {
                    display: none !important;
                }
            @import url('https://fonts.googleapis.com/css2?family=Orelega+One&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100..900;1,100..900&display=swap');

             
            /*Hide top toolbar*/
            #MainMenu,header,footer{
                visibility:hidden;
            }

            .block-container{
                padding-top:1.5rem !important
            }
                
            h1{
                
                font-family: "Orelega One", serif !important;
                font-size:3.5rem  !important;
                line-height:1.1 !important;
                margin-bottom:0 !important;
            }
                
            h2{
                
                font-family: "Orelega One", serif !important;
                font-size:2rem  !important;
                line-height:1.1 !important;
                margin-bottom:0 !important;
                color:black !important;
            }
                    
                
            h3,h4,h5,p{
                
                font-family: "Raleway", sans-serif !important;
                
            }
                
            button[kind="primary"]{
                border-radius: 1.5rem !important; 
                background: #5865F2 !important;
                color:white !important;
                padding:10px 20px !important;
                border: none !important;
                transition:transform 0.25s ease-in-out !important;
            }
                 
            button[kind="secondary"]{
                border-radius: 1.5rem !important; 
                background: #EB459E !important;
                color:white !important;
                padding:10px 20px !important;
                border: none !important;
                transition:transform 0.25s ease-in-out !important;
            }
                
            button[kind="tertiary"]{
                border-radius: 1.5rem !important; 
                background: black !important;
                color:white !important;
                padding:10px 20px !important;
                border: none !important;
                transition:transform 0.25s ease-in-out !important;
            }
            button:hover{
                transform:scale(1.05)
            }
            [data-testid="stImage"] > img {
                margin-left:auto !important;
                margin-right:auto !important;
                display:block !important;
            }
        </style>


    """,unsafe_allow_html=True)