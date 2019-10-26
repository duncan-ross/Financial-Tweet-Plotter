import tweepy 
  
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "7p2IBF0gP4W3HJa7ZcFzloz43" 
consumer_secret = "OQ0KCiISY9QfBOD3D6vnlGCmQCDCx3Pnq8x3xV6fHFc7Ofkaap"
access_key = "2269956405-3QgYwxs4xOyNxLQAFqCVPPtzUq06DaxzX42iiq3"
access_secret = "ZqyWbCtFaGhUYZxWkIr3Y6mhTnHhQGS9yB2l2Koz3CNK2"
  
# Function to extract tweets 
def get_tweets(username): 
          
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted =
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j)  
  
        # Printing the tweets 
        print "\n".join(tmp)
  
  
# Driver code 
if __name__ == '__main__': 
    get_tweets("@realDonaldTrump")  