import requests
url = 'https://raw.githubusercontent.com/BC-SECURITY/Empire/a58e0a5e608b1ebed5f81d8018105d020735db89/data/module_source' \
      '/situational_awareness/network/powerview.ps1'

resp = requests.get(url)
parser = resp.content
parser = str(parser)
parser = parser.replace(' ', '')
parser2 = parser.split('function')
func_names = list()
analizar = ['(', ')', '{', '}']
for x in parser2[1:]:
    if '{' in x:
        parser_func = x[:x.find('{')]
        if parser_func.find('[') == -1:
            if parser_func.find('(') == -1:
                if parser_func.find(')') == -1:
                    if len(parser_func) < 100:
                        func_names.append(parser_func)
