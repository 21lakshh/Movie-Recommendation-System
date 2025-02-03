# Movie Recommendation System

## Overview
This project is a **Movie Recommendation System** implemented using both **Content-Based Filtering** and **Collaborative Filtering**. The system is deployed as a **Streamlit web application**, utilizing the **TMDB Movies Dataset** for content-based filtering and user-movie rating data for collaborative filtering. The app integrates with the TMDB (The Movie Database) API to fetch the poster paths of recommended movies and display them in the streamlit Web-App.

## Features
- **Content-Based Filtering**: Recommends movies based on textual similarity (genres & overview).
- **Collaborative Filtering**: Uses user-movie rating data to recommend movies based on user preferences.
- **Streamlit Web Application**: Interactive UI for movie recommendations.

---

## Content-Based Filtering Approach
1. **Data Preprocessing**:
   - Uses the **TMDB Movies Dataset**.
   - Removes unnecessary features.
   - Combines `genres` and `overview` to create a new `tags` column.
2. **Text Vectorization**:
   - Converts text data into vectors using **CountVectorizer** (Bag of Words model).
   - Transforms textual data into a **sparse matrix**.
3. **Similarity Computation**:
   - Computes **cosine similarity** between movie vectors to find similar movies.
---

## Collaborative Filtering Approach
1. **User-Movie Interaction Matrix**:
   - Creates a structured matrix between `user_id` and `movie_id` containing **ratings**.
   - Missing values are filled with `0`.
2. **CSR Matrix Representation**:
   - Converts the user-movie matrix into a **Compressed Sparse Row (CSR) matrix** for efficiency.
3. **Model for Recommendation**:
   - Uses **Nearest Neighbors** algorithm to find similar users/movies based on rating patterns.

---

### 1. Clone the Repository
```sh
git clone https://github.com/21lakshh/Movie-Recommendation-System.git
```
---

### 2. Dependencies 
- NumPy: A powerful library in Python for numerical computing, providing support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.

- Streamlit: An open-source app framework used for building interactive and data-driven web applications with minimal effort. It's commonly used for deploying machine learning models and data science tools.

- Pickle: A Python module for serializing (pickling) and deserializing (unpickling) Python objects, allowing you to save and load objects to/from files, which is useful for saving models, datasets, or complex data structures.

- OS: A Python module that provides a way to interact with the operating system, allowing you to perform tasks such as file manipulation, directory operations, and environment variable handling.

- Requests: A simple and easy-to-use Python library for making HTTP requests, commonly used for interacting with APIs and retrieving data from web services.
---
### 3. Run Streamlit Web-App
```sh
streamlit run recommendation.py
```

---
Please download the similarity.sav file through this drive link: 
```sh
https://drive.google.com/file/d/1ROne5iR9kiGrz_qTJjFyhvvmVjHIs04r/view?usp=sharing
```

