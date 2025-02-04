import google.generativeai as genai
from playwright.sync_api import sync_playwright
import time
import urllib.parse

# Configure Gemini API
GEMINI_API_KEY = 'AIzaSyAZNEYWiW7uPyBZWlKLbq1ie2x1aUuSPDw'
genai.configure(api_key=GEMINI_API_KEY)

def get_user_input():
    print("\n=== Product Search ===")
    query = input("Enter your search query (e.g., 'best wallet 8x11 leatherbound journal'): ")
    return query

def scrape_eaty_products(query):
    products = []
    
    with sync_playwright() as p:
        try:
            # Launch browser with headed mode for debugging
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            
            # Go to Flipkart homepage first
            page.goto("https://www.flipkart.com")
            time.sleep(2)  # Wait for page to load
            
            # Look for and fill the search box
            search_box = page.query_selector('input[name="q"]')
            if search_box:
                search_box.fill(query)  # Fill the search query
                search_box.press("Enter")  # Press Enter to search
                print(f"Searching for: {query}")
            else:
                print("Could not find search box")
            
            time.sleep(120)  # Give JavaScript time to load
            
            # Example selectors - replace these with actual selectors from eaty.com
            product_cards = page.query_selector_all('.product-card')
            
            for card in product_cards:
                try:
                    title_element = card.query_selector('.product-title')
                    price_element = card.query_selector('.product-price')
                    desc_element = card.query_selector('.product-description')
                    link_element = card.query_selector('a')
                    
                    product = {
                        'title': title_element.text_content() if title_element else "No title",
                        'price': price_element.text_content() if price_element else "No price",
                        'description': desc_element.text_content() if desc_element else "No description",
                        'link': link_element.get_attribute('href') if link_element else "#"
                    }
                    products.append(product)
                    print(f"Found product: {product['title']}")
                    
                except Exception as e:
                    print(f"Error extracting product details: {e}")
                    continue
            
        except Exception as e:
            print(f"Error during scraping: {e}")
        finally:
            browser.close()    
    return products

def filter_products_with_gemini(products, original_query):
    try:
        model = genai.GenerativeModel('gemini-pro')
        # Prepare products data for Gemini
        products_text = "\n".join([
            f"Product {i+1}:\nTitle: {p['title']}\nPrice: {p['price']}\nDescription: {p['description']}"
            for i, p in enumerate(products)
        ])
        
        prompt = f"""
        Original search query: {original_query}
        
        Available products:
        {products_text}
        
        Task:
        1. Analyze these products for relevance to the search query
        2. Consider factors like:
           - Match to specified dimensions (8x11)
           - Material (leatherbound)
           - Quality and features
           - Price value
        3. Return the top 5 most relevant products
        
        Format your response as:
        1. [Product Name] - [Price]
           - Why this matches the requirements
           - Key features
           - Any concerns or missing information
        
        Only include products that reasonably match the search criteria.
        """
        
        response = model.generate_content(prompt)
        return response.text
        
    except Exception as e:
        return f"Error filtering products: {e}"

def display_results(filtered_results):
    print("\n=== Filtered Search Results ===")
    print(filtered_results)

def main():
    try:
        # Get user input
        query = get_user_input()
        
        # Step 1: Scrape products
        print("\nScraping products...")
        products = scrape_eaty_products(query)
        
        if products:
            print(f"\nFound {len(products)} products")
            
            # Step 2: Filter and rank products
            filtered_results = filter_products_with_gemini(products, query)
            
            # Display results
            display_results(filtered_results)
        else:
            print("\nNo products found to analyze")
            
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        
    print("\nSearch complete!")

if __name__ == "__main__":
    main()