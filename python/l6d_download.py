import requests,os,time
from datetime import datetime, timedelta

#################################setting#################################
startdate    = datetime(2022, 1, 1)
enddate      = datetime(2022, 12, 31)

#outputpath(optional)
outputpath   = 'l6d/'

#################################setting#################################


url_base = 'https://sys.qzss.go.jp/archives/l6/'


def download_with_retry(url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.content
            else:
                print(f"Error {response.status_code}: {url}")
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
        outputname = f"{yyyy}{doy}.l6"

        print(f"Downloading: {outputname}")
        
        if outputpath==None:
            outputpath=os.getcwd()
        
        os.makedirs(outputpath, exist_ok=True)

        with open(outputpath + '/' + outputname, mode='wb') as f:
            for hour_letter in 'ABCDEFGHIJKLMNOPQRSTUVWX':
                filename = f"{yyyy}{doy}{hour_letter}.l6"
                url = f"{url_base}{yyyy}/{filename}"
                
                content = download_with_retry(url)

                if content:
                    f.write(content)
                else:
                    print(f"Skipped file: {filename}")

        current_date += timedelta(days=1)

print("Download completed.")
