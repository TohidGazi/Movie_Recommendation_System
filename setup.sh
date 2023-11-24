mkdir -p ~/.streamlit/credentials.toml
echo "\
[server]/n/
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
" > ~/.streamlit/config.toml