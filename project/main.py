from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__) #ijsjjsjsjjsjs Comment 012983019283091823091823098

@main.route('/')
def index():
    return render_template('index.html') #This comment is in the dev branch on my fork, idk if this will create a dev branch on the main repo

# The earlier comment didn't go to a dev branch on the original repo, it was in main. 
# A dev branch has been added to the original repo, so I will push this and see if there is an option in the pull request to merge into dev branch.

# comment 1296102960934602
<<<<<<< Updated upstream
# am i in branch dev?
=======
print("test") # adding to dev then merging with test to see if the github action works
>>>>>>> Stashed changes

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

#comment by ivan