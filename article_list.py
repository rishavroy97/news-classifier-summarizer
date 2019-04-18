'''import cPickle as pickle #data preprocessing
from collections import Counter #tokenization
import keras #ML
import utils
import conv_utils
import backend as K
import tensorflow as tf
import postprocessing as pr #helper

#Step 1 - Load data
with open('data/%s.pkl','rb') as fp:
    heads, desc, keywords = pickle.load(fp)

#headings
i=0
heads[i]

#Articles
desc[i]


#Tokenize text
def get_vocab(lst):
    vocabcount, vocab = Counter(w for txt in lst for w in txt.split())
    return vocab, vocabcount

vocab, vocabcount = get_vocab(head+desc)

print vocab[:50]
print '....' , len(vocab)

#Create word embeddings with GloVe
path = 'glove.6B.zip'
glove_weights = get_glove_weights(path, origin="http://nlp.stanford.edu/data/glove.6B.zip")
word_embeddings = pr.build_glove_matrix(glove_weights, vocab)

#3stacked LSTM RNN
def build_model(embedding):
    model = Sequential()
    model.add(Embedding(weights=[embedding], name='embedding_1'))
    for i in range(3):
        lstm = LSTM(rnn_size,name='lstm_%d'%(i+1))
        model.add(lstm)
        model.add(Dropout(p_dense,name='dropout_%d'%(i+1)))
    model.add(Dense())
    model.add(Activation('softmax', name='activation'))
    return model

#Initialize Encoder RNN with Embeddings
encoder = biuld_model(embedding)
encoder.compile(loss='categorical_crossentropy',optimizer'rmsprop')
encoder.save_weights('embeddings.pkl', overwrite=True)

#Initialize Decoder RNN with Embeddigs
with open('embeddings.pkl', 'rb')
    embeddings = pickle.load(fp)
decoder = build_model(embeddings)

#Convert a given article to a headline
headline1 = pr.gen_headline(decoder, desc[1])

#Convert a given article to a headline
headline2 = pr.gen_headline(decoder, desc[2])
'''

text=[
"There were raucous celebrations around the 18th green as Woods finished with a two-under-par 70 to win on 13 under, one clear of fellow Americans Dustin Johnson, Xander Schauffele and Brooks Koepka. Woods, written off by so many so often as he battled back problems in recent years, punched the air in delight, a wide smile across his face, before celebrating with his children at the back of the green." ,

" Almost five years since Liverpool title chance's were ruined by a 2-0 defeat in the same fixture, the hosts kept themselves in the hunt for a first league title in 29 years with two goals in the space of two minutes that saw Anfield erupt. After a nervy first half in which both sides had chances, Liverpool emerged from the break with added purpose and took the lead via Sadio Manes header.There was a huge sense of relief inside the ground, but that became a deafening roar when Salah smashed a left-footed angled drive into the top right corner from 25 yards for his 19th Premier League goal of the season ",

"The Mercedes driver passed team-mate Valtteri Bottas, who started from pole position, off the line and controlled Formula 1's 1,000th race from there. Ferrari's Sebastian Vettel took third, after the team ordered team-mate Charles Leclerc to let him by in the opening laps. The decision led to Leclerc losing fourth place to Max Verstappen's Red Bull. Ferrari will face questions about the wisdom of their approach to the race - and to team orders in general - but Hamilton was serenely distant from such concerns. After taking the lead, Hamilton edged away from Bottas, building a five-second lead before his first pit stop on lap 22. Mercedes' decision to bring Bottas in first to protect from Vettel behind dropped the lead to less than two seconds, but Hamilton soon pulled away again to take his second victory in a row",

"Guava Island: Fans respond to Donald Glover and Rihanna's new film . Donald Glover and Rihanna's short film was made during a hush-hush shoot in Cuba and premiered at Coachella. For those who weren't at the Californian music festival, it was then released on Amazon Prime. The movie stars Donald Glover as Deni Maroon - a musician who wants to put on a festival for the people of Guava. Rihanna plays his long-term girlfriend, Kofi.",

"The Rise of Skywalker: Star Wars Episode IX title revealed . The title was revealed at a Star Wars celebration event in Chicago, while a teaser trailer was posted on Twitter with the words: 'Every generation has a legend.' Director JJ Abrams said the movie is set some time after previous instalment The Last Jedi. The Rise of Skywalker is due to be released later this year. Despite his apparent death at the end of Episode VI, Return of the Jedi, Emperor Palpatine seems to be making a comeback. His sinister cackle is heard at the end of the trailer and Ian McDiarmid, who plays the character, strolled on stage to loud applause at the announcement.",

"Everything about Uber is big. The taxi app and delivery business is America's biggest venture capital-backed company. It is forecast to raise $10bn ($7.6bn) when it sells its shares on the New York Stock Exchange - one of the largest amounts on record. And the 10-year-old company could be valued at as much as $100bn when it floats. However, the other big thing about Uber is its losses which, although down on the previous year, hit $3bn in 2018. And that raises the biggest point of all - when will Uber make a profit and perhaps justify that massive market valuation? It is the question that Uber's chief executive, Dara Khosrowshahi, will face over the next few weeks as he embarks on a roadshow to visit potential investors ahead of the flotation, which is expected in May. ",

"Chinese stocks rebounded from their worst week of the year amid signs an economic recovery was firming, with large caps climbing and the country’s offshore equities poised to enter a bull market. Sovereign bonds fell. The SSE (LON:SSE) 50 Index of some of China’s biggest stocks rose 2.2 percent as of 9:56 a.m. in Shanghai. New China Life Insurance Co. climbed 5.9 percent, in line for the biggest gain since Feb. 25, as insurers and banks advanced. The Hang Seng China Enterprises Index advanced 1.7 percent to extend its gain from a low in early January to 20 percent. Investors were content to take profits last week from the best-performing stocks in the world in 2019. After trading ended for the week, the People’s Bank of China released credit data that suggested growth exceeded all estimates in March. Risk sentiment is also being boosted by signs the U.S. and China are nearing a trade deal after Treasury Secretary Steven Mnuchin said the U.S. is open to facing “repercussions” if it doesn’t live up to its commitments. 'The credit data lifted expectations on market liquidity and economic fundamentals,' said Wang Jianhui, a Beijing-based analyst with Capital Securities Co. 'It provided an excuse for investors who wanted to bottom fish stocks after last week’s correction.' The yield on China’s 10-year government bonds rose 4 basis points to 3.40 percent, the highest since December. The yield has climbed 12 basis points in the past two sessions.",

"Social networks Facebook and Instagram, as well as messaging service WhatsApp, were unavailable on Sunday for more than three hours, users said. The website Down Detector reported that thousands of people globally had complained about the Facebook-owned trio being down from 11.30 BST onwards. Facebook users were presented with the message: 'Something went wrong.' At 14:50, the site said it had resolved the issue after some users 'experienced trouble connecting' to the apps. ",

"North Korean leader Kim Jong Un said he is open to a third summit with President Donald Trump, but set the year’s end as a deadline for Washington to offer mutually acceptable terms for an agreement to salvage the high-stakes nuclear diplomacy, the state-run media said Saturday. Kim made the comments during a speech Friday at a session of the North Korea’s rubber-stamp parliament, which made a slew of personnel changes that bolstered his diplomatic lineup amid stalemated negotiations with the United States. His speech came hours after Trump and visiting South Korean President Moon Jae-in met in Washington and agreed on the importance of nuclear talks with North Korea.",

"The United Nations on Friday urgently appealed for the release and evacuation of more than 1,500 detained refugees and migrants caught in the crossfire of escalating fighting sparked by a self-styled Libyan army commander’s military campaign to take the capital. The U.N. refugee agency said the refugees and migrants are believed to be trapped in detention centers where hostilities are ranging. The oil-rich North African country is now governed by rival administrations _ a U.N.-backed government in the capital Tripoli and the west, and the self-styled Libyan National Army in the east led by Field Marshal Khalifa Hifter who launched the major offensive earlier this month. U.N. spokesman Stephane Dujarric said fighting continued Friday on the outskirts of Tripoli, with reports of increased use of heavy artillery.",

"Today, after months and months of teasing, Samsung unveiled its folding-screen smartphone, the Samsung Galaxy Fold. While its namesake trick is technically impressive, it's also questionably useful. Oh, and it will launch in April at a sky-high price of $1,980 at the very least.  The Samsung device may be on-trend in a world of increasingly glitzy and expensive handsets. But it is bucking conventional wisdom in one good and important way: it is extremely thick. It's just too bad that it's not all battery.  Owing to its folding design, which is basically two phones of typical thickness joined on their longest edge by a hinge of screen, the Fold gets chunky when in compact mode. With a battery in each side, it's essentially two phones stacked on top of each other in closed form.",

"The 2019 Mobile World Congress did not disappoint. MWC (as it’s known) is a major consumer tech event focused on showcasing and introducing the industry’s latest and greatest products. Held in Barcelona, this year’s attention-commanding products were headlined by 5G-compatible hardware and foldable smartphones that can transform into a tablet. The latter included headline-grabbing products from Samsung and Huawei, though you’ll have to be patient if you want to have one of them. The Samsung Galaxy Fold, for example, is weeks away from hitting the shelves.  As expected, MWC 2019 showcased a number of excellent smartphones from today’s leading Android manufacturers. They range from the decidedly premium Samsung Galaxy S10 lineup, all the way to affordably-priced offerings from the likes of Lenovo and Sony, which are bound to push the boundaries of design and performance in their price range. With such ground-breaking tech on display, it can be hard to stand out at MWC. But — from a dual-screen smartphone to a travel-friendly monitor — these gadgets managed to do so, and have us truly amped for their release",

]

import paralleldots

paralleldots.set_api_key("OGNYZsxjhVpVkXqGUGRzp2abSXqk1uFt3upfaVUpZnU")

category = { 
    "finance": [ "markets", "economy", "shares" ], 
    "politics": [ "diplomacy", "UN", "war", "elections" ],
    "sports": ["game", "vs", "ball", "score","championship"],
    "tech": ["engineer", "scientist", "discovery","invention","gadget","technology" ],
    "entertainment": ["hollywood", "movie", "cinema","film"]
}


def create_categorized_list():
    categorized_articles = list()
    for i in range(len(text)) :
        response=paralleldots.custom_classifier(text[i],category)
        categorized_articles.append({
            'article' : text[i],
            'scores' : response
            })
        print("Article no.", i, "completed...")

    print(categorized_articles)

    return categorized_articles

# print(create_categorized_list())