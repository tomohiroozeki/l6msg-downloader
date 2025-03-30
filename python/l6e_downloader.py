import requests,os,time
from datetime import datetime, timedelta


#################################setting#################################

sat = 'J07'

startdate = datetime(2025, 3, 1)
enddate = datetime(2025, 3, 1)

#outputpath(optional)
outputpath   = 'l6e/'

#################################setting#################################

url_base = 'https://l6msg.go.gnss.go.jp/archives/'
satellite_prn_map = {'J02': 204, 'J03': 205, 'J04': 206, 'J05': 207 ,'J07': 209, 'J08': 210,'J09': 211}
prn = satellite_prn_map.get(sat, None)

def download_with_retry(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.content
            else:
                print(f"HTTP Error {response.status_code} at {url}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(delay)
    return None

if __name__ == "__main__":
    current_date = startdate
    while current_date <= enddate:
        doy = current_date.strftime('%j')
        yyyy = current_date.strftime('%Y')
        outputname = f"{yyyy}{doy}.{prn}.l6"

        print(f"Downloading: {outputname}")
        
        if outputpath==None:
            outputpath=os.getcwd()

        os.makedirs(outputpath, exist_ok=True)

        with open(outputpath + '/' + outputname, mode='wb') as f:
            for hour_letter in 'ABCDEFGHIJKLMNOPQRSTUVWX':
                filename = f"{yyyy}{doy}{hour_letter}.{prn}.l6"
                url = f"{url_base}{yyyy}/{doy}/{filename}"
                
                content = download_with_retry(url)
                if content:
                    f.write(content)
                else:
                    print(f"Skipped missing file: {filename}")

        current_date += timedelta(days=1)

print("Download finished.")