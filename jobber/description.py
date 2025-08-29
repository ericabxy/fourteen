def parse_tr_content(tag, name):
    content_s = str(tag.find_all(class_=name)[0])
    linebreaks = content_s.split('<br/>')
    content_t = []
    for para in linebreaks:
        soup = BeautifulSoup(para, 'html.parser')
        content_t.append(soup.text.strip( ))
    return content_t
