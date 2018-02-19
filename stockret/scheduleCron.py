from crontab import CronTab

my_cron = CronTab(user="Jenna Millin")

for job in my_cron:
    print job

# job = my_cron.new(command='python scrapAmazon.py amazon.html')
# job.day.on(4, 5, "*")
# my_cron.write()
