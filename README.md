# Movie Recommendation System 🎬

Ever watched a movie and liked it so much that you wanted to watch similar ones?  
This **Movie Recommendation System** recommends movies from a dataset of **5000+ movies** based on content similarity using NLP and machine learning techniques.

---

## 📋 About This Project

This is a **content-based movie recommendation system** that analyzes movie features and suggests similar movies based on genres, keywords, cast, crew, and plot overview. The system uses Natural Language Processing (NLP) techniques to understand movie characteristics and find the best matches for your preferences.

---

## 🤖 Machine Learning Model

### Algorithm: Content-Based Filtering with NLP

**Core Technique:** Cosine Similarity with CountVectorizer

The system uses the following approach:

1. **Feature Engineering**
   - Extracts key movie features: genres, keywords, cast members (top 3), directors, and plot overview
   - Concatenates all text features into a single combined feature string for each movie

2. **NLP & Text Vectorization** 
   - **CountVectorizer** from scikit-learn converts text features into numerical vectors
   - Creates a term-frequency matrix representing word occurrences across all movies
   - Removes common stop words to focus on meaningful terms

3. **Similarity Calculation**
   - Computes **Cosine Similarity** between all movie vectors
   - Generates a similarity matrix (4809 x 4809) stored in `similarity.pkl`
   - Values range from 0 to 1, where 1 means identical movies

4. **Recommendation Logic**
   - When a user selects a movie, the system retrieves its similarity scores with all other movies
   - Sorts movies by similarity score in descending order
   - Returns the top 8 most similar movies as recommendations

### Why This Approach?

- **Efficient**: Pre-computed similarity matrix enables instant recommendations
- **Scalable**: Works well with the 4809-movie dataset
- **Interpretable**: Easy to understand what drives recommendations
- **Fast**: No real-time computation needed, just matrix lookups

---

## 🔄 How the Recommendation System Works

```
User Input (Movie Selection)
         ↓
    Movie Selected
         ↓
  Retrieve Similarity Scores (from similarity.pkl)
         ↓
  Sort by Similarity (Descending)
         ↓
  Return Top 8 Most Similar Movies
         ↓
  Display with Posters from TMDB API
```

### Step-by-Step Process:

1. **Data Loading**: Movie dataset (4809 movies) loaded from `movie_dict.pkl`
2. **Feature Extraction**: Combined text features from genres, keywords, cast, crew, and overview
3. **Vectorization**: CountVectorizer transforms text into numerical format
4. **Similarity Computation**: Cosine similarity measures how similar movies are
5. **Ranking**: Top 8 most similar movies are ranked and displayed
6. **Poster Fetching**: Movie posters retrieved from TMDB API for visual appeal

---

## 📊 Dataset

- **Source**: TMDB (The Movie Database) 5000 Movies Dataset
- **Size**: 4,809 movies with complete information
- **Features Used**:
  - Genres (e.g., Action, Drama, Comedy)
  - Keywords (e.g., "space war", "adventure")
  - Cast (top 3 actors)
  - Crew (director)
  - Plot Overview
  - Spoken Languages

**Pickle Files** (Pre-computed for efficiency):
- `movie_dict.pkl`: Processed movie data dictionary
- `similarity.pkl`: Pre-computed 4809×4809 cosine similarity matrix

---

## 🛠️ Technologies & Tools

| Technology | Purpose |
|-----------|---------|
| **Python** | Core programming language |
| **scikit-learn** | CountVectorizer, Cosine Similarity calculations |
| **Pandas & NumPy** | Data manipulation and numerical operations |
| **Streamlit** | Interactive web interface for recommendations |
| **Pickle** | Serializing and saving processed data/models |
| **TMDB API** | Fetching movie posters dynamically |
| **Git & Git LFS** | Version control and large file management |
| **GitHub** | Repository hosting |

---

## 💻 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akhatabhowmik/movie-recommendation.git
   cd movie-recommendation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run

**Start the Streamlit app:**
```bash
streamlit run app.py
```

**Then:**
- Open the URL displayed in your terminal (usually `http://localhost:8501`)
- Select a movie from the dropdown menu
- Click the "Recommend" button
- View 8 similar movie recommendations with posters

---

## 🎯 Usage Example

1. Start the app
2. Select **"Avatar"** from the dropdown
3. Click **Recommend**
4. Get suggestions like: *Avatar*, *Guardians of the Galaxy*, *Star Wars: Episode IV*, etc.
5. Each recommendation comes with a movie poster

---

## 🌐 Live Demo

Try the live version here: [Movie Recommendation System](https://movie-recommendation-002.streamlit.app/)

---

## 📁 Project Structure

```
movie-recommendation/
├── app.py                          # Streamlit web app
├── movie recommendation system.ipynb # Jupyter notebook with model training
├── requirements.txt                # Python dependencies
├── movie_dict.pkl                  # Pre-processed movie data
├── similarity.pkl                  # Pre-computed similarity matrix
├── .gitattributes                  # Git LFS configuration
└── README.md                       # This file
```

---

## 📦 Dependencies

- pandas
- numpy
- scikit-learn
- streamlit
- requests

See `requirements.txt` for specific versions.

---

## 💡 How It Learns

The model learns by:
1. **Training Phase** (in Jupyter notebook):
   - Loading and cleaning movie data
   - Extracting and combining text features
   - Applying CountVectorizer to create word-frequency vectors
   - Computing cosine similarity between all movies
   - Saving similarity matrix to `similarity.pkl`

2. **Inference Phase** (in Streamlit app):
   - Loading pre-computed similarity matrix
   - Looking up scores for selected movie
   - Ranking and displaying top 8 matches

---

## 🔍 Model Performance

- **Recommendation Speed**: < 100ms per query (pre-computed similarity)
- **Dataset Size**: 4,809 movies
- **Similarity Matrix**: 4,809 × 4,809 dense matrix
- **Memory Usage**: Pickle files (~260 KB compressed)

---

## 🤝 Contributing

Feel free to:
- Fork the repository
- Improve the recommendation algorithm
- Add new features (user ratings, collaborative filtering)
- Enhance the UI/UX
- Submit pull requests

---

## 🚀 Future Enhancements

- [ ] Hybrid recommendations (combine content + collaborative filtering)
- [ ] User rating-based refinement
- [ ] Genre-specific recommendations
- [ ] Director/Actor popularity weighting
- [ ] Machine Learning model fine-tuning
- [ ] Recommendation explanations

---

## 📄 License

This project is licensed under the MIT License. See LICENSE for details.

---

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Check the project's Discussions tab
- Review the Jupyter notebook for implementation details

---

**Happy movie hunting! 🍿**
