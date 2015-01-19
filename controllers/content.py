

def index():
    if not auth.user:
        message = "log in to view content"
    else:
        message = "your content goes here"

    return dict(message = message)

def add():
    
    grid=SQLFORM.smartgrid(db.website, linked_tables=['theme'])
    
    return dict(grid=grid)
