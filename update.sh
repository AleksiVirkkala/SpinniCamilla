# Kill running bot
kill $(ps aux | grep '[p]ython' | awk '{print $2}')
# Get latest code
git pull

# Add separation and date to different runs
echo "" >> ./log.txt
echo "----------" >> ./log.txt
date >> ./log.txt
echo "----------" >> ./log.txt
echo "" >> ./log.txt


# Start the bot
python3 -u main.py >> ./log.txt &