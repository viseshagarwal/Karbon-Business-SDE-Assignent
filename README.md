# Financial Flag Analysis App

This is a simple Flask application that allows users to upload financial data in JSON format and displays financial flags based on the analysis.

## Features

- Upload JSON files containing financial data.
- Calculate and display:
  - Total Revenue Flag
  - Borrowing to Revenue Flag
  - ISCR Flag
- Display the financial flags in a table.

## Technologies Used

- Python
- Flask
- HTML/CSS

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/viseshagarwal/Karbon-Business-SDE-Assignent.git
   cd your-repository-name
   ```



2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your browser and go to `http://localhost:5000`.

3. Upload a JSON file to see the financial flags.

## Deployed App: https://karbon-business-sde-assignent.vercel.app/

## Note

This project is for educational purposes only. The data used in the project is dummy data and does not represent any real-world financial data.
