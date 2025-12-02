# Football Needs You! ⚽

A fun, interactive penalty shootout game built with HTML, CSS, and JavaScript.

## About the Game

Test your penalty-taking skills! Choose your shooting direction and try to score past the goalkeeper. The keeper will try to save your shot, so pick wisely!

## Features

- Interactive penalty shootout gameplay
- Score tracking system
- Responsive goalkeeper AI
- Clean, modern UI design
- Play directly in your browser

## How to Play

1. Open `index.html` in your web browser
2. Click on one of the three goal sections (Left, Center, or Right)
3. Watch as you take your shot and the goalkeeper dives
4. Try to score as many goals as you can!

## Game Controls

- **Click Left Zone**: Shoot to the left side of the goal
- **Click Center Zone**: Shoot straight down the middle
- **Click Right Zone**: Shoot to the right side of the goal

## Installation

No installation required! Simply:

```bash
# Clone the repository
git clone <repository-url>

# Open the game
open index.html
```

Or just double-click `index.html` to play in your browser.

## Analytics Dashboard

This repository also includes a powerful Streamlit-based analytics dashboard for visualizing data!

### Features

- Upload CSV/Excel files for instant visualization
- Automatic data preprocessing and cleaning
- Interactive charts and graphs using Plotly
- KPI metrics dashboard
- Trend analysis over time
- Language distribution visualization
- Time-based activity heatmaps
- Export processed data as CSV

### Running the Dashboard

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit dashboard
streamlit run analytics_dashboard.py
```

The dashboard will open in your browser at `http://localhost:8501`

### Dashboard Features

- **File Upload**: Support for CSV and Excel files with Korean encoding
- **KPI Metrics**: Total job count, average video duration, popular languages
- **Trend Analysis**: Daily job volume tracking with line charts
- **Language Distribution**: Bar and pie charts for source/target languages
- **Time Patterns**: Heatmap showing activity by day and hour
- **Data Export**: Download cleaned data as CSV

## Technologies Used

- HTML5
- CSS3
- Vanilla JavaScript
- Python (for Analytics Dashboard)
- Streamlit
- Pandas
- Plotly

## Game Mechanics

- The goalkeeper randomly chooses a direction to dive
- If you shoot where the keeper dives, it's a **SAVE**
- If you shoot where the keeper doesn't dive, it's a **GOAL**
- Your score is tracked throughout your session

## Contributing

Feel free to fork this project and add your own features! Some ideas:
- Different difficulty levels
- Goalkeeper difficulty settings
- Sound effects
- Power-up shots
- Tournament mode

## License

MIT License - Feel free to use and modify as you wish!

---

**Football Needs You!** - Answer the call and become a penalty shootout legend! ⚽🥅
