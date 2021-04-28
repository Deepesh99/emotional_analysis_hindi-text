import pandas as pd
import numpy as np
import itertools as it
import spacy
from spacy.lang.hi import Hindi
import regex as re
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 
nlp_hi = Hindi()

app = Flask(__name__)

#CORS
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*"
    }
})

#routes    
@app.route('/', methods=['POST'])
def predict():
      
    # get data
    data = request.get_json(force=True)
    sent = data['comment']
    print("sent",type(sent))
    #print(sent)
    res={}
    print("res",type(res))
    af_pre=preprocessing_hi(sent)
    print("af_pre",type(af_pre))
    print(af_pre)
    print("hello")
    res['after']=af_pre
    res['before']=sent
    print("res",type(res))
    return jsonify(res)


def preprocessing_hi(text_hi):
    
    tweet_hi = []
    print("tweet_hi",type(tweet_hi))
    tokenized_text = nlp_hi(text_hi)
    print("tt",type(tokenized_text))
    for token in tokenized_text:
        if(token.text!='\n\n' and not token.is_stop and not token.is_punct and not token.is_space and not token.like_email and not token.is_digit and not token.is_quote and not token.is_alpha and not token.like_url):
              #tweet_hi.append(token.lemma_)
              tweet_hi.append(token)
    print(tweet_hi)
    print(type(tweet_hi[0]))
    sep = ' '
    tweet = sep.join(tweet_hi)
    print("tweet",type(tweet))
    print(tweet)
    
    return tweet
if __name__ == "__main__":
    app.run(port = 5000, debug=True)
