import psycopg2
import random
conn = psycopg2.connect("dbname=voordeelshop user=postgres password= D@t@b@s3!")
cur = conn.cursor()
count = 0
def content_recommend(profile_id):
    global count
    count += 1
    # retrieve previously viewed products
    cur.execute(f"""
    SELECT * FROM profiles_previously_viewed
    WHERE profid = '{profile_id}'
    """)
    viewed_prod = cur.fetchall()
    conn.commit()
    # choose a random viewed product
    rndm_prod = random.choice(viewed_prod)
    # take de categories from the product
    cur.execute(f"""
    SELECT id, category, subcategory, subsubcategory FROM products
    WHERE id='{rndm_prod[1]}'
    """)
    prod = cur.fetchall()
    # checkt eerst op subsubcat dan subcat dan cat om een random recommended product te geven
    if prod[0][3] != None:
        cur.execute(f"""
        SELECT id, name, brand, sellingprice FROM products
        WHERE subsubcategory='{prod[0][3]}'
        """)
        recommended_prod= random.choice(cur.fetchall())
    elif prod[0][2] != None:
        cur.execute(f"""
        SELECT id, name, brand, sellingprice FROM products
        WHERE subcategory='{prod[0][2]}'
        """)
        recommended_prod= random.choice(cur.fetchall())
    elif prod[0][1] != None:
        cur.execute(f"""
        SELECT id, name, brand ,sellingprice FROM products
        WHERE category='{prod[0][1]}'
        """)
        recommended_prod= random.choice(cur.fetchall())
    elif count < 5:
        content_recommend(profile_id)
    else:
        cur.execute("""
        select * from products
        """)
        recommended_prod= random.choice(cur.fetchall)
    return recommended_prod

def freq(lst):
    freq = {}
    for item in lst:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

def max_keyvalue(d):
     # creates a list with all the values and keys of the dict and returns the key with the max value
     value, key = list(d.values()), list(d.keys())
     return key[value.index(max(value))]

def creating_most_common(profile_id):
    targetaudience_lst, type_lst = [], []
    cur.execute(f"""
    SELECT * FROM profiles_previously_viewed
    WHERE profid='{profile_id}'
    """)
    viewed_prod = cur.fetchall()
    for i in range(0, len(viewed_prod)):
        cur.execute(f"""
        SELECT type, targetaudience FROM products
        WHERE id='{viewed_prod[i][1]}'
        """)
        prod = cur.fetchall()
        type_lst.append(prod[0][0])
        targetaudience_lst.append(prod[0][1])
    dict1, dict2 = freq(type_lst), freq(targetaudience_lst)
    return max_keyvalue(dict1), max_keyvalue(dict2)
def create_similar_table():
    cur.execute("""
    CREATE TABLE similar_profiles(
    id varchar(255) NOT NULL UNIQUE,
    type varchar(255) NOT NULL,
    targetaudience varchar(255) NOT NULL,
    PRIMARY KEY (id))
    """)
    conn.commit()
def insert_sim_table(x_limit):
    cur.execute(f"""
    SELECT DISTINCT profid from profiles_previously_viewed
    LIMIT {x_limit}
    """)
    x = cur.fetchall()
    for i in range(0, len(x)):
        y = creating_most_common(x[i][0])
        y1 = list(y)
        if y1[1] == "Baby's":
            y1[1]= 'Babies'
        elif y1[0] == "Auto's":
            y1[0]= 'Autos'
        cur.execute(f"""
        INSERT INTO similar_profiles (id, type, targetaudience)
        VALUES ('{x[i][0]}','{y1[0]}','{y1[1]}')
        """)
        conn.commit()
# insert_sim_table(100)
# insert_sim_table(1000) # ong 2 min om in te laden
def collaborative_recommendations(profile_id):
    user = creating_most_common(profile_id)
    user1 = list(user)
    if user1[1] == "Baby's":
        user1[1] = 'Babies'
    elif user1[0] == "Auto's":
        user1[0] = 'Autos'
    cur.execute(f"""
    SELECT * FROM similar_profiles WHERE type='{user1[0]}' and targetaudience='{user1[1]}'
    """)
    x = cur.fetchall()
    for i in range(0, len(x)):
        if x[i][0] != profile_id:
            continue
        else:
            cur.execute(f"""
            SELECT prodid from profiles_previously_viewed
            WHERE profid='{profile_id}'
            Limit 1
            """)
            z = cur.fetchall()
            recommendation = z[0][0]
    cur.execute(f"""
    SELECT id, name, brand, category, sellingprice FROM products
    WHERE id='{recommendation}'
    """)
    recommended = cur.fetchall()
    return recommended[0]
print(collaborative_recommendations(""))
cur.close()
conn.close()