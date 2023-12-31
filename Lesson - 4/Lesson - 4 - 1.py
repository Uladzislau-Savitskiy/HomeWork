bucket_3l_list = [" ", " ", " "]
bucket_5l_list = [" ", " ", " ", " ", " "]
clear = "\b"*10000
front = """

    3l             5l
              _____________
              \{7}{7}{7}{7}{7}{7}{7}{7}{7}{7}{7}/
_________      \{6}{6}{6}{6}{6}{6}{6}{6}{6}/
\{2}{2}{2}{2}{2}{2}{2}/       \{5}{5}{5}{5}{5}{5}{5}/
 \{1}{1}{1}{1}{1}/         \{4}{4}{4}{4}{4}/
  \{0}{0}{0}/           \{3}{3}{3}/
   ¯¯¯             ¯¯¯
"""

# database ------------------------------------------
database = {
    'bucket_3l': 0,
    'bucket_5l': 0,
}

# backend -------------------------------------------
working = True

while working:



    # --------------------------------------------------------------
    bucket_3l_list = (["@"] * database['bucket_3l'] + [" "] * 3)[:3]
    bucket_5l_list = (["@"] * database['bucket_5l'] + [" "] * 5)[:5]
    print(front.format(*(bucket_3l_list[:4] + bucket_5l_list)))
    if  database['bucket_5l'] == 4:
        print("You WIN")
        break
    cmd = input(">> ")
    # --------------------------------------------------------------



    if cmd == "fill_3l":
        database['bucket_3l'] = 3

    elif cmd == "fill_5l":
        database['bucket_5l'] = 5

    elif cmd == "pour_5l":
        database['bucket_5l'] = 0

    elif cmd == "pour_3l":
        database['bucket_3l'] = 0

    elif cmd == "pour_from_5_to_3":
        if database['bucket_5l'] == 0 or database['bucket_3l'] == 3:
            database['bucket_3l'] += 0
            database['bucket_5l'] += 0
        amount_to_pour = min(database['bucket_5l'], 3 - database['bucket_3l'])
        database['bucket_5l'] -= amount_to_pour
        database['bucket_3l'] += amount_to_pour
    elif cmd == "pour_from_3_to_5":
        if database['bucket_3l'] == 0 or database['bucket_5l'] == 3:
            database['bucket_3l'] += 0
            database['bucket_5l'] += 0
        amount_to_pour = min(database['bucket_3l'], 5 - database['bucket_5l'])
        database['bucket_5l'] += amount_to_pour
        database['bucket_3l'] -= amount_to_pour
    print(clear)