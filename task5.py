import re
import requests
import bs4


def regex_a(txt):
    match = re.search(r'Product review: \d+', txt)
    return match


def regex_b(txt):
    match = re.search(r'Product review: [1-5]', txt)
    return match


def regex_c(txt):
    match = re.search(r'Product review:\s*[1-5]', txt)
    return match


def regex_d(txt):
    match = re.search(r'[^\n]{3,5}\.', txt)
    return match


def write_text_to_file(txt, file_path):
    f = open(file_path, 'w')
    f.write(txt)
    f.close()


def get_file_length(file_path):
    f = open(file_path)
    f.seek(0, 2)
    file_length = f.tell()
    f.close()
    return file_length


def sum_file_nums(file_path):
    f = open(file_path)
    file_sum = 0
    for line in f:
        file_sum += float(line.strip())
    print(round(file_sum, 10))


def parse_file(file_path, delimiter):
    f = open(file_path)
    matrix = []
    for line in f:
        row_items = [float(item) for item in line.strip().split(delimiter)]
        matrix.append(row_items)
    f.close()
    return matrix


def get_last_k_characters_of_webpage(url, k):
    response = requests.get(url)
    if response.status_code != requests.codes.ok:
        print(f'Sorry, there was an error: {response.status_code}')
    else:
        content = response.text
        return content[-k:]


def get_div_tags(url):
    content = get_last_k_characters_of_webpage(url, 4500)
    soup = bs4.BeautifulSoup(content, 'html.parser')
    item_list = [item for item in soup.select('div')]
    return item_list


def get_id_values_from_div_tags_with_id_attribute(url):
    content = get_last_k_characters_of_webpage(url, 4500)
    soup = bs4.BeautifulSoup(content, 'html.parser')
    item_list = [item.get('id') for item in soup.select('div[id]')]
    return item_list


def get_urls(url):
    content = get_last_k_characters_of_webpage(url, 4500)
    urls_list = re.findall(r'http://www\.[\w.]+\.il/[\w~./]+.html', content)
    return urls_list


