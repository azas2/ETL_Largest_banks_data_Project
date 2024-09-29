<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Largest Banks Data Extraction Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>

    <h1>🏦 Largest Banks Data Extraction Project</h1>

    <h2>🔧 Requirements</h2>
    <p>To run this project, you'll need:</p>
    <ul>
        <li>Python 3.x</li>
        <li>Libraries:
            <ul>
                <li><code>pandas</code></li>
                <li><code>requests</code></li>
                <li><code>beautifulsoup4</code></li>
                <li><code>sqlite3</code></li>
                <li><code>numpy</code></li>
            </ul>
        </li>
    </ul>
    <p>You can install the required libraries using:</p>
    <pre><code>pip install pandas requests beautifulsoup4 numpy</code></pre>

    <h2>📂 File Structure</h2>
    <ul>
        <li><code>main.py</code> (your script)</li>
        <li><code>exchange_rate.csv</code> (CSV file containing currency exchange rates)</li>
        <li><code>Largest_banks_data.csv</code> (output CSV file)</li>
        <li><code>Banks.db</code> (SQLite database file)</li>
        <li><code>code_log.txt</code> (log file for tracking progress)</li>
    </ul>

    <h2>🚀 Getting Started</h2>
    <ol>
        <li>Clone this repository or download the script.</li>
        <li>Ensure you have the <code>exchange_rate.csv</code> file in the same directory.</li>
        <li>Run the script:</li>
        <pre><code>python main.py</code></pre>
    </ol>

    <h2>📊 Queries Available</h2>
    <p>You can run the following queries after loading data into the database:</p>
    <ul>
        <li><strong>View All Data:</strong>
            <pre><code>SELECT * FROM Largest_banks;</code></pre>
        </li>
        <li><strong>Average Market Capitalization (in GBP):</strong>
            <pre><code>SELECT AVG(MC_GBP_Billion) FROM Largest_banks;</code></pre>
        </li>
        <li><strong>Top 5 Banks:</strong>
            <pre><code>SELECT Name FROM Largest_banks LIMIT 5;</code></pre>
        </li>
    </ul>

    <h2>📜 Logging</h2>
    <p>All progress and errors are logged in <code>code_log.txt</code> for your reference.</p>

    <h2>📬 Contact</h2>
    <p>For questions or feedback, feel free to reach out!</p>

</body>
</html>
