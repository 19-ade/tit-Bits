import requests
from bs4 import BeautifulSoup

def links_generator(r):
    soup = BeautifulSoup(r.content, "html5lib")
    links = soup.find_all('a')
    for i in range(5):
        del links[0]
    url = "https://sanjayvidhyadharan.in"
    pdf_links = [url + link['href'] for link in links if link['href'].endswith('pdf')]
    return pdf_links




def download_pdfs_series(pdf_links):
    for link in pdf_links:

        '''iterate through all links in video_links  
        and download them one by one'''

        # obtain filename by splitting url and getting
        # last string
        file_name = link.split("/")[-1]

        print("Downloading file:%s" % file_name)

        # create response object
        r = requests.get(link, stream=True, verify=False)

        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)


        print("%s downloaded!\n" % file_name)

    print("All pdf downloaded!")
    return


if __name__ == "__main__":
    # getting all video links
    url_big = "https://sanjayvidhyadharan.in/Downloads/Study%20Materils%20for%20Digital%20%20Design%202020/"
    r = requests.get(url_big + "Lecture_notes/")
    r1 = requests.get(url_big + "Lab_Manual/")
    r2 = requests.get(url_big + "Tutorials/")
    tut_links = links_generator(r2)
    lab_links= links_generator(r1)
    lecture_links=links_generator(r)

    # download all videos
    download_pdfs_series(lecture_links)
    download_pdfs_series(lab_links)
    download_pdfs_series(tut_links)
    #print(pdf_links)