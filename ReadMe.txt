Global Fisheries Data Analysis Dashboard
 Problem Statement
This project will utilize data science tools on the world's fisheries data (1950-2023) to identify trends, detect overfishing warnings, and understand sustainability in aquatic food systems.

 Data
•	Source: FAO FishStatJ (Global Capture Production)
•	Samples: >1M+
•	Timespan: 1950-2023
•	Entities: 275 countries, >13,000 species

 Methods
•	Data collection from several FAO databases
•	Data cleansing and filtration (only official data)
•	Data normalization between species, locations, and time
•	Exploratory data analysis (EDA)
•	Data comparison of production between decades
•	Plotting using Matplotlib & Plotly

 Important Findings & Interpretation
 Global Trend in Production
•	Up from 20 million tonnes (1950) → Peak 96 million tonnes (1996)
•	Peak plateauing at 75-80 million tonnes (2023)
 Indicates that global fisheries have reached ecological capacity

 Country Level Observation
•	High concentration in production
•	Led by China, Indonesia, India, Vietnam
 Demonstrates geopolitical dominance in marine resources

 Species-level Trends
•	Decrease: Atlantic cod, herring
•	Growth: tuna, crustacean
 Illustrates ecosystem reorganization

 Statistical Finding (Primary Research Tool)
Decadal statistical analysis reveals:
•	Main categories decreasing up to -56%
•	Some species growing up to +120%
 This suggests:
•	Overfishing of traditional stocks
•	Evolution towards lower-trophic stocks
 Insights
•	Global fishery resources have stopped increasing
•	Decline in species due to over-exploitation
•	Increase in some species shows "fishing down the food web"
•	Growing dependency of fisheries on climate

Graphs Produced
•	Global production trend graph
•	Comparison of country-wise production
•	Trend line for each species
•	Regional production maps
•	Growth versus decline graphs
 Technologies
•	Python
•	Pandas
•	NumPy
•	Matplotlib
•	Plotly

 Installation
git clone https://github.com/your-username/fisheries-analysis.git
cd fisheries-analysis
pip install pandas numpy matplotlib plotly

 Usage
python main.py
Or open:
jupyter notebook
Then run the analysis notebook step-by-step.

Future Research Directions
•	Apply this approach to Red Sea fisheries
•	Include information about coral reef ecosystems
•	Utilize geospatial mapping techniques

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

