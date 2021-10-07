# Kill running bot
kill $(ps aux | grep '[p]ython' | awk '{print $2}')
# Get latest code
git pull
# Start the bot
python3 main.py >> ./log.txt &