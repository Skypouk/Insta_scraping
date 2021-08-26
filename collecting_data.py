from dotenv import load_dotenv, find_dotenv
import os

"""
Load predefined environment variables, the variables IG_USERNAME and IG_PASSWORD can be set in a .env file
as follows: 
IG_USERNAME="XXXXXXX"
IG_PASSWORD="XXXXXXX"
"""
load_dotenv(find_dotenv(), verbose=True)

data_dir = r"C:\Users\bentahe\Desktop\insta_scraping\data"
os.system(f"instagram-scraper --filename ig_users.txt --comments --media-types image --destination {data_dir} -u {os.getenv('IG_USERNAME')} -p {os.getenv('IG_PASSWORD')} -m 10")
