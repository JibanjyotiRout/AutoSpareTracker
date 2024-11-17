# AutoSpareTracker
An Efficient Solution for Supply Chain in the Automobile Industry
Pre-requisites
Python 3.7 or above
Flask
SQLite
Machine Learning libraries:
scikit-learn
pandas
numpy
AutoSpareTracker is a warehouse inventory management system that integrates machine learning (ML) and AI-driven features. This system helps companies efficiently manage their inventory of spare parts, locate items quickly, predict product demand, and interact with a chatbot for additional support.
Maintain all files according this structure

AutoSpareTracker/
├── app.py                       
├── ai_models/                  
│   ├── demand_predictor.pkl     
├── database/                   
│   ├── warehouse.db             
├── templates/                  
│   ├── login.html               
│   ├── dashboard.html           
│   ├── locate_parts.html        
│   ├── demand_products.html     
│   ├── chatbot.html             
├── static/                      
│   ├── css/
│   │   ├── style.css            
│   ├── images/
│   │   ├── login_background.jpg 
│   │   ├── dashboard.jpg        
│   │   ├── locate_parts.jpg     
│   │   ├── demand_products.jpg  
│   │   ├── chatbot.jpg          
├── train_model.py              
├── requirements.txt             
└── README.md                    
