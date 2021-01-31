def main():
    # giving the webpage a title
    st.title("Google Trends")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """ 
        <div style ="background-color:black;padding:13px"> 
        <h1 style ="color:white;text-align:center;">Top 10 Countries </h1> 
        </div> 
        """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html=True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    term_name = st.text_input("Term", "Type Here")
    result = ""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Search"):
        results = Trends.google_trends(term= term_name)
    st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()
    
