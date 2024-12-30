import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
import logging
import time
import re
import random

# Setup logging
logging.basicConfig(filename="instagram_scraper.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Rich Console for styled output
console = Console()

def display_header():
    """
    Menampilkan header profesional di terminal.
    """
    console.print(Panel.fit(
        "[bold blue]Instagram Caption Scraper[/bold blue]\n"
        "Created by: [bold green]@syaaikoo[/bold green]\n"
        "[italic]Use responsibly and comply with Instagram policies.[/italic]",
        title="Welcome", subtitle="Version 2.0", style="bold magenta"
    ))

def validate_url(url):
    """
    Memvalidasi apakah URL adalah URL Instagram yang sah.
    """
    instagram_url_pattern = r'^https?://(www\.)?instagram\.com/p/[a-zA-Z0-9_-]+/?$'
    return re.match(instagram_url_pattern, url.strip()) is not None

def get_instagram_caption(post_url):
    """
    Mengambil caption dari URL postingan Instagram.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    for attempt in range(3):  # Retry mechanism
        try:
            response = requests.get(post_url, headers=headers, timeout=10)
            response.raise_for_status()

            # Parsing HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            meta_tag = soup.find('meta', attrs={'property': 'og:description'})

            if meta_tag:
                content = meta_tag.get('content', '')
                caption = content.split('•')[0].strip()  # Extract caption
                logging.info(f"Caption successfully fetched for URL: {post_url}")
                return caption
            else:
                raise ValueError("Caption not found in meta tags.")

        except requests.exceptions.RequestException as e:
            logging.warning(f"HTTP error on attempt {attempt + 1} for URL {post_url}: {e}")
        except Exception as e:
            logging.warning(f"Parsing error on attempt {attempt + 1} for URL {post_url}: {e}")
        time.sleep(random.uniform(2, 5))  # Random delay to avoid detection

    return None

def process_urls():
    """
    Memproses daftar URL Instagram dan menampilkan hasil di terminal.
    """
    console.print("[bold cyan]Masukkan daftar URL Instagram (pisahkan dengan koma atau masukkan file):[/bold cyan]")
    input_data = Prompt.ask("[bold yellow]Input URLs or File Path[/bold yellow]")

    if input_data.endswith('.txt'):
        with open(input_data, 'r', encoding='utf-8') as file:
            urls = [line.strip() for line in file.readlines()]
    else:
        urls = input_data.split(',')

    urls = [url.strip() for url in urls if validate_url(url)]

    if not urls:
        console.print("[bold red]Tidak ada URL Instagram yang valid.[/bold red]")
        return

    keyword_filter = Prompt.ask(
        "[bold green]Masukkan kata kunci untuk filter (opsional):[/bold green]",
        default=None
    )

    output_file = Prompt.ask(
        "[bold magenta]Nama file output untuk menyimpan caption (contoh: captions.txt):[/bold magenta]",
        default="captions.txt"
    )

    captions = []
    failed_urls = []

    table = Table(title="Instagram Caption Results", show_lines=True)
    table.add_column("URL", style="cyan", no_wrap=True)
    table.add_column("Caption", style="green")
    table.add_column("Status", style="bold magenta")

    for url in urls:
        console.print(f"[cyan]Processing URL:[/cyan] {url}")
        caption = get_instagram_caption(url)

        if caption:
            if keyword_filter and keyword_filter.lower() not in caption.lower():
                table.add_row(url, caption, "[yellow]Filtered[/yellow]")
                continue

            captions.append(f"URL: {url}\nCaption: {caption}\nWord Count: {len(caption.split())}\n")
            table.add_row(url, caption, "[green]Success[/green]")
        else:
            failed_urls.append(url)
            table.add_row(url, "N/A", "[red]Failed[/red]")

    console.print("\n")
    console.print(table)

    # Save captions to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(captions))

    console.print(f"[bold green]Hasil telah disimpan ke file:[/bold green] {output_file}")

    # Save failed URLs to a separate file
    if failed_urls:
        failed_file = "failed_urls.txt"
        with open(failed_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(failed_urls))
        console.print(f"[bold red]URL yang gagal diproses disimpan ke file:[/bold red] {failed_file}")

def main():
    """
    Fungsi utama untuk menjalankan fitur-fitur script.
    """
    display_header()
    process_urls()
    console.print("\n[bold blue]Terima kasih telah menggunakan Instagram Caption Scraper.[/bold blue]")

if __name__ == "__main__":
    main()