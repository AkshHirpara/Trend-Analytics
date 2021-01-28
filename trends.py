import tweepy
import pandas as pd
from pytrends.request import TrendReq
from wordcloud import WordCloud, STOPWORDS
from os import environ
import streamlit as st


class Trends:
#     """ The Trends tab will be used to get details for Search Trends and Social Media Trends Tab. """

    def google_trends(term: str) -> dict:
        """Google Trends Function to know Keyword Trends in Google

        Args:
            term to be searched.

        Returns: Dictionary of Top10 Countries where the searched keyword is famous and Similar Topics relating to
        the Searched Keyword
        """
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=[term])
        region_wise = pytrend.interest_by_region()
        top10 = region_wise.sort_values(by=term, ascending=False).head(10)
#         top10 = pd.DataFrame.to_dict(top10)
        top10 = st.bar_chart(top10)
        related_queries = pytrend.related_queries()
        related_queries = pd.DataFrame(related_queries[term]['rising'].sort_values(by="value", ascending=False))
#         related_queries = st.bar_chart(related_queries)
#     stopwords = stoplists.gtrends_stop_words
#     remove_words = [word for word in related_queries['query'] if word in stopwords]
#     related_queries = related_queries[~related_queries['query'].isin(remove_words)]
#         related_queries = pd.DataFrame.to_dict(related_queries)
        return (top10,related_queries)


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
    
