'''
TODO:
    # define tables: 
        -Website/URL
        -Organization
        -Google Docs? 
        -??

    # add some default content to tables
'''


## add some default user data 
if db(db.auth_user).isempty():
    import datetime
    from gluon.contrib.populate import populate

'''
    temp_user_id = db.auth_user.insert(first_name='Michael', last_name'Scotch',
                                       email='ntgroos@gmail.com',
                                       password=CRYPT()('password')[0])
'''


def get_websites(user_id=auth.user_id, org_id=None):
                query = (db.website.entered_by == user_id)
                
                if org_id:
                    query += db.website.org == org_id
                
                return db(query).select(db.website.ALL)
