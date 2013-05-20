NUS-Bidding-History
===================
A place to scrape and host the data scraped from NUS CORS Archive

##Data Format##
- NUS Bidding Activity (12 columns, 77944 entries/rows)
  - Bid_status:
    - 'S' for 'Successful'
    - 'U' for 'Unsuccessful'
  - Student_Type
    - 'R' for 'Returning' (Years 2 to 4)
    - 'N' for 'New' (Year 1)
    - 'NA' for not applicable/available
  - Account
    - 'G' for 'General'
    - 'P' for 'Programme'
    - 'NA' for not applicable/available
- NUS Bidding Summary (12 columns, 175383 entries/rows)


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
* instructions (current file)
* log (from wget, when fetching the html files)
* nus_bidding_activity.csv
* nus_bidding_summary.csv