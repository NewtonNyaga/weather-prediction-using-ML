import tkinter as tk
from tkinter import ttk
import webbrowser

class HTMLGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather Forecasting Model")
        self.geometry("800x600")

        # Create a WebView widget
        self.webview = tk.ttk.Notebook(self)
        self.webview.pack(fill=tk.BOTH, expand=True)

        # Load the HTML GUI into WebView
        self.load_html_gui()

    def load_html_gui(self):
        html_page = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Weather Forecasting Model</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                .container {
                    max-width: 600px;
                    margin: 0 auto;
                    background-color: #fff;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                .button {
                    display: block;
                    width: 100%;
                    padding: 10px 20px;
                    margin-top: 20px;
                    font-size: 16px;
                    text-align: center;
                    background-color: #007bff;
                    color: #fff;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    text-decoration: none;
                }
                .button:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Weather Forecasting Model</h1>
                <p>Select CSV file:</p>
                <input type="file" id="fileInput" accept=".csv" style="width: 100%;">
                <button id="predictButton" class="button">Predict</button>
            </div>

            <script>
                document.getElementById("predictButton").addEventListener("click", function() {
                    alert("Predict button clicked!");
                });
            </script>
        </body>
        </html>
        """

        # Create a new tab for WebView
        html_tab = tk.Frame(self.webview)
        self.webview.add(html_tab, text="HTML GUI")

        # Load HTML content into WebView
        browser = tk.ttk.Frame(html_tab)
        browser.pack(fill=tk.BOTH, expand=True)
        browser_text = tk.Text(browser)
        browser_text.pack(fill=tk.BOTH, expand=True)
        browser_text.insert(tk.END, html_page)

        # Disable editing in the WebView
        browser_text.config(state=tk.DISABLED)


if __name__ == "__main__":
    app = HTMLGUI()
    app.mainloop()
