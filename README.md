<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>🏦 Largest Banks Data Extraction Project</h1>

<p>This project extracts data about the largest banks in the world from Wikipedia, transforms it, and stores it in both a CSV file and an SQLite database. The extracted data includes market capitalization in various currencies.</p>

<h2>📑 Table of Contents</h2>
<ul>
    <li><a href="#requirements">🔧 Requirements</a></li>
    <li><a href="#file-structure">📂 File Structure</a></li>
    <li><a href="#getting-started">🚀 Getting Started</a></li>
    <li><a href="#functionality">🛠️ Functionality</a></li>
    <li><a href="#license">📄 License</a></li>
    <li><a href="#contributing">🤝 Contributing</a></li>
</ul>

<h2 id="requirements">🔧 Requirements</h2>
<p>To run this project, you'll need:</p>
<ul>
    <li><b>Python 3.x</b></li>
    <li><b>Libraries:</b>
        <ul>
            <li>pandas</li>
            <li>requests</li>
            <li>beautifulsoup4</li>
            <li>numpy</li>
            <li>sqlite3</li>
        </ul>
    </li>
</ul>
<p><b>Install the required libraries:</b></p>
<pre><code>pip install pandas requests beautifulsoup4 numpy</code></pre>

<h2 id="file-structure">📂 File Structure</h2>
<pre><code>
 main.py                   # Main script for data extraction and transformation
 exchange_rate.csv         # CSV file with currency exchange rates
 Largest_banks_data.csv    # Output CSV file with bank data
 Banks.db                  # SQLite database file
 code_log.txt              # Log file for tracking progress
</code></pre>

<h2 id="getting-started">🚀 Getting Started</h2>
<p>1. <b>Clone the repository:</b></p>
<pre><code>git clone &lt;repository-url&gt;</code></pre>
<p>2. <b>Navigate to the directory:</b></p>
<pre><code>cd &lt;repository-name&gt;</code></pre>
<p>3. <b>Ensure <code>exchange_rate.csv</code> is in the directory.</b></p>
<p>4. <b>Run the script:</b></p>
<pre><code>python main.py</code></pre>
<p>5. <b>Check <code>code_log.txt</code> for updates on progress.</b></p>

<h2 id="functionality">🛠️ Functionality</h2>
<ul>
    <li><b>Data Extraction:</b> Fetches bank data from the specified Wikipedia page.</li>
    <li><b>Data Transformation:</b> Cleans and converts the data, adding market capitalization in GBP, EUR, and INR based on exchange rates.</li>
    <li><b>Data Loading:</b> Saves the transformed data to a CSV file and an SQLite database.</li>
    <li><b>Querying:</b> Allows running SQL queries to retrieve specific information from the database.</li>
</ul>

<h2 id="license">📄 License</h2>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>

<h2 id="contributing">🤝 Contributing</h2>
<p>If you would like to contribute to this project, please fork the repository and submit a pull request.</p>

<h2 id="contact">📞 Contact</h2>
<p>For inquiries, contact <a href="ahmed679942@gmail.com">my_emial</a>.</p>

</body>
</html>
