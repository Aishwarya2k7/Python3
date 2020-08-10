
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(wrd):
    for i in punctuation_chars:
        if i in wrd:
            wrd.strip()
            wrd = wrd.replace(i,'')
    return wrd

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(sentences):
    sentences = sentences.lower()
    lst = sentences.split(' ')
    c=0
    for i in lst:
        wrd = strip_punctuation(i)
        if wrd in positive_words:
            c=c+1
    return c


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentences):
    sentences = sentences.lower()
    lst = sentences.split(' ')
    c=0
    for i in lst:
        wrd = strip_punctuation(i)
        if wrd in negative_words:
            c=c+1
    return c
f = open('project_twitter_data.csv','r')
file = open('resulting_data.csv','a')
file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')


for i in f.readlines()[1:]:
    #print(f.read())
    val = i.split(',')
    pos = get_pos(val[0])
    neg = get_neg(val[0])
    tot = pos-neg
    string = '{},{},{},{},{}'.format(val[1].strip(),val[2].strip(),str(pos),str(neg),str(tot))+"\n"
    
    #print(val[1]+','+val[2]+','+str(pos)+','+str(neg)+','+str(tot))
    file.write(string)

f.close()
file.close()
