brew services start redis
brew services stop redis

python3 -m Logger.mock.main

# 3 steps
sudo systemctl start redis
sudo python3 -m Logger.main
python3 -m Server.app

# addition
sudo python3 -m pip install eventlet