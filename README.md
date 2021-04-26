# chatbot
Repository containing code for LSTM-based chatbot that generates HTML and CSS code

# Roadmap to implementation
We can split the implementation into 3 parts:  
1. Create and format the data  
2. Train and save the model  
3. Use the model while chatting  

*Notes:*  
Maybe we should consider creating two models, one for chatting and one for generating appropriate items  
We should come up with a way of referencing a specific element in a web page and applying changes to it


# Suggestions to improve the project  
1. Should this be an entire web application or just a console app?  
2. Make a web scraper -> Scrape w3schools page -> train the model with this data -> check the results  
3. Research and improve the current neural network architecture  
4. Should we represent the web page that is being generated as an in-memory tree or as a .txt file or a string from which we will read and write?  
