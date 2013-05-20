NUS-Bidding-History
===================
A place to scrape and host the data scraped from NUS CORS Archive


##Data Format##
* NUS Bidding Activity (12 columns, 77944 entries/rows)
  - Bid_status {'S':'Successful', 'U':'Unsuccessful'}
  - Student_Type {'R':'Returning', 'N':'New', 'NA':null}
  - Account {'G':'General', 'P':'Programme', 'NA':null}
* NUS Bidding Summary (12 columns, 175383 entries/rows)


##Instructions## (for UNIX users):

0) Create the following directories:
    $ mkdir links
    $ mkdir Bidding_Activity
    $ mkdir Bidding_Summary

1) To retrieve the links to all the bidding summaries & activities:
    $ python scripts/extract_archive_links.py > links/archive_links.txt
    $ python scripts/extract_bidding_links.py > links/bidding_links.txt

2) To retrieve the html files corresponding to the links in each files
    $ mkdir Bidding_Activity
    $ mkdir Bidding_Summary

3) Copy the list of links into their corresponding folders:
    $ cp links/bidding_links.txt Bidding_Activity/bidding_links.txt
    $ cp links/archive_links.txt Bidding_Summary/archive_links.txt

4) Download all the html files
    $ cd Bidding_Activity
    Bidding_Activity]$ wget -i bidding_links.txt
    Bidding_Activity]$ cd ../Bidding_Summary
    Bidding_Summary]$ wget -i archive_links.txt

5) Cleaning up...
    Bidding_Summary]$ cd .. # return to parent directory
    $ rm Bidding_Activity/bidding_links.txt
    $ rm Bidding_Summary/archive_links.txt

6) Parse the html
    $ python scripts/scrape_bids_from_html.py > bidding_activity.csv
    $ python scripts/scrape_summary_from_html.py > bidding_summary.csv

7) And now, we work with pandas (in ipython) *code available in /tutorials
see the following tutorials for details:
* [Cleaning NUS Bidding Summary](http://nbviewer.ipython.org/5611329)
* [Cleaning NUS Bidding Activity](http://nbviewer.ipython.org/5611582)


##Folder Structure:##
* Bidding_Activity *[hidden]*
  - html files containing the bidding activities for each module
  - original/unprocessed bidding_activity.csv
* Bidding_Summary *[hidden]*
  - html files containing the bidding summaries for each semester
  - original/unprocessed bidding_summary.csv
* links
  - archive_links.txt # links to the bidding summaries
  - bidding_links.txt # links to the bidding activities
* scripts
  - for pulling the list of links from CORS
  - for scraping the data from the html files
* tutorials
  - for storing the ipython notebooks and code
* log (from wget, when fetching the html files)
* nus_bidding_activity.csv
* nus_bidding_summary.csv
* README.md (current file)