# FAO_Fisheries_Analysis
Built an end-to-end data science pipeline to analyze global fisheries data, generating insights on production trends, regional contributions, and species-level changes using Python and interactive visualizations.

Global Fisheries Data Analysis Dashboard
An interactive data analysis project exploring global fisheries trends from 1950 to 2023 using FAO datasets.
The goal is to identify production patterns, overfishing signals, and sustainability challenges in global aquatic food systems.
________________________________________
Dashboard Preview
(Add your screenshots here — highly recommended)
images/
├── global_trend.png
├── country_comparison.png
├── species_trends.png
├── map_visualization.png
________________________________________
 Features
•	Analyze global fish production trends over 70+ years 
•	Compare fisheries output across countries 
•	Identify declining and emerging species 
•	Detect signs of overfishing and ecological limits 
•	Visualize data using Matplotlib and Plotly 
•	Perform decade-wise statistical comparisons 
________________________________________
Dataset
•	Source: FAO FishStatJ (Global Capture Production) 
•	Time Span: 1950 – 2023 
•	Samples: 1M+ records 
•	Coverage: 
o	275 countries 
o	13,000+ species 
________________________________________ Methodology
•	Data collection from multiple FAO databases 
•	Data cleaning and filtering (official records only) 
•	Normalization across species, regions, and time 
•	Exploratory Data Analysis (EDA) 
•	Decadal production comparisons 
•	Visualization and trend analysis 
________________________________________
 Key Insights
•	Global fish production increased from 20 million tonnes (1950) to a peak of 96 million tonnes (1996) 
•	Production has since plateaued (~75–80 million tonnes by 2023), suggesting ecological limits 
•	Fisheries production is highly concentrated in a few countries:
China, Indonesia, India, Vietnam 
•	Declining species: Atlantic cod, herring 
•	Growing species: tuna, crustaceans 
•	Evidence of “fishing down the food web” 
•	Increasing dependence of fisheries on environmental and climate factors 
________________________________________
 Visualizations
•	Global production trend graph 
•	Country-wise production comparison 
•	Species-level trend analysis 
•	Regional production maps 
•	Growth vs decline comparison charts 
________________________________________
 Technologies Used
•	Python 
•	Pandas 
•	NumPy 
•	Matplotlib 
•	Plotly 
________________________________________
 Project Structure
fisheries-analysis/
│── data/              # Raw and processed datasets
│── notebooks/         # Jupyter notebooks for analysis
│── src/               # Source code
│── images/            # Graphs and visual outputs
│── main.py            # Main execution script
│── requirements.txt   # Dependencies
________________________________________
 Installation
git clone https://github.com/your-username/fisheries-analysis.git
cd fisheries-analysis

pip install -r requirements.txt
________________________________________
 Usage
Run the main script:
python main.py
Or explore step-by-step analysis:
jupyter notebook
________________________________________
 Future Work
•	Extend analysis to regional fisheries (e.g., Red Sea) 
•	Integrate coral reef ecosystem data 
•	Apply geospatial visualization techniques 
•	Incorporate climate-related variables 
________________________________________
License
This project is licensed under the MIT License.
________________________________________
Contribution
Contributions are welcome!
Feel free to fork the repository and submit a pull request.
TERMS OF USE/LICENSE:
--------------------
https://www.fao.org/contact-us/terms/db-terms-of-use/en

As stated in Article 1 of its Constitution, the Food and Agriculture Organization of the United Nations (“FAO”) “shall collect, analyse, interpret, 
and disseminate information related to nutrition, food, and agriculture”. In this regard, FAO creates and maintains corporate statistical databases on topics 
related to its mandate and encourages their use for statistical, scientific, research and evidence-based decision-making purposes. Accordingly, all FAO corporate 
statistical databases provide datasets free of charge, in machine-readable format on FAO’s corporate website. They are subject to the Statistical Database terms 
of use of this agreement (“Database terms”) and the Terms and Conditions regarding the Reuse of Web content (https://www.fao.org/contact-us/terms/en), 
which are incorporated herein by reference.

FAO encourages you to use datasets contained in FAO corporate statistical databases for research, statistical, scientific and evidence-based decision-making purposes. 
You may access, download, create copies, adapt and re-disseminate datasets subject to these Database terms. Unless specified otherwise in their metadata or webpage, 
all datasets disseminated through FAO corporate statistical databases (see examples in Annex 1) are licensed under the Creative Commons Attribution-4.0 International 
licence (CC BY 4.0) available here as complemented by the Terms of Use outlined below. In other words, when you access, download, or otherwise extract any data or 
datasets from these databases, you agree to comply with the terms and conditions of the CC BY 4.0 licence and all terms specified in the additional terms of use outlined below.
https://creativecommons.org/licenses/by/4.0/legalcode.en


COPYRIGHT & DISCLAIMER CLAUSES
-----------------------------
All requests for translation and adaptation rights, and for resale and other commercial use rights should be made via www.fao.org/contact-us/licence-request or addressed to copyright@fao.org.

The designations employed and the presentation of material in this information product do not imply the expression of any opinion whatsoever on the part of the Food and Agriculture Organization of the United Nations (FAO) concerning the legal or development status of any country, territory, city or area or of its authorities, or concerning the delimitation of its frontiers or boundaries. The mention of specific companies or products of manufacturers, whether or not these have been patented, does not imply that these have been endorsed or recommended by FAO in preference to others of a similar nature that are not mentioned.

FAO declines all responsibility for errors or deficiencies in the database or software or in the documentation accompanying it, for program maintenance and upgrading as well as for any damage that may arise from them. FAO also declines any responsibility for updating the data and assumes no responsibility for errors and omissions in the data provided. Users are, however, kindly asked to report any errors or deficiencies in this product to FAO.
The word "countries" appearing in the text refers to countries, territories and areas without distinction. 
The designations employed and the presentation of material in the map(s) do not imply the expression of any opinion whatsoever on the part of FAO concerning the legal or constitutional status of any country, territory or sea area, or concerning the delimitation of frontiers.

For comments, views and suggestions relating to this data, please email to:
Email: Fish-Statistics-Inquiries@fao.org

(c) FAO 2025

 Contact / Credits
Author: Arika Raza
Dataset provided by FAO (Food and Agriculture Organization of the United Nations)
