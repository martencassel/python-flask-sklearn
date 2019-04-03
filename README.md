sudo apt-get -y install virtualenv

virtualenv -p python3 venv
source venv/bin/activate

pip list 

git init
echo 'venv' > .gitignore

pip freeze > requirements.txt
