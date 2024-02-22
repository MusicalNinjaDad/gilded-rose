python3 -m venv .venv \
&& . .venv/bin/activate \
&& python3 -m ensurepip \
&& pip install -e .[test,dev] \
&& python3 -m pytest \
&& ruff check .