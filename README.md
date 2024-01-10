# Football Fixtures API

This project provides a simple API to retrieve football fixtures using the Football Data API. ⚽📅

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.x 🐍
- Flask 🌐
- Requests library 📡

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hkimi02/football-fixtures-api.git
   ```

2. **Install the required dependencies:**

   ```bash
   pip install flask requests
   ```

### Usage

1. Obtain an API key from [Football Data API](https://www.football-data.org/). 🔑

2. Replace `'your_api_key'` in `main.py` with your actual API key.

3. Run the Flask app:

   ```bash
   python main.py
   ```

4. Open your browser or use a tool like `curl` or Postman to send a GET request:

   - Retrieve Premier League fixtures:

     ```bash
     http://127.0.0.1:5000/get_fixtures?league_id=2021
     ```

   - Retrieve a list of all available leagues:

     ```bash
     http://127.0.0.1:5000/get_all_leagues
     ```

### API Endpoints

- `/get_fixtures`
  - Method: GET
  - Parameters:
    - `league_id` (required): ID of the football league (e.g., 2021 for Premier League).

- `/get_all_leagues`
  - Method: GET
  - Retrieves a list of all available football leagues.

### Example Response

```json
{
  "fixtures": [
    {
      "homeTeam": {"name": "TeamA"},
      "awayTeam": {"name": "TeamB"},
      "date": "2023-01-01T18:00:00Z",
      "status": "SCHEDULED"
    },
    // More fixtures...
  ]
}
```

### Contributing

Contributions are welcome! Please feel free to open issues or pull requests. 🙌
