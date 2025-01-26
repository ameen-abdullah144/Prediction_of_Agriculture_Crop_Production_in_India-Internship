# Prediction of Agriculture Crop Production in India

## Context
India, being the second-largest country by population with over 1.3 billion people, heavily relies on agriculture as its primary resource. However, the agricultural sector faces numerous challenges, from crop selection to optimizing cultivation practices. This project aims to address these challenges by leveraging historical data on agriculture production trends in India (2001-2014).

---

## Dataset Overview
The dataset is sourced from [data.gov.in](https://data.gov.in/) and is fully licensed. It contains valuable information about agricultural crop cultivation and production in India.

### **Dataset Details:**
- **Crop:** Name of the crop (string)
- **Variety:** Subsidiary name of the crop (string)
- **State:** Location of crop cultivation/production (string)
- **Quantity:** Number of quintals/hectares (integer)
- **Production:** Production quantity in quintals/tons (integer)
- **Duration in Days:** Number of days required for cultivation
- **Unit:** Unit of measurement (tons/quintals)
- **Cost:** Cost of cultivation and production (integer)
- **Recommended Zone:** Suggested location/state for optimal cultivation (string)

📂 Dataset Link: [Google Drive Dataset](https://drive.google.com/file/d/1zfqvs8-mAO6E0JpgvhBdueNx8Th03pUp/view?usp=sharing)

---

## Features
1. **Crop-Specific Recommendations:**  
   If the user inputs a wrong state for a crop, the system suggests the recommended locations for that crop.
   
2. **State-Specific Recommendations:**  
   Provides a list of crops suitable for the inputted state.

3. **Data Insights:**  
   Helps identify trends and patterns in crop cultivation and production across different states in India.

---

## Inspiration
Agriculture is the backbone of India's economy, yet it faces persistent challenges such as low productivity, unsuitable crop choices, and inadequate planning. This project aims to:
- Solve problems related to crop cultivation and production.
- Provide actionable insights to farmers and policymakers.
- Contribute towards improving agricultural practices in India.

---

## How to Use
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo-name.git
