# Chinese Medicinal Materials Price Crawler

A high-concurrency crawler project designed to scrape market price data of Chinese medicinal materials from [Zhongyao Tiandi Network](https://www.zyctd.com/). It adopts a **Multiprocessing + Asynchronous Coroutine** architecture for efficient data collection and supports exporting data to Excel/CSV formats.

## Project Introduction

This crawler aims to fetch price data (including medicinal material name, specification, market, price, trend, weekly/monthly/annual price changes) from Zhongyao Tiandi Network. It uses a hybrid concurrent architecture:

- **Multiprocessing**: Distributes URL groups to multiple processes to fully utilize multi-core CPU resources.
- **Asynchronous Coroutine**: Uses `asyncio` + `aiohttp` within each process to execute asynchronous HTTP requests, improving request efficiency.
- **Data Persistence**: Saves crawled data as Excel or CSV files via `pandas`, with configurable output formats.
- **Logging System**: A comprehensive logging system (file + console) to track crawling progress and error information.

## Technology Stack

| Technology          | Purpose                                |
| ------------------- | -------------------------------------- |
| Python 3.10+        | Core programming language              |
| `multiprocessing`   | Multiprocess task allocation           |
| `asyncio`/`aiohttp` | Asynchronous HTTP requests             |
| `lxml`              | HTML parsing (XPath method)            |
| `pandas`            | Data processing and export (Excel/CSV) |
| `logging`           | Log management                         |

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/medicinal-materials-crawler.git
cd medicinal-materials-crawler
```

### 2. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install aiohttp lxml pandas openpyxl
```

- `openpyxl` is a necessary dependency for pandas to write Excel files.

## Usage

Start crawling by running the main entry file directly:

```bash
python main.py
```

### Execution Flow

1. The system generates URLs for pages 1 to 122 of the target website (configurable in `settings.py`).
2. URLs are grouped and assigned to multiple processes.
3. Each process uses asynchronous coroutines to crawl and parse data from its assigned URL group.
4. Crawled data is saved to the `./data` directory (automatically created if it does not exist) in Excel/CSV format.
5. Logs are recorded in the `./log/spider.log` file and printed to the console in real time.

## Configuration Instructions

Core configuration files are located in the `config` directory:

### 1. `settings.py`

- `URL_POSITION`: URL template for target pages (page number placeholder: `{}`).
- `PageConfig`:
  - `START`/`STOP`: Start/end page numbers for crawling (default: 1 to 122).
  - `STEP`: Number of URLs assigned to each process (default: 32).
- `FileType`:
  - `EXCEL=1`: Save data as Excel format (.xlsx).
  - `CSV=1`: Save data as CSV format (.csv).
- `DATE_PATH`: Path template for output files (saved to the `./data` directory).

### 2. `http_settings.py`

- `HEADERS`: HTTP request headers (customize `user-agent` to avoid anti-crawling).

### 3. `logging_settings.py`

- `LOGGER_NAME`: Name of the logger instance.
- `LOGGER_DIR_PATH`: Log file directory (default: `./log`).
- `LOGGER_FILE_PATH`: Log file path (default: `./log/spider.log`).

## Project Structure

```Plain
medicinal-materials-crawler/
├── core/                     # Core business logic
│   ├── service.py            # Process management and task execution
│   └── handlers.py           # Asynchronous crawling and HTML parsing
├── config/                   # Configuration file directory
│   ├── settings.py           # Core configuration (URL, page numbers, file type)
│   ├── http_settings.py      # HTTP request header configuration
│   └── logging_settings.py   # Log configuration
├── save_data/                # Data persistence module
│   └── dao.py                # Save data to Excel/CSV via pandas
├── utils/                    # Utility functions directory
│   ├── logger.py             # Log initialization
│   └── utils.py              # URL generation, batch asynchronous crawling
├── data/                     # Output directory (auto-created)
├── log/                      # Log directory (auto-created)
├── main.py                   # Project entry file
└── README.md                 # Project documentation
```

## Notes

1. **Anti-Crawling Note**: The crawler adds a 0.1-second delay (`asyncio.sleep(0.1)`) between requests to avoid excessive pressure on the target server. If you need to adjust the delay, ensure compliance with the website's robots.txt protocol.
2. **File Format**: The default output format is CSV (configurable to Excel in `settings.py`).
3. **Error Handling**: Basic timeout handling (10 seconds) has been added for HTTP requests; for production use, it is recommended to extend the error handling logic.
4. **Concurrency Configuration**: The number of processes is determined by the number of URL groups (122 pages are divided into 4 groups by default). The number of processes can be modified by adjusting `PageConfig.STEP`.

## Open Source License

This project is licensed under the MIT Open Source License - see the LICENSE file for details.
