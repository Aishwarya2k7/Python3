
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
import requests_with_caching
import json
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")
def get_movies_from_tastedive(s):
    baseurl = "https://tastedive.com/api/similar"
    paramsd = {}
    paramsd['q'] = s
    paramsd['type'] = 'movies'
    paramsd['limit'] = "5"
    m_resp = requests_with_caching.get(baseurl, params = paramsd)
    return m_resp.json()
def extract_movie_titles(s):
    #movies_rep = get_movies_from_tastedive(s)
    movie_dict = s['Similar']['Results']
    lst = [i['Name'] for i in movie_dict]
    return lst
def get_related_titles(lst):
    all_lst = []
    for i in lst:
        returned_lst = extract_movie_titles(get_movies_from_tastedive(i))
        for j in returned_lst:
            if j not in all_lst:
                all_lst.append(j)
    return all_lst

def get_movie_data(s):
    baseurl = "http://www.omdbapi.com/"
    param_d = {"t":s,"r":"json"}
    omdb_resp = requests_with_caching.get(baseurl,params = param_d)
    return omdb_resp.json()
def get_movie_rating(omdb_dict):
    val=0
    s_lst = omdb_dict['Ratings']
  
    for i in range(len(s_lst)):
        if s_lst[i]['Source']=='Rotten Tomatoes':
            rate = s_lst[i]['Value']
           
            val=int(rate.strip('%'))
           
    return val

def get_sorted_recommendations(mlist):
    mlist_rel = get_related_titles(mlist)
    mlist_sorted = {}
    for i in mlist_rel:
        rating = get_movie_rating(get_movie_data(i))
        if i not in mlist_sorted:
            mlist_sorted[i] = rating
    #print(mlist_sorted)
    mlist_sorted = sorted(mlist_sorted.items(),key = lambda x: x[1],reverse=True)
    for i in range(len(mlist_sorted)-1):
        if mlist_sorted[i][1] == mlist_sorted[i+1][1]:
            l = mlist_sorted[i:i+2]
            l = sorted(l, key = lambda x :x[0],reverse=True)
            mlist_sorted[i] = l[0]
            mlist_sorted[i+1] = l[1]
    flst = [x[0] for x in mlist_sorted]
    return flst
    

