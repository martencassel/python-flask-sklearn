sudo apt-get -y install virtualenv

virtualenv -p python3 venv
source venv/bin/activate

pip list 

pip freeze > requirements.txt

# pickle 
Traceback (most recent call last):
  File "app.py", line 7, in <module>
    model = pickle.load(open("models/finalized_model.sav", "rb"))
ModuleNotFoundError: No module named 'sklearn'
