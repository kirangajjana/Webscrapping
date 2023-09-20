import streamlit as st
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

st.title("Web Scraping Application")

# Function to scrape website and generate PDF
def scrape_website_and_generate_pdf(url, pdf_filename):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract and display the content on the Streamlit app
        st.subheader("Scraped Data:")
        scraped_data = soup.get_text()
        st.text(scraped_data)

        # Create a PDF with the scraped content
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.drawString(100, 750, "Scraped Data:")
        c.drawString(100, 730, scraped_data)
        c.save()

        st.success(f"PDF saved as {pdf_filename}")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Streamlit app UI
st.write("Enter the URL of the website you want to scrape:")
website_url = st.text_input("Website URL")

if st.button("Scrape and Save as PDF"):
    if website_url:
        pdf_filename = "scraped_data3.pdf"
        scrape_website_and_generate_pdf(website_url, pdf_filename)
    else:
        st.warning("Please enter a website URL first.")

st.write("made by kiran gajjana nit sikkim")
