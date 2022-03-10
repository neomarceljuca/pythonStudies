import json
import oauth2
import urllib.parse


#Class responsible for contacting Twitter API, post for an account and perform basic search on latest tweets about a topic.
#Requests occur through OAUTH2 using the request method from API.
#Requires 4 propper keys and ELEVATED ACCESS to use the provided endpoints.
class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key,consumer_secret, token_key, token_secret)

#Sets up the Client based on existing keys to reach the API.
#Requires: consumer API key,consumer API secret, token key, token secret
    def conexao(self, consumer_key,consumer_secret, token_key, token_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

#tweet in behalf of the account associated with the token provided at class instantiation
#novo_tweet: string with the content to be posted.
#return: the feedback dictionary provided by API.
    def tweet(self, novo_tweet):
        query_codificada = urllib.parse.quote(novo_tweet, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto
 #Reports latest 15 tweets about a topic provided to 'query' and defined on 2 digit form to 'lang'
#Format: List of dictionaries provided by API.
    def searchFullInfo(self, query, lang):
        query_codificada = urllib.parse.quote(query, safe ='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=' + lang)
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        tweets = objeto['statuses']
        return tweets

#Reports latest 15 tweets about a topic provided to 'query' and defined on 2 digit form to 'lang'
#Format: (Time the tweet as posted, Tweet content, User)
    def searchSummary(self, query, lang):
        minhaPesquisa = self.searchFullInfo(query, lang)
        meuRelatorio = []
        for resultado in minhaPesquisa:
            tweetx = {
                "User": resultado['user']['screen_name'],
               "Tweet": resultado['text'],
               "Posted at:": resultado['created_at']
            }
            meuRelatorio.append(tweetx)
        return meuRelatorio

