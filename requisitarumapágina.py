import urllib.request

def requisitar_pagina(url):
        resposta = urllib.request.urlopen(url)
        conteudo = resposta.read(1000)#quantidade de caracteres exibidos da página
        return conteudo
# URL da página que você deseja requisitar
url_pagina = "https://www.uol.com"
# Faz a requisição à página e exibe o conteúdo
conteudo_pagina = requisitar_pagina(url_pagina)
print(conteudo_pagina)