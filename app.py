import streamlit as st
from duckduckgo_search import DDGS

st.title("DuckDuckGo Search Agent")
st.write("Enter a query below and get search results from DuckDuckGo.")

query = st.text_input("Your Search Query:")

try:
        with DDGS() as ddgs:  # Correct variable name (ddgs instead of ddg)
            results = list(ddgs.text(query, max_results=5))  # Convert generator to list
            
            if not results:
                st.warning("No results found")
            else:
                for idx, r in enumerate(results, start=1):
                    st.markdown(f"**{idx}. [{r['title']}]({r['href']})**")
                    st.caption(r['body'])
                    
    except Exception as e:
        st.error(f"Search failed: {str(e)}")
        st.info("Make sure 'duckduckgo_search' is
