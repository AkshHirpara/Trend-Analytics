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
#     stopwords = stoplists.gtrends_stop_words
#     remove_words = [word for word in related_queries['query'] if word in stopwords]
#     related_queries = related_queries[~related_queries['query'].isin(remove_words)]
        related_queries = pd.DataFrame.to_dict(related_queries)
        return {"top10": top10}


def main():
    # giving the webpage a title
    st.title("Google Trends")

    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """ 
        <div style ="background-color:yellow;padding:13px"> 
        <h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1> 
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
        a = Trends.google_trends(term= term_name)
        result = st.bar_chart(a)
    st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()
    # def tweet_insights(self, term: str, no_of_tweets: int, max_words: int, min_word_length: int,
#                    remove_words: list) -> dict:
#     """Trending Words and their Frequencies of Appearance from Tweets
#
#     Args:
#         self
#         term: Keyword to be searched.
#         no_of_tweets: Total Tweets to be Scraped.
#         max_words: Maximum Words to be present in Word Cloud.
#         min_word_length: Min Word Length for each word present in Word-Cloud.
#         remove_words: [list] of words to be removed from the Word-Cloud.
#
#     Returns: Dictionary of Top N Keywords Trending on Twitter
#     """
#     customer_key = environ.get('twitter_api_key')
#     customer_secret = environ.get('twitter_api_secret')
#     access_token = environ.get('twitter_access_token')
#     access_secret = environ.get('twitter_access_secret')
#     auth = tweepy.OAuthHandler(customer_key, customer_secret)
#     auth.set_access_token(access_token, access_secret)
#     api = tweepy.API(auth)
#     results = []
#     for tweet in tweepy.Cursor(api.search, q=term, lang='en', geocode="51.509865,-0.118092,1000mi").items(
#             no_of_tweets):
#         results.append(tweet)
#
#     dataset = pd.DataFrame()
#     dataset['tweetText'] = [tweet.text for tweet in results]
#     tweet_text = dataset['tweetText']
#     stoplist = stoplists.tweet_stop_words
#     stop_words = [term, "https", "co", "RT", "that", "new",
#                   "WOW", "SEE", "will", "on", "it", "then", "the"] + list(STOPWORDS) + list(remove_words) + stoplist
#     word_cloud = WordCloud(width=1000, height=500, max_words=max_words, min_word_length=min_word_length,
#                            stopwords=set(stop_words), collocations=False).generate(
#         ''.join(tweet_text))
#     return {"trending_words": word_cloud.words_}
